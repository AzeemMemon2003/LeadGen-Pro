import { NavLink } from "react-router-dom";

export default function Sidebar() {
  const linkStyle = ({ isActive }) =>
    `block px-3 py-2 rounded-lg text-sm font-medium transition ${
      isActive ? "bg-black text-white" : "text-gray-600 hover:bg-gray-100"
    }`;

  return (
    <div className="w-64 bg-white border-r p-5">

      <h1 className="text-xl font-bold mb-8">
        LeadGen Pro
      </h1>

      <nav className="space-y-2">
        <NavLink to="/" className={linkStyle}>
          Dashboard
        </NavLink>

        <NavLink to="/leads" className={linkStyle}>
          Leads
        </NavLink>

        <NavLink to="/scan" className={linkStyle}>
          Website Scanner
        </NavLink>
      </nav>

    </div>
  );
}