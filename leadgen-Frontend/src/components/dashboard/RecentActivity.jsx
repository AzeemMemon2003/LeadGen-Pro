export default function RecentActivity({ activity }) {

  if (!activity || activity.length === 0) {

    return (

      <div className="rounded-2xl border bg-white p-6 shadow-md">

        <h2 className="mb-5 text-xl font-semibold">
          Recent Activity
        </h2>

        <p className="text-slate-500">
          No recent activity found.
        </p>

      </div>

    );

  }

  return (

    <div className="rounded-2xl border bg-white p-6 shadow-md">

      <h2 className="mb-5 text-xl font-semibold">
        Recent Activity
      </h2>

      <div className="space-y-4">

        {activity.map((lead, index) => (

          <div
            key={index}
            className="flex items-center justify-between border-b pb-3 last:border-none"
          >

            <div className="flex items-center gap-3">

              <div className="h-3 w-3 rounded-full bg-blue-500"></div>

              <div>

                <p className="font-medium">
                  {lead.company}
                </p>

                <p className="text-sm text-slate-500">
                  {lead.website}
                </p>

              </div>

            </div>

            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium">
              {lead.priority}
            </span>

          </div>

        ))}

      </div>

    </div>

  );

}