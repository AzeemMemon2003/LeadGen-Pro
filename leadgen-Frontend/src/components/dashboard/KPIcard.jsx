export default function KPICard({
  title,
  value,
  color = "bg-blue-500",
}) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md border hover:shadow-xl transition">

      <div className="flex justify-between items-center">

        <div>

          <p className="text-sm text-slate-500">
            {title}
          </p>

          <h2 className="mt-2 text-3xl font-bold">
            {value}
          </h2>

        </div>

        <div className={`h-12 w-12 rounded-xl ${color}`} />

      </div>

    </div>
  );
}