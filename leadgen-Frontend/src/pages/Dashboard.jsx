import { useEffect, useState } from "react";
import { getLeads } from "../api/leadApi";

export default function Dashboard() {
  const [stats, setStats] = useState({
    total: 0,
    scanned: 0,
    high: 0,
    conversion: 0,
  });

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const res = await getLeads();

      console.log("API Response:", res.data);

      const leads = Array.isArray(res.data) ? res.data : [];

      const highPriority = leads.filter(
        (lead) =>
          lead.priority === "HIGH" ||
          lead.priority === "WARM"
      ).length;

      setStats({
        total: leads.length,
        scanned: leads.length,
        high: highPriority,
        conversion:
          leads.length > 0
            ? Math.round((highPriority / leads.length) * 100)
            : 0,
      });

    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">
        Dashboard Overview
      </h1>

      <div className="grid grid-cols-4 gap-6">

        <div className="border rounded-lg p-6 shadow">
          <p className="text-gray-500">Total Leads</p>
          <h2 className="text-3xl font-bold">
            {stats.total}
          </h2>
        </div>

        <div className="border rounded-lg p-6 shadow">
          <p className="text-gray-500">Sites Scanned</p>
          <h2 className="text-3xl font-bold">
            {stats.scanned}
          </h2>
        </div>

        <div className="border rounded-lg p-6 shadow">
          <p className="text-gray-500">High Priority</p>
          <h2 className="text-3xl font-bold text-red-600">
            {stats.high}
          </h2>
        </div>

        <div className="border rounded-lg p-6 shadow">
          <p className="text-gray-500">Conversion Rate</p>
          <h2 className="text-3xl font-bold text-green-600">
            {stats.conversion}%
          </h2>
        </div>

      </div>
    </div>
  );
}