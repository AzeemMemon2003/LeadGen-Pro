import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function getDashboard() {
  const res = await API.get("/api/dashboard");
  return res.data;
}