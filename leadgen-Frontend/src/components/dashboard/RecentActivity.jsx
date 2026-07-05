const activity = [
  "Google scanned",
  "Tesla qualified",
  "Apple contacted",
  "Microsoft converted",
];

export default function RecentActivity() {

  return (

    <div className="rounded-2xl bg-white border shadow-md p-6">

      <h2 className="text-xl font-semibold mb-5">
        Recent Activity
      </h2>

      <div className="space-y-4">

        {activity.map((item, index) => (

          <div
            key={index}
            className="flex items-center gap-4"
          >

            <div className="h-3 w-3 rounded-full bg-blue-500"/>

            <p>{item}</p>

          </div>

        ))}

      </div>

    </div>

  );
}