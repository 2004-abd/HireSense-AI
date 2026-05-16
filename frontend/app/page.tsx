import { BarChart3, Brain, BriefcaseBusiness, FileText, History, Lock } from "lucide-react";
import Link from "next/link";

import AppNavbar from "@/components/AppNavbar";

export default function HomePage() {
  return (
    <main className="container">
      <AppNavbar publicMode />

      <section className="hero">
        <div>
          <span className="badge">AI Resume Screening for Multiple Career Fields</span>

          <h1>Analyze resume-job fit with secure AI intelligence.</h1>

          <p>
            HireSense AI compares resumes with job descriptions, predicts fit
            quality, extracts matched and missing skills, accepts PDF/DOCX
            resumes, and stores every analysis securely in MongoDB.
          </p>

          <div className="nav-links" style={{ marginTop: 26 }}>
            <Link className="btn btn-primary" href="/register">
              Start Free Analysis
            </Link>

            <Link className="btn" href="/about">
              View AI Pipeline
            </Link>
          </div>
        </div>

        <div className="hero-card">
          <span className="badge">What the AI analyzes</span>

          <h2>Resume Fit Intelligence</h2>

          <div className="mock-card">
            <p>
              The system checks skill alignment, text similarity, model
              confidence, and missing job requirements.
            </p>

            <div className="progress">
              <span style={{ width: "82%" }} />
            </div>

            <div className="grid-3">
              <div className="metric">
                <span>Fit</span>
                <b>Role Based</b>
              </div>

              <div className="metric">
                <span>Skills</span>
                <b>Broad</b>
              </div>

              <div className="metric">
                <span>Data</span>
                <b>10k+</b>
              </div>
            </div>

            <div className="chip-row">
              <span className="chip">Technology</span>
              <span className="chip">Business</span>
              <span className="chip">Design</span>
              <span className="chip">Marketing</span>
              <span className="chip">Finance</span>
              <span className="chip">Healthcare</span>
              <span className="chip">Education</span>
            </div>
          </div>
        </div>
      </section>

      <section className="grid-3 section">
        <div className="card">
          <Brain />
          <h2>NLP Model</h2>
          <p>
            TF-IDF feature engineering and logistic regression classify Strong,
            Moderate, or Weak Fit.
          </p>
        </div>

        <div className="card">
          <FileText />
          <h2>PDF/DOCX Upload</h2>
          <p>
            Upload a resume file or paste text manually. Only PDF and DOCX
            formats are allowed.
          </p>
        </div>

        <div className="card">
          <BriefcaseBusiness />
          <h2>Broad Skill Coverage</h2>
          <p>
            Designed for tech, business, finance, marketing, HR, design,
            healthcare, education, and operations roles.
          </p>
        </div>
      </section>

      <section className="grid-3 section">
        <div className="card">
          <Lock />
          <h2>Secure Gateway</h2>
          <p>
            Registration, password hashing, OAuth2 login, and JWT protected AI
            routes.
          </p>
        </div>

        <div className="card">
          <History />
          <h2>History Tracking</h2>
          <p>
            Every analysis is saved in MongoDB so users can review previous
            results.
          </p>
        </div>

        <div className="card">
          <BarChart3 />
          <h2>Visual Analytics</h2>
          <p>
            Model metrics and analysis charts give a professional dashboard
            experience.
          </p>
        </div>
      </section>

      <section className="card section">
        <span className="badge">How it works</span>
        <h2>End-to-end AI Workflow</h2>
        <p>
          The backend gathers a structured training dataset, cleans text,
          transforms resume-job pairs with TF-IDF, trains a classification
          model, calculates validation metrics, and exposes secure FastAPI
          endpoints for the React dashboard.
        </p>
      </section>

      <footer className="footer">
        HireSense AI — Next.js, FastAPI, MongoDB, JWT, PDF/DOCX parsing, and
        Machine Learning
      </footer>
    </main>
  );
}
