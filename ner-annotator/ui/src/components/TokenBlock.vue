<template>
  <mark :style="bgColor">
    <Token :token="t" v-for="t in token.tokens" :key="t.start" />
    <span class="tag">
      {{tagName(token.label)}}
      <a class="delete is-small" @click="$emit('remove-block', token.start)"></a>
    </span>
  </mark>
</template>
<script>
import Token from "./Token";

export default {
  name: "TokenBlock",
  emits: ["remove-block"],
  data:function() {
    return {
      showClose: false,
      bgColor:''
    }
  },
  methods:{
    tagName(i){
      let ALL_TAGS = {
      name: "PER",
      gender: "GEN",
      date: "DATE",
      city: "CITY",
      address: "LOC",
      skills: "SKILL",
      institute_name: "INS",
      degree: "DEGREE",
      major: "MAJOR",
      work_organization: "ORG",
      position: "POS",
      certificates: "CER",
      english_skill_level: "ENGLEVEL",
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
  mounted(){
    switch(this.tagName(this.token.label)){
      case "name":
        this.bgColor = "background-color:#f85aba !important"
        break;
      case "email":
        this.bgColor = "background-color:#87ceeb !important"
        break;
      case "landline":
        this.bgColor = "background-color:#ddae21 !important"
        break;
      case "gender":
        this.bgColor = "background-color:#ddae21 !important"
        break;
      case "personal_summary":
        this.bgColor = "background-color:#FF5733  !important"
        break;
      case "birth_Date":
        this.bgColor = "background-color:#34D037 !important"
        break;
      case "city":
        this.bgColor = "background-color:#9D34D1 !important"
        break;
      case "address":
        this.bgColor = "background-color:#D13451 !important"
        break;
      case "skills":
        this.bgColor = "background-color:#7127E1 !important"
        break;
      case "institute_name":
        this.bgColor = "background-color:#1A5BF4 !important"
        break;
      case "degree":
        this.bgColor = "background-color:#3FF51B !important"
        break;
      case "education_start_year":
        this.bgColor = "background-color:#A5F51B !important"
        break;
      case "education_end_year":
        this.bgColor = "background-color:#F5A11B !important"
        break;
      case "education_summary":
        this.bgColor = "background-color:#F51B1B !important"
        break;
      case "work_organization":
        this.bgColor = "background-color:#1BF5CD !important"
        break;
      case "position":
        this.bgColor = "background-color:#F5DB1B !important"
        break;
      case "work_start_year":
        this.bgColor = "background-color:#F51BAC !important"
        break;
      case "work_end_year":
        this.bgColor = "background-color:#A51BF5 !important"
        break;
      case "work_summary":
        this.bgColor = "background-color:#1B6EF5 !important"
        break;
      case "certificates":
        this.bgColor = "background-color:#55F51B !important"
        break;
      case "english_skill_level":
        this.bgColor = "background-color:#F51B55 !important"
        break;
      
    }
  },
  props: {
    token: {
      type: Object,
      requried: true
    }
  },
  components: {
    Token
  },
  
  
  
}
</script>

<style lang="scss">
mark {
  padding: 0.5rem;
  position: relative;
  background-color: burlywood;
  &::after {
    content: var(--tag);
    padding: 0.3rem;
    color: darkslategray;
    font-size: small;
  }
}
.close-btn {
  cursor: pointer;
  font-size: small;
  position: absolute;
  width: 1rem;
  height:1rem;
  padding-left: 0.2rem;
  border-radius: 50%;
  background-color: black;
  color: white;
}
.delete {
  margin-left: 10px;
}
</style>