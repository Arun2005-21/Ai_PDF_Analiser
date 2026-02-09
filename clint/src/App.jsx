import { useState } from "react";
import "./App.css";

function App() {
  const [pdf, setPdf] = useState(null);
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) setPdf(file);
  };

  const fetchApi = async () => {
    if (!pdf) {
      alert("Please select a PDF first!");
      return;
    }

    const formData = new FormData();
    formData.append("pdf", pdf);

    try {
      setLoading(true);
      setSummary("");

      const res = await fetch("http://localhost:5001/api", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (!res.ok) {
        alert(data.error || "Backend error");
        return;
      }

      setSummary(data.message);
    } catch (err) {
      console.log(err);
      alert("Failed to fetch. Backend is not running or crashed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <input type="file" accept="application/pdf" onChange={handleFileUpload} />
      <button onClick={fetchApi} disabled={loading}>
        {loading ? "Generating..." : "Generate AI Summary"}
      </button>

{summary && <pre style={{ whiteSpace: "pre-wrap" }}>{summary}</pre>}
    </>
  );
}

export default App;
