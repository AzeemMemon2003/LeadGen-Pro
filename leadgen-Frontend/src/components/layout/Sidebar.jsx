import { NavLink } from "react-router-dom";
import {
  FiHome,
  FiUsers,
  FiSearch,
  FiSettings,
} from "react-icons/fi";

const menu = [
  {
    name: "Dashboard",
    icon: <FiHome size={20} />,
    path: "/",
  },
  {
    name: "Leads",
    icon: <FiUsers size={20} />,
    path: "/leads",
  },
  {
    name: "Scanner",
    icon: <FiSearch size={20} />,
    path: "/scan",
  },
];

export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-screen w-64 bg-slate-900 text-white flex flex-col shadow-xl">

      {/* Logo */}

      <div className="border-b border-slate-800 px-6 py-6">

        <h1 className="text-2xl font-bold text-blue-400">
          LeadGen Pro
        </h1>

        <p className="text-sm text-slate-400">
          AI CRM
        </p>

      </div>

      {/* Navigation */}

      <nav className="flex-1 px-4 py-6">

        {menu.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `mb-2 flex items-center gap-3 rounded-xl px-4 py-3 transition-all ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-slate-300 hover:bg-slate-800"
              }`
            }
          >
            {item.icon}

            <span>{item.name}</span>

          </NavLink>
        ))}

      </nav>

      {/* Footer */}

      <div className="border-t border-slate-800 p-4">

        <button className="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-slate-300 hover:bg-slate-800">

          <FiSettings size={20} />

          Settings

        </button>

      </div>

    </aside>
  );
}