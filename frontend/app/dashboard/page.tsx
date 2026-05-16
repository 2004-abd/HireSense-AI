"use client";

import { useEffect, useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import AppNavbar from "@/components/AppNavbar";
import { API_URL, getErrorMessage, getToken, getUserName } from "@/lib/api";

type Result = {
  fit_category: string;
  fit_score: number;
  confidence: number;
  skill_match_rate: number;
  matched_skills: string[];
  missing_skills: string[];
  suggestions: string[];
};

export default function DashboardPage() {
  const [authChecked, setAuthChecked] = useState(false);
  const [mode, setMode] = useState<"text" | "file">("text");
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [userName, setUserName] = useState("");

  useEffect(() => {
    const token = getToken();

    if (!token) {
      window.location.replace("/login");
      return;
    }

    setUserName(getUserName());
    setAuthChecked(true);
  }, []);

  if (!authChecked) {
    return (
      <main className="auth-wrap">
        <div className="card auth-card">
          <span className="badge">Checking secure access</span>
          <h2>Loading dashboard...</h2>
          <p>Please login first if you are not redirected automatically.</p>
        </div>
      </main>
    );
  }

  const chartData = result
    ? [
        { name: "Fit Score", value: result.fit_score },
        { name: "Confidence", value: result.confidence },
        { name: "Skill Match", value: result.skill_match_rate },
      ]
    : [];

  async function analyze() {
    setError("");
    setResult(null);

    if (!jobDescription.trim() || jobDescription.trim().length < 30) {
      setError("Job description must be at least 30 characters.");
      return;
    }

    if (mode === "text" && resumeText.trim().length < 50) {
      setError("Resume text must be at least 50 characters.");
      return;
    }

    if (mode === "file") {
      if (!resumeFile) {
        setError("Please upload a resume file.");
        return;
      }

      const allowed = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
      ];

      if (!allowed.includes(resumeFile.type)) {
        setError("Only PDF and DOCX resume files are allowed.");
        return;
      }
    }

    setLoading(true);

    try {
      let res: Response;

      if (mode === "text") {
        res = await fetch(`${API_URL}/analysis/resume-fit`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${getToken()}`,
          },
          body: JSON.stringify({
            resume_text: resumeText,
            job_description: jobDescription,
          }),
        });
      } else {
        const formData = new FormData();
        formData.append("resume_file", resumeFile as File);
        formData.append("job_description", jobDescription);

        res = await fetch(`${API_URL}/analysis/resume-fit-file`, {
          method: "POST",
          headers: {
            Authorization: `Bearer ${getToken()}`,
          },
          body: formData,
        });
      }

      const data = await res.json();

      if (!res.ok) {
        setError(getErrorMessage(data, "Analysis failed."));
        setLoading(false);
        return;
      }

      setResult(data);
    } catch {
      setError("Backend is not reachable or analysis failed.");
    }

    setLoading(false);
  }

  return (
    <main className="container dashboard">
      <AppNavbar />

      <section className="card">
        <span className="badge">Protected AI Workspace</span>

        <h1 style={{ fontSize: 48 }}>Resume & Job Fit Analyzer</h1>

        <p>
          Welcome {userName || "User"}. Analyze resumes for any role using text
          input or PDF/DOCX upload. The system extracts broad skills, predicts
          fit quality, shows charts, and stores history in MongoDB.
        </p>
      </section>

      <section className="workspace" style={{ marginTop: 18 }}>
        <div className="card">
          <div className="tab-row">
            <button
              className={`tab ${mode === "text" ? "active" : ""}`}
              onClick={() => setMode("text")}
            >
              Paste Resume
            </button>

            <button
              className={`tab ${mode === "file" ? "active" : ""}`}
              onClick={() => setMode("file")}
            >
              Upload PDF/DOCX
            </button>
          </div>

          {mode === "text" ? (
            <>
              <label>Resume Text</label>
              <textarea
                placeholder="Paste resume text here..."
                value={resumeText}
                onChange={(e) => setResumeText(e.target.value)}
              />
            </>
          ) : (
            <div className="file-box">
              <label>Resume File</label>
              <input
                className="input"
                type="file"
                accept=".pdf,.docx,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                onChange={(e) => setResumeFile(e.target.files?.[0] || null)}
              />
              <p>Only PDF and DOCX files are accepted.</p>
            </div>
          )}

          <label>Job Description</label>
          <textarea
            placeholder="Paste job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />

          <button className="btn btn-primary" onClick={analyze} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>

          {error && <p className="error">{error}</p>}
        </div>

        <div className="card">
          <h2>AI Result</h2>

          {!result && (
            <p>
              Your analysis result will appear here with charts, skill gaps, and
              suggestions.
            </p>
          )}

          {result && (
            <>
              <div className="result-grid">
                <div className="metric">
                  <span>Fit</span>
                  <b>{result.fit_category}</b>
                </div>

                <div className="metric">
                  <span>Score</span>
                  <b>{result.fit_score}%</b>
                </div>

                <div className="metric">
                  <span>Skills</span>
                  <b>{result.skill_match_rate}%</b>
                </div>
              </div>

              <div style={{ height: 250, marginTop: 24 }}>
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={chartData}>
                    <defs>
                      <linearGradient
                        id="analysisGradient"
                        x1="0"
                        y1="0"
                        x2="0"
                        y2="1"
                      >
                        <stop offset="0%" stopColor="#60a5fa" />
                        <stop offset="100%" stopColor="#8b5cf6" />
                      </linearGradient>
                    </defs>

                    <CartesianGrid
                      strokeDasharray="4 4"
                      stroke="rgba(255,255,255,0.08)"
                      vertical={false}
                    />

                    <XAxis
                      dataKey="name"
                      tick={{ fill: "#aab8cc", fontSize: 12 }}
                    />

                    <YAxis
                      domain={[0, 100]}
                      tick={{ fill: "#aab8cc", fontSize: 12 }}
                      tickFormatter={(value) => `${value}%`}
                    />

                    <Tooltip
                      cursor={false}
                      contentStyle={{
                        background: "rgba(15,23,42,0.96)",
                        border: "1px solid rgba(255,255,255,0.12)",
                        borderRadius: "14px",
                        color: "#eef5ff",
                      }}
                    />

                    <Bar
                      dataKey="value"
                      fill="url(#analysisGradient)"
                      radius={[10, 10, 0, 0]}
                      barSize={42}
                      activeBar={false}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </div>

              <h3>Matched Skills</h3>
              <div className="chip-row">
                {result.matched_skills.length ? (
                  result.matched_skills.map((skill) => (
                    <span className="chip" key={skill}>
                      {skill}
                    </span>
                  ))
                ) : (
                  <p>No matched skills found.</p>
                )}
              </div>

              <h3>Missing Skills</h3>
              <div className="chip-row">
                {result.missing_skills.length ? (
                  result.missing_skills.map((skill) => (
                    <span className="chip" key={skill}>
                      {skill}
                    </span>
                  ))
                ) : (
                  <p>No major missing skills found.</p>
                )}
              </div>

              <h3>Suggestions</h3>
              {result.suggestions.map((suggestion, index) => (
                <p key={index}>• {suggestion}</p>
              ))}
            </>
          )}
        </div>
      </section>
    </main>
  );
}
