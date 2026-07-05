import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Leads from "./pages/Leads";
import Scan from "./pages/Scan";

import Sidebar from "./components/layout/Sidebar";
import Topbar from "./components/layout/Topbar";

export default function App() {
  return (
    <BrowserRouter>

      <Sidebar />

      <div className="ml-64 min-h-screen bg-slate-100">

        <Topbar />

        <main className="p-8">

          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/leads" element={<Leads />} />
            <Route path="/scan" element={<Scan />} />
          </Routes>

        </main>

      </div>

    </BrowserRouter>
  );
}