import { useEffect, useState } from "react";
import { getLeads } from "../api/leadApi";

export default function Leads() {
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadLeads();
  }, []);

  async function loadLeads() {
    try {
      const data = await getLeads();
      setLeads(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  if (loading) return <h2>Loading...</h2>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Leads</h1>

      <table className="w-full border">
        <thead className="bg-gray-200">
          <tr>
            <th className="border p-2">Company</th>
            <th className="border p-2">Website</th>
            <th className="border p-2">Priority</th>
            <th className="border p-2">Status</th>
          </tr>
        </thead>

        <tbody>
          {leads.map((lead, index) => (
            <tr key={index}>
              <td className="border p-2">{lead.company}</td>
              <td className="border p-2">{lead.website}</td>
              <td className="border p-2">{lead.priority}</td>
              <td className="border p-2">{lead.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}