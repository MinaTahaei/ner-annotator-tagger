<template>
  <div class="my-2">
    <button class="button is-danger" @click="generateJSONExport()">
      Export Annotations
    </button>
    <button class="button is-primary" style="margin-left:10px">
        <a :href="pdfLink" download="guide.pdf" style="color:white">Guide</a> 
        </button>
  </div>
</template>
<script>
import {mapState} from "vuex";
import Swal from "sweetalert2";
export default {
  name: "Export",
  computed: {
    ...mapState(["annotations", "classes"]),
  },
  data(){
    return{
      pdfLink:require("../../../guide.pdf"),
    }
  },
  methods: {
    generateJSONExport() {
      if(this.$store.state.taggerName === "" | this.$store.state.taggerName === undefined){
        Swal.fire("Enter your name","","warning");
        return;
      }
      const filename = this.$store.state.fileName + ".json";
      const output = {
        'taggerName':this.$store.state.taggerName,
        "classes": this.classes.map(c => c.name),
        "annotations": this.annotations
      }

      const jsonStr = JSON.stringify(output);
      console.log(jsonStr)
      let element = document.createElement("a");
      element.setAttribute(
        "href",
        "data:text/plain;charset=utf-8," + encodeURIComponent(jsonStr)
      );
      element.setAttribute("download", filename);

      element.style.display = "none";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    },
    // showSample(){
    //   const filename = "guide.json";
      
    //   let element = document.createElement("a");
    //   element.setAttribute(
    //     "href =" +"../../../dist.7z",
    //     "data:text/plain;charset=utf-8," + encodeURIComponent()
    //   );
    //   element.setAttribute("download", filename);

    //   element.style.display = "none";
    //   document.body.appendChild(element);
    //   element.click();
    //   document.body.removeChild(element);
    // }
  },
};
</script>
