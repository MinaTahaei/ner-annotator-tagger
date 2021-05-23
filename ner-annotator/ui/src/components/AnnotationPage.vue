<template>
  <div class="columns is-desktop">
    <div class="column is-one-fifth">
      <AnnotationSidebar :current="currentSentence" />
    </div>
    <div class="column">
      <div class="panel m-4">
        <div class="panel-heading">
          <classes-block />
        </div>
        <div class="panel-block">
          <div id="editor" dir="rtl">
            <component
              :is="t.type === 'token' ? 'Token' : 'TokenBlock'"
              :id="'t' + t.start"
              v-for="t in tm.tokens"
              :token="t"
              :key="t.start"
              @remove-block="onRemoveBlock"
            />
          </div>
        </div>
        <div class="panel-block">
          <div class="field is-grouped">
            <p class="control">
              <button class="button is-danger is-outlined" @click="resetBlocks">
                Reset
              </button>
            </p>
            <p class="control">
              <button class="button" @click="skipCurrentSentence">Skip</button>
            </p>
            <p class="control">
              <button class="button is-link" @click="saveTags">Save</button>
            </p>
          </div>
        </div>
      </div>
      <template v-for="file in files" :key="file">
        <button @click="select_file(file)"  class="file-box">{{file}}</button>

      </template>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import { mapMutations } from "vuex";
import axios from "../axios";
import Token from "./Token";
import TokenBlock from "./TokenBlock";
import AnnotationSidebar from "./AnnotationSidebar";
import ClassesBlock from "./ClassesBlock.vue";
import TokenManager from "./token-manager";
import Swal from "sweetalert2";
export default {
  name: "AnnotationPage",
  data: function () {
    return {
      files:[],
      selectedFile:'',
      tm: new TokenManager([]),
      currentSentence: {},
      currentIndex: 0,
      redone: "",
    };
  },
  components: {
    Token,
    TokenBlock,
    AnnotationSidebar,
    ClassesBlock,
  },
  computed: {
    ...mapState(["inputSentences", "classes", "annotations", "currentClass"]),
  },
  watch: {
    inputSentences() {
      alert("change")
      this.currentIndex = 0;
      this.tokenizeCurrentSentence();
    },
  },
  created() {
    if (this.inputSentences.length) {
      this.tokenizeCurrentSentence();
    }
    document.addEventListener("mouseup", this.selectTokens);
  },
  beforeUnmount() {
    document.removeEventListener("mouseup", this.selectTokens);
  },
  mounted(){
    this.getFiles();
  },
  methods: {
    ...mapMutations(["setInputSentences"]),
    getFiles(){
      
      axios
        .get("/files")
        .then((res) => {
          this.files = res.data;
        })
        .catch((err) => alert(err));
    },
    select_file(name){
      this.selectFile = name;
      axios.get(`/files/${name}`)
        .then((res) => {
          
          this.setInputSentences(res.data);
          
        })
        .catch((err) => alert(err));
    },
    tokenizeCurrentSentence() {
      if (this.currentIndex >= this.inputSentences.length) {
        // TODO show completed message
        // alert("You have completed all the sentences");
        return;
      }
      this.currentSentence = this.inputSentences[this.currentIndex];
      axios
        .post("/tokenize", this.currentSentence)
        .then((res) => {
          this.tm = new TokenManager(res.data.tokens);
        })
        .catch((err) => alert(err));
    },
    selectTokens() {
      let selection = document.getSelection();

      if (
        selection.anchorOffset === selection.focusOffset &&
        selection.anchorNode === selection.focusNode
      )
        return;

      let startIdx, endIdx;
      try {
        startIdx = parseInt(
          selection.anchorNode.parentElement.id.replace("t", "")
        );
        endIdx = parseInt(
          selection.focusNode.parentElement.id.replace("t", "")
        );
      } catch (e) {
        console.log("selected text were not tokens");
        return;
      }

      if (!this.classes.length && selection.anchorNode) {
        alert(
          "There are no Tags available. Kindly add some Tags before tagging."
        );
        selection.empty();
        return;
      }

      this.tm.addNewBlock(startIdx, endIdx, this.currentClass);
      selection.empty();
    },
    onRemoveBlock(blockStart) {
      this.tm.removeBlock(blockStart);
    },
    resetBlocks() {
      this.tm.resetBlocks();
    },
    skipCurrentSentence() {
      this.currentIndex++;
      this.tokenizeCurrentSentence();
    },
    saveTags() {
      axios
        .post("/detokenize", { tokens: this.tm.words })
        .then((res) => {
          let fun = this.tm.exportAsAnnotation();
          let len = fun.length;
          let array = [];
          for (let i = 0; i < len; i++) {
            if (!array.includes(fun[i][2])) {
              array.push(fun[i][2]);
            }
          }
          len = this.$store.state.classes.length;
          let notIncluded = [];
          for (let i = 0; i < len; i++) {
            if (!array.includes(this.$store.state.classes[i].name.toString())) {
              notIncluded.push(this.$store.state.classes[i].name.toString());
            }
          }
          console.log(notIncluded.length + " : " + len)
          if (notIncluded.length>0) {
            Swal.fire({
              title: "Do you want to save?",
              showDenyButton: true,
              text: "you have not selected these tokens yet : \n" + notIncluded,
              confirmButtonText: `Save`,
              denyButtonText: `Don't save`,
            }).then((result) => {
              /* Read more about isConfirmed, isDenied below */
              if (result.isConfirmed) {
                this.$store.commit("addAnnotation", [
                res.data.text,
                { entities: this.tm.exportAsAnnotation() },
                ]);
                this.currentIndex++;
                this.tokenizeCurrentSentence();
        
        
                Swal.fire("Saved!", "", "success");
              } else if (result.isDenied) {
                Swal.fire("Changes are not saved", "", "info");
              }
            });
          }

          
        })
        .catch((e) => {
          console.log(e);
        });
    },
    dialogBox() {},
  },
};
</script>

<style lang="scss">
#editor {
  padding: 1rem;
}
.file-box{
  margin: 1rem;
  padding: 10px;
  border-radius: 20px;
  box-shadow: 0 0 3px 0.5px #000;
  border:none;
  background-color:rgba(71, 231, 170, 0.466);
  text-align: center;
  font-size: 12px;
}
</style>
