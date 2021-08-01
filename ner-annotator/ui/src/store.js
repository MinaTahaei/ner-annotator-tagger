export const mutations = {
  setInputSentences(state, payload) {
    if (!Array.isArray(payload)) {
      state.originalText = payload;
      payload = payload.split(state.separator);
    }
    state.inputSentences = payload.map((s, i) => ({ id: i, text: s }));
  },
  addClass(state, payload) {
    let existing = state.classes.find((c) => c.name == payload);
    if (existing) {
      return;
    }
    let lastIndex = state.classes.reduce((p, c) => {
      return c.id > p ? c.id : p;
    }, 0);
    state.classes.push({
      id: lastIndex + 1,
      name: payload,
    });
    if (state.classes.length === 1) {
      state.currentClass = state.classes[0];
    }
  },
  removeClass(state, payload) {
    state.classes = state.classes.filter((c) => c.id != payload);
    if (state.currentClass.id === payload) {
      state.currentClass = state.classes[0];
    }
  },
  setCurrentClass(state, payload) {
    state.currentClass = state.classes.find((c) => c.id === payload);
  },
  addAnnotation(state, payload) {
    state.annotations[0]=payload;
  },
  setSeparator(state, payload) {
    state.separator = payload;
    const sentences = state.originalText.split(state.separator);
    state.inputSentences = sentences.map((s, i) => ({ id: i, text: s }));
  },
  setFileName(state,payload){
    state.fileName = payload;
    },
  setTaggerName(state,payload){
    state.taggerName = payload;
    },
  tagName(state ,payload){
      
    
    if(Object.values(state.abbr).includes(payload)){
        let item = Object.values(state.abbr).indexOf(payload)
        
        return Object.keys(state.abbr)[item];
        
      }
      else{
        return payload;
      }
    
  }
};

export const getters = {};
export default {
  state() {
    return {
      originalText: "",
      separator: "---",
      classes: [],
      inputSentences: [],
      annotations: [],
      currentClass: {},
      fileName:"",
      taggerName:"",
       abbr: {
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
      },
     
    };
  },
  getters,
  mutations,
  actions: {},
};
