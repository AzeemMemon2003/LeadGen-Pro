import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
} from "recharts";

const data = [
  { name: "High", value: 42 },
  { name: "Medium", value: 81 },
  { name: "Low", value: 125 },
];

const COLORS = [
  "#ef4444",
  "#f59e0b",
  "#3b82f6",
];

export default function PriorityChart() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md border">

      <h2 className="mb-6 text-xl font-semibold">
        Priority Distribution
      </h2>

      <div className="h-72">

        <ResponsiveContainer>

          <PieChart>

            <Pie
              data={data}
              dataKey="value"
              outerRadius={90}
            >

              {data.map((entry, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index]}
                />
              ))}

            </Pie>

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}