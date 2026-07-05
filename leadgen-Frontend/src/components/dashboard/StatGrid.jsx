import KPICard from "./KPICard";

export default function StatGrid() {

  return (

    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

      <KPICard
        title="Total Leads"
        value="248"
        color="bg-blue-500"
      />

      <KPICard
        title="Qualified"
        value="163"
        color="bg-green-500"
      />

      <KPICard
        title="Contacted"
        value="91"
        color="bg-yellow-500"
      />

      <KPICard
        title="High Priority"
        value="42"
        color="bg-red-500"
      />

    </div>

  );
}