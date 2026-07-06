import { useEffect, useState } from "react";
import { Eye } from "lucide-react";
import { getLeads } from "../api/leadApi";
import LeadDrawer from "../components/leads/LeadDrawer";

export default function Leads() {
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");
  const [priority, setPriority] = useState("ALL");

  const [selectedLead, setSelectedLead] = useState(null);
  const [drawerOpen, setDrawerOpen] = useState(false);

  useEffect(() => {
    loadLeads();
  }, []);

  async function loadLeads() {
    try {
      const data = await getLeads();
      setLeads(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  function openLead(lead) {
    setSelectedLead(lead);
    setDrawerOpen(true);
  }

  const filteredLeads = leads.filter((lead) => {
    const matchesSearch =
      lead.company.toLowerCase().includes(search.toLowerCase()) ||
      lead.website.toLowerCase().includes(search.toLowerCase());

    const matchesPriority =
      priority === "ALL" || lead.priority === priority;

    return matchesSearch && matchesPriority;
  });

  if (loading) {
    return (
      <div className="text-xl font-semibold">
        Loading Leads...
      </div>
    );
  }

  return (
    <div className="space-y-6">

      <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">

        <div>
          <h1 className="text-4xl font-bold">
            Leads
          </h1>

          <p className="text-slate-500">
            Manage and review your qualified leads
          </p>
        </div>

        <div className="flex flex-col gap-3 sm:flex-row">

          <input
            type="text"
            placeholder="Search company or website..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 sm:w-80"
          />

          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
            className="rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-blue-500"
          >
            <option value="ALL">All Priority</option>
            <option value="HIGH">High</option>
            <option value="MEDIUM">Medium</option>
            <option value="LOW">Low</option>
          </select>

        </div>

      </div>

      <div className="overflow-x-auto rounded-2xl border bg-white shadow-md">

        <table className="min-w-full">

          <thead className="bg-slate-100">

            <tr>
              <th className="px-6 py-4 text-left">Company</th>
              <th className="px-6 py-4 text-left">Website</th>
              <th className="px-6 py-4 text-left">Score</th>
              <th className="px-6 py-4 text-left">Priority</th>
              <th className="px-6 py-4 text-left">Status</th>
              <th className="px-6 py-4 text-center">Actions</th>
            </tr>

          </thead>

          <tbody>

            {filteredLeads.length > 0 ? (

              filteredLeads.map((lead, index) => (

                <tr
                  key={index}
                  className="border-t transition hover:bg-slate-50"
                >

                  <td className="px-6 py-4 font-semibold">
                    {lead.company}
                  </td>

                  <td className="px-6 py-4">
                    <a
                      href={lead.website}
                      target="_blank"
                      rel="noreferrer"
                      className="text-blue-600 hover:underline"
                    >
                      {lead.website}
                    </a>
                  </td>

                  <td className="px-6 py-4">
                    <span className="rounded-lg bg-slate-100 px-3 py-1 font-medium">
                      {lead.score}
                    </span>
                  </td>

                  <td className="px-6 py-4">
                    <span
                      className={`rounded-full px-3 py-1 text-sm font-medium ${
                        lead.priority === "HIGH"
                          ? "bg-red-100 text-red-700"
                          : lead.priority === "MEDIUM"
                          ? "bg-yellow-100 text-yellow-700"
                          : "bg-blue-100 text-blue-700"
                      }`}
                    >
                      {lead.priority}
                    </span>
                  </td>

                  <td className="px-6 py-4">
                    <span className="rounded-full bg-green-100 px-3 py-1 text-green-700">
                      {lead.status}
                    </span>
                  </td>

                  <td className="px-6 py-4 text-center">

                    <button
                      onClick={() => openLead(lead)}
                      className="rounded-lg p-2 transition hover:bg-slate-100"
                    >
                      <Eye size={18} />
                    </button>

                  </td>

                </tr>

              ))

            ) : (

              <tr>

                <td
                  colSpan="6"
                  className="py-10 text-center text-slate-500"
                >
                  No leads found.
                </td>

              </tr>

            )}

          </tbody>

        </table>

      </div>

      <LeadDrawer
        lead={selectedLead}
        open={drawerOpen}
        onClose={() => setDrawerOpen(false)}
      />

    </div>
  );
}