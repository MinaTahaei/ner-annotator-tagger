import axios from "axios";

const instance = axios.create({
  baseURL:  'http://109.122.253.142'+ ':5555',
  
});

export default instance;
