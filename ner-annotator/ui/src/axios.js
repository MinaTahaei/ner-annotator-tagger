import axios from "axios";

const instance = axios.create({
  baseURL: 'http://' + window.location.hostname + ':5555',
  timeout: 3000,
});

export default instance;
