<template>
<div>

    <div class="in">
      <label style="font-size:14px">Name : </label>
    <input @keyup="saveName" v-model="username" type="text">

    </div>
  <div class="field is-grouped is-grouped-multiline">
    <div class="control" v-for="cl in classes" :key="cl.id">
      <div class="tags is-medium has-addons">
        <a
          class="tag is-medium"
          :class="{ 'is-link': cl.id === currentClass.id }"
          @click="setCurrentClass(cl.id)"
        >
          {{ tagName(cl.name) }}
        </a>
        <!-- <a class="tag is-medium is-delete" @click="removeClass(cl.id)"></a> -->
      </div>
    </div>

    <p class="control" v-if="showNewClassInput || classes.length === 0">
      <input
        type="text"
        class="input is-inline"
        v-model="newClassName"
        @keyup="onInputKeyup"
        placeholder="NER TAG"
      />
      <button class="button is-info is-inline" @click="saveNewClass">
        Add
      </button>
    </p>

    <!-- <p class="control">
      <button
        class="button is-primary"
        @click="showNewClassInput = true"
      >
        <span class="icon">
          <font-awesome-icon class="fa-lg" icon="plus-square" />
        </span>
      </button>
    </p> -->
  </div>
</div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "ClassesBlock",
  data() {
    return {
      showNewClassInput: false,
      newClassName: "",
      username:'',
    };
  },
  mounted() {
    let ALL_TAGS = {
      name: "PER",
      // gender: "GEN",
      date: "DATE",
      city: "CITY",
      address: "LOC",
      skills: "SKILL",
      institute_name: "INS",
      degree: "DEGREE",
      major: "MAJOR",
      organization: "ORG",
      position: "POS",
      certificates: "CER",
      level: "ENGLEVEL",
    };
    let array = [
      "name",
      // "gender",
      "date",
      "city",
      "address",
      "skills",
      "institute_name",
      "degree",
      "major",
      "organization",
      "position",
      "certificates",
      "level",
    ];
    for (let i = 0; i < array.length; i++){
      

        this.$store.commit("addClass", ALL_TAGS[array[i]]);
      
    }
  },
  computed: {
    ...mapState(["classes", "currentClass"]),
  },
  watch: {
    newClassName(now, then) {
      if (now != then) {
        this.newClassName = now.toUpperCase();
      }
    },
  },
  methods: {
    ...mapMutations(["removeClass", "setCurrentClass"]),
    saveName(){
      this.$store.commit('setTaggerName',this.username)
    },
    saveNewClass() {
      this.$store.commit("addClass", this.newClassName);
      this.showNewClassInput = false;
      this.newClassName = "";
    },
    onInputKeyup(e) {
      if (e.key === "Enter") {
        this.saveNewClass();
      }
    },
    tagName(i){
      let ALL_TAGS = {
      name: "PER",
      // gender: "GEN",
      date: "DATE",
      city: "CITY",
      address: "LOC",
      skills: "SKILL",
      institute_name: "INS",
      degree: "DEGREE",
      major: "MAJOR",
      organization: "ORG",
      position: "POS",
      certificates: "CER",
      level: "ENGLEVEL",
    };
    if(Object.values(ALL_TAGS).includes(i)){
        let item = Object.values(ALL_TAGS).indexOf(i)
        return Object.keys(ALL_TAGS)[item];
        
      }
      else{
        return i;
      }
    }
  },
};
</script>
<style scoped>
.in{
  margin-bottom: 20px;
}
</style>
