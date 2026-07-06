import { useEffect, useState } from "react";
import {
  scanWebsite,
  getScanStatus,
} from "../api/leadApi";

export default function Scan() {
  const [url, setUrl] = useState("");

  const [loading, setLoading] = useState(false);

  const [data, setData] = useState(null);

  const [error, setError] = useState(null);

  const [progress, setProgress] = useState({
    running: false,
    total: 0,
    current: 0,
    success: 0,
    failed: 0,
    current_website: "",
  });

  useEffect(() => {
    let timer;

    if (progress.running) {
      timer = setInterval(async () => {
        try {
          const status = await getScanStatus();

          setProgress(status);

          if (!status.running) {
            clearInterval(timer);
          }
        } catch (e) {
          console.error(e);
        }
      }, 1000);
    }

    return () => clearInterval(timer);

  }, [progress.running]);

  const handleScan = async () => {

    if (!url.trim()) {
      setError("Please enter a website URL.");
      return;
    }

    setLoading(true);
    setError(null);
    setData(null);

    try {

      const result = await scanWebsite(url);

      setData(result);

      setProgress({
        running: true,
        total: result.total,
        current: 0,
        success: 0,
        failed: 0,
        current_website: "",
      });

      setUrl("");

    } catch (err) {

      console.error(err);

      setError(
        err?.response?.data?.message ||
        "Scan failed."
      );

    } finally {

      setLoading(false);

    }
  };

  const percent =
    progress.total > 0
      ? (progress.current / progress.total) * 100
      : 0;

  return (
    <div className="max-w-4xl">

      <h1 className="text-2xl font-bold mb-6">
        Website Scanner
      </h1>

      <div className="flex gap-3 mb-6">

        <input
          type="text"
          className="border rounded p-3 flex-1"
          placeholder="Enter website URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button
          onClick={handleScan}
          disabled={loading || progress.running}
          className={`px-6 py-3 rounded text-white ${
            loading || progress.running
              ? "bg-gray-500"
              : "bg-black hover:bg-gray-800"
          }`}
        >
          {progress.running ? "Scanning..." : "Scan"}
        </button>

      </div>

      {error && (

        <div className="mb-4 p-3 rounded bg-red-100 text-red-700">

          {error}

        </div>

      )}

      {data && (

        <div className="mb-6 p-4 rounded bg-green-100">

          <strong>{data.message}</strong>

        </div>

      )}

      {progress.total > 0 && (

        <div className="border rounded p-5">

          <h2 className="font-bold text-lg mb-4">

            Live Scan Progress

          </h2>

          <div className="w-full bg-gray-200 rounded h-4 mb-4">

            <div
              className="bg-green-600 h-4 rounded transition-all"
              style={{
                width: `${percent}%`,
              }}
            />

          </div>

          <p className="mb-2">
            <strong>Current Website:</strong>{" "}
            {progress.current_website || "-"}
          </p>

          <p>
            <strong>Progress:</strong>{" "}
            {progress.current} / {progress.total}
          </p>

          <p>
            <strong>Success:</strong>{" "}
            {progress.success}
          </p>

          <p>
            <strong>Failed:</strong>{" "}
            {progress.failed}
          </p>

          {!progress.running &&
            progress.total > 0 && (

              <div className="mt-4 p-3 rounded bg-green-50 border border-green-300">

                ✅ Scan Complete

              </div>

            )}

        </div>

      )}

    </div>
  );
}