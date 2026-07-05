import { FiBell, FiSearch } from "react-icons/fi";

export default function Topbar() {
  return (
    <header className="sticky top-0 z-30 flex h-16 items-center justify-between border-b border-slate-200 bg-white px-8">

      <div>
        <h1 className="text-2xl font-bold text-slate-800">
          Dashboard
        </h1>

        <p className="text-sm text-slate-500">
          Welcome back, Azeem 👋
        </p>
      </div>

      <div className="flex items-center gap-4">

        <div className="flex items-center rounded-xl border bg-slate-50 px-3 py-2">
          <FiSearch className="mr-2 text-slate-400" />
          <input
            type="text"
            placeholder="Search..."
            className="bg-transparent outline-none"
          />
        </div>

        <button className="rounded-xl border p-3 hover:bg-slate-100">
          <FiBell />
        </button>

        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-600 font-bold text-white">
          A
        </div>

      </div>
    </header>
  );
}