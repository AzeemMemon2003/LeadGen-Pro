import StatGrid from "../components/dashboard/StatGrid";
import RecentActivity from "../components/dashboard/RecentActivity";
import PriorityChart from "../components/dashboard/PriorityChart";

export default function Dashboard() {
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

      <StatGrid />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <RecentActivity />

        <PriorityChart />

      </div>

    </div>
  );
}