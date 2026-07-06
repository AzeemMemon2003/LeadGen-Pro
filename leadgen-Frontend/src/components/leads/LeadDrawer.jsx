import { useEffect, useState } from "react";
import { X, Globe, Mail, Phone, Save } from "lucide-react";
import { updateLeadStatus } from "../../api/leadApi";

export default function LeadDrawer({
  lead,
  open,
  onClose,
  onUpdated,
}) {
  const [status, setStatus] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (lead) {
      setStatus(lead.status);
    }
  }, [lead]);

  if (!open || !lead) return null;

  async function saveStatus() {
    try {
      setSaving(true);

      await updateLeadStatus(lead.id, status);

      if (onUpdated) {
        await onUpdated();
      }

      onClose();
    } catch (err) {
      console.error(err);
      alert("Failed to update lead.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <>
      <div
        onClick={onClose}
        className="fixed inset-0 bg-black/40 backdrop-blur-sm z-40"
      />

      <div className="fixed right-0 top-0 h-screen w-[520px] bg-white shadow-2xl z-50 flex flex-col">

        {/* Header */}

        <div className="border-b p-6">

          <div className="flex justify-between items-start">

            <div>

              <div className="flex items-center gap-3">

                <div className="h-14 w-14 rounded-xl bg-blue-600 text-white flex items-center justify-center text-xl font-bold">

                  {lead.company?.charAt(0)}

                </div>

                <div>

                  <h2 className="text-2xl font-bold">

                    {lead.company}

                  </h2>

                  <a
                    href={lead.website}
                    target="_blank"
                    rel="noreferrer"
                    className="text-blue-600 hover:underline flex items-center gap-1 mt-1"
                  >
                    <Globe size={16} />
                    {lead.website}
                  </a>

                </div>

              </div>

            </div>

            <button
              onClick={onClose}
              className="rounded-lg p-2 hover:bg-slate-100"
            >
              <X size={22} />
            </button>

          </div>

        </div>

        {/* Body */}

        <div className="flex-1 overflow-y-auto p-6 space-y-8">

          {/* Lead Qualification */}

          <div>

            <h3 className="font-semibold mb-3">

              Lead Qualification

            </h3>

            <div className="rounded-xl border p-4">

              <div className="flex justify-between mb-3">

                <span>Lead Score</span>

                <span className="font-bold">

                  {lead.score}/100

                </span>

              </div>

              <div className="h-3 rounded-full bg-slate-200 overflow-hidden">

                <div
                  className="h-full bg-blue-600"
                  style={{ width: `${lead.score}%` }}
                />

              </div>

              <div className="mt-4 flex gap-2">

                <span
                  className={`rounded-full px-3 py-1 text-sm font-semibold ${
                    lead.priority === "HIGH"
                      ? "bg-red-100 text-red-700"
                      : lead.priority === "MEDIUM"
                      ? "bg-yellow-100 text-yellow-700"
                      : "bg-blue-100 text-blue-700"
                  }`}
                >
                  {lead.priority}
                </span>

              </div>

            </div>

          </div>

          {/* Contact */}

          <div>

            <h3 className="font-semibold mb-3">

              Contact

            </h3>

            <div className="rounded-xl border divide-y">

              <Info
                icon={<Mail size={18} />}
                label="Primary Email"
                value={lead.primary_email}
              />

              <Info
                icon={<Phone size={18} />}
                label="Phone"
                value={lead.phone}
              />

              <Info
                icon={<Globe size={18} />}
                label="Website"
                value={lead.website}
              />

            </div>

          </div>

          {/* Technology */}

          <div>

            <h3 className="font-semibold mb-3">

              Technology

            </h3>

            <div className="flex flex-wrap gap-2">

              {lead.technology?.length ? (

                lead.technology.map((tech, index) => (

                  <span
                    key={index}
                    className="rounded-full bg-slate-100 px-3 py-1 text-sm"
                  >
                    {tech}
                  </span>

                ))

              ) : (

                <span className="text-slate-400">

                  No technology detected.

                </span>

              )}

            </div>

          </div>

          {/* Email Verification */}

          <div>

            <h3 className="font-semibold mb-3">

              Email Verification

            </h3>

            <div className="rounded-xl border divide-y">

              <Info
                icon={<Mail size={18} />}
                label="Verification"
                value={
                  lead.email_verified
                    ? "✅ Verified"
                    : "❌ Not Verified"
                }
              />

              <Info
                icon={<Mail size={18} />}
                label="Confidence"
                value={`${lead.email_confidence || 0}%`}
              />

              <Info
                icon={<Mail size={18} />}
                label="Provider"
                value={lead.email_provider || "-"}
              />

              <Info
                icon={<Mail size={18} />}
                label="Role Account"
                value={lead.email_role ? "Yes" : "No"}
              />

              <Info
                icon={<Mail size={18} />}
                label="Disposable"
                value={lead.email_disposable ? "Yes" : "No"}
              />

            </div>

          </div>

          {/* Lead Status */}

          <div>

            <h3 className="font-semibold mb-3">

              Lead Status

            </h3>

            <select
              value={status}
              onChange={(e) => setStatus(e.target.value)}
              className="w-full rounded-xl border p-3"
            >
              <option>Not Contacted</option>
              <option>Contacted</option>
              <option>Qualified</option>
              <option>Proposal Sent</option>
              <option>Closed Won</option>
              <option>Closed Lost</option>
            </select>

          </div>

        </div>

        {/* Footer */}

        <div className="border-t p-6">

          <button
            onClick={saveStatus}
            disabled={saving}
            className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700 disabled:opacity-60 flex justify-center items-center gap-2"
          >
            <Save size={18} />
            {saving ? "Saving..." : "Save Changes"}
          </button>

        </div>

      </div>

    </>
  );
}

function Info({ icon, label, value }) {
  return (
    <div className="flex items-center gap-4 p-4">

      <div className="text-slate-500">

        {icon}

      </div>

      <div>

        <p className="text-xs uppercase text-slate-400">

          {label}

        </p>

        <p className="font-medium break-all">

          {value || "-"}

        </p>

      </div>

    </div>
  );
}