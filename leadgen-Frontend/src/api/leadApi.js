import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const scanWebsite = async (url) => {
  const res = await API.post("/api/scan", {
    websites: [url],
  });

  return res;
};

export const getLeads = async () => {
  const res = await API.get("/api/leads");

  console.log("Axios Response:", res);

  return res;
};