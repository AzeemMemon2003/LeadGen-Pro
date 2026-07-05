import { useState } from "react";
import { scanWebsite } from "../api/leadApi";

export default function Scan() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const handleScan = async () => {
    if (!url) return;

    setLoading(true);
    setError(null);

    try {
      const res = await scanWebsite(url);
      setData(res.data);
    } catch (err) {
      setError("Scan failed. Backend not connected or API error.");
    }

    setLoading(false);
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Website Scanner</h1>

      <div className="flex gap-2 mb-4">
        <input
          className="border p-2 w-full rounded"
          placeholder="Enter website URL (e.g. example.com)"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button
          onClick={handleScan}
          className="bg-black text-white px-4 py-2 rounded"
        >
          {loading ? "Scanning..." : "Scan"}
        </button>
      </div>

      {error && (
        <div className="text-red-500 mb-3">
          {error}
        </div>
      )}

      {data && (
        <div className="bg-gray-100 p-4 rounded">
          <h3 className="font-bold mb-2">Scan Result:</h3>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}