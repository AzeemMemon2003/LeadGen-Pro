import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  Legend,
} from "recharts";

const COLORS = [
  "#ef4444",
  "#f59e0b",
  "#3b82f6",
];

export default function PriorityChart({ data }) {

  if (!data) return null;

  const chartData = [
    {
      name: "High",
      value: data.high,
    },
    {
      name: "Medium",
      value: data.medium,
    },
    {
      name: "Low",
      value: data.low,
    },
  ];

  return (
    <div className="rounded-2xl border bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold">
        Priority Distribution
      </h2>

      <div className="h-72">

        <ResponsiveContainer width="100%" height="100%">

          <PieChart>

            <Pie
              data={chartData}
              dataKey="value"
              nameKey="name"
              outerRadius={90}
              label
            >

              {chartData.map((entry, index) => (
                <Cell
                  key={entry.name}
                  fill={COLORS[index]}
                />
              ))}

            </Pie>

            <Tooltip />
            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}