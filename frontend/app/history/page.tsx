"use client";

import { useEffect, useState } from "react";

import AppNavbar from "@/components/AppNavbar";
import { API_URL, getErrorMessage, getToken } from "@/lib/api";

type HistoryItem = {
  source: string;
  resume_preview: string;
  job_preview: string;
  created_at: string;
  result: {
    fit_category: string;
    fit_score: number;
    confidence: number;
    skill_match_rate: number;
    matched_skills: string[];
    missing_skills: string[];
  };
};

export default function HistoryPage() {
  const [history, setHistory] = useState<HistoryItem[]>([]);
  const [error, setError] = useState("");
  const [authChecked, setAuthChecked] = useState(false);

  useEffect(() => {
    async function loadHistory() {
      const token = getToken();

      if (!token) {
        window.location.replace("/login");
        return;
      }

      setAuthChecked(true);

      try {
        const res = await fetch(`${API_URL}/analysis/history`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        const data = await res.json();

        if (!res.ok) {
          setError(getErrorMessage(data, "Could not load history."));
          return;
        }

        setHistory(data);
      } catch {
        setError("Backend is not reachable.");
      }
    }

    loadHistory();
  }, []);

  if (!authChecked) {
    return (
      <main className="auth-wrap">
        <div className="card auth-card">
          <span className="badge">Checking secure access</span>
          <h2>Loading history...</h2>
        </div>
      </main>
    );
  }

  return (
    <main className="container dashboard">
      <AppNavbar />

      <section className="card">
        <span className="badge">MongoDB Analysis History</span>

        <h1 style={{ fontSize: 46 }}>Previous Resume Analyses</h1>

        <p>
          Review recent AI predictions saved securely in MongoDB for your
          account.
        </p>
      </section>

      <section className="card" style={{ marginTop: 18 }}>
        {error && <p className="error">{error}</p>}

        {!error && history.length === 0 && <p>No analysis history found yet.</p>}

        {history.map((item, index) => {
          const skillMatch =
            typeof item.result?.skill_match_rate === "number"
              ? item.result.skill_match_rate
              : 0;

          const score =
            typeof item.result?.fit_score === "number"
              ? item.result.fit_score
              : 0;

          return (
            <div className="history-item" key={`${item.created_at}-${index}`}>
              <div>
                <span className="badge">
                  {item.source === "file" ? "File Upload" : "Text Input"}
                </span>

                <p>{new Date(item.created_at).toLocaleString()}</p>
              </div>

              <div>
                <h3 style={{ marginTop: 0 }}>
                  {item.result.fit_category} — {score.toFixed(2)}%
                </h3>

                <p>
                  <b>Resume:</b> {item.resume_preview}
                </p>

                <p>
                  <b>Job:</b> {item.job_preview}
                </p>

                <div className="chip-row">
                  {(item.result.matched_skills || []).slice(0, 10).map((skill) => (
                    <span className="chip" key={skill}>
                      {skill}
                    </span>
                  ))}
                </div>

                {(item.result.missing_skills || []).length > 0 && (
                  <>
                    <h3>Missing Skills</h3>

                    <div className="chip-row">
                      {item.result.missing_skills
                        .slice(0, 10)
                        .map((skill) => (
                          <span className="chip" key={skill}>
                            {skill}
                          </span>
                        ))}
                    </div>
                  </>
                )}
              </div>

              <div className="metric">
                <span>Skill Match</span>
                <b>{skillMatch.toFixed(0)}%</b>
              </div>
            </div>
          );
        })}
      </section>
    </main>
  );
}
