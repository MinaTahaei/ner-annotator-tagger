<template>
  <div>
    <!-- <StartPage v-if="currentPage === 'start'" v-on:file-loaded="onFileLoaded" /> -->
    <AnnotationPage  />
  </div>
</template>

<script>

import AnnotationPage from "./components/AnnotationPage";

import "./assets/styles.scss";

export default {
  name: "App",
  data: function() {
    return {
      currentPage: "start",
    };
  },
  components: {
    AnnotationPage,
  },
  methods: {
    onFileLoaded() {
      this.currentPage = "annotator";
    },
  },
};
</script>
