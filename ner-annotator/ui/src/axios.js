import axios from "axios";

const instance = axios.create({
  baseURL:  'http://' + window.location.hostname + ':5555',
  
});

export default instance;
