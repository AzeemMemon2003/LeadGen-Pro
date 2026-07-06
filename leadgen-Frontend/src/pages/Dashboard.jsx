import { useEffect, useState } from "react";

import { getDashboard } from "../api/dashboardApi";

import StatGrid from "../components/dashboard/StatGrid";
import RecentActivity from "../components/dashboard/RecentActivity";
import PriorityChart from "../components/dashboard/PriorityChart";

export default function Dashboard() {

  const [dashboard, setDashboard] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    loadDashboard();

  }, []);

  async function loadDashboard() {

    try {

      const data = await getDashboard();

      setDashboard(data);

    } catch (err) {

      console.error(err);

    } finally {

      setLoading(false);

    }

  }

  if (loading) {

    return (
      <div className="text-xl font-semibold">
        Loading Dashboard...
      </div>
    );

  }

  return (

    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold">
          Dashboard
        </h1>

        <p className="text-slate-500">
          Overview of your LeadGen CRM
        </p>

      </div>

      <StatGrid stats={dashboard} />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <RecentActivity
          activity={dashboard.recent_activity}
        />

        <PriorityChart
          data={dashboard.priority_distribution}
        />

      </div>

    </div>

  );

}