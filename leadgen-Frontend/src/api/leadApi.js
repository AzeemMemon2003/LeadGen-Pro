import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const scanWebsite = async (url) => {
  const res = await API.post("/api/scan", {
    websites: [url],
  });

  return res.data;
};

export const getLeads = async () => {
  const res = await API.get("/api/leads");

  console.log("Axios Response:", res.data);

  return res.data;
};
export async function updateLeadStatus(id, status) {

  const response = await fetch(
    `http://127.0.0.1:8000/api/leads/${id}`,
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        status,
      }),
    }
  );

  return await response.json();
}