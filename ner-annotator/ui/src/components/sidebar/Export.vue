<template>
  <div class="my-2">
    <button class="button is-danger" @click="generateJSONExport()">
      Export Annotations
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
  },
};
</script>
