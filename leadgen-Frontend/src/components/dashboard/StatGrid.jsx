import KPICard from "./KPICard";

export default function StatGrid({ stats }) {

  if (!stats) return null;

  return (

    <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">

      <KPICard
        title="Total Leads"
        value={stats.total_leads}
        color="bg-blue-500"
      />

      <KPICard
        title="Qualified Leads"
        value={stats.qualified}
        color="bg-green-500"
      />

      <KPICard
        title="High Priority"
        value={stats.high_priority}
        color="bg-red-500"
      />

      <KPICard
        title="Contacted"
        value={stats.contacted}
        color="bg-yellow-500"
      />

      <KPICard
        title="Verified Emails"
        value={stats.verified_emails}
        color="bg-emerald-500"
      />

      <KPICard
        title="Average Score"
        value={stats.average_score}
        color="bg-indigo-500"
      />

      <KPICard
        title="Success Rate"
        value={`${stats.success_rate}%`}
        color="bg-purple-500"
      />

      <KPICard
        title="Proposals"
        value={stats.proposal_count}
        color="bg-pink-500"
      />

    </div>

  );

}