import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Leads from "./pages/Leads";
import Scan from "./pages/Scan";
import Sidebar from "./components/Sidebar";

export default function App() {
  return (
    <BrowserRouter>
      <div className="flex h-screen bg-gray-50">

        <Sidebar />

        <main className="flex-1 p-8 overflow-y-auto">

          <div className="bg-white rounded-xl border p-6 min-h-full">

            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/leads" element={<Leads />} />
              <Route path="/scan" element={<Scan />} />
            </Routes>

          </div>

        </main>

      </div>
    </BrowserRouter>
  );
}