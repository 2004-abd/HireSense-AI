"use client";

import {
  Brain,
  Database,
  FileText,
  Lock,
  Server,
  Workflow,
} from "lucide-react";

import AppNavbar from "@/components/AppNavbar";

export default function AboutPage() {
  return (
    <main className="container">
      <AppNavbar />

      <section className="card">
        <span className="badge">Project Documentation</span>

        <h1 style={{ fontSize: 54 }}>AI Resume & Job Fit Analyzer</h1>

        <p>
          HireSense AI is a full-stack machine learning web application built
          with Next.js, FastAPI, MongoDB, JWT authentication, PDF/DOCX parsing,
          and an end-to-end NLP model pipeline.
        </p>
      </section>

      <section className="grid-3 section">
        <div className="card">
          <Server />
          <h2>Frontend</h2>
          <p>
            Next.js interface with landing page, authentication pages, protected
            dashboard, model metrics, resume analysis, and history tracking.
          </p>
        </div>

        <div className="card">
          <Lock />
          <h2>Security</h2>
          <p>
            Password hashing, OAuth2 login route, JWT tokens, protected API
            endpoints, and secure user-specific analysis history.
          </p>
        </div>

        <div className="card">
          <Database />
          <h2>MongoDB</h2>
          <p>
            Stores registered users, analysis results, system logs, model
            metrics, and previous resume-job fit history.
          </p>
        </div>
      </section>

      <section className="card section">
        <span className="badge">AI Lifecycle</span>

        <h2>Backend Machine Learning Pipeline</h2>

        <div className="grid-3" style={{ marginTop: 18 }}>
          <div className="metric">
            <Workflow />
            <h3>1. Data Gathering</h3>
            <p>
              The system uses a structured dataset with 10,000+ resume-job
              examples across technology, business, marketing, finance,
              healthcare, education, HR, design, operations, and support roles.
            </p>
          </div>

          <div className="metric">
            <FileText />
            <h3>2. Data Cleaning</h3>
            <p>
              The training pipeline removes missing values, duplicate rows,
              short text samples, and formatting noise before model training.
            </p>
          </div>

          <div className="metric">
            <Brain />
            <h3>3. Feature Engineering</h3>
            <p>
              Resume text and job descriptions are transformed into numerical
              features using TF-IDF vectorization.
            </p>
          </div>

          <div className="metric">
            <Brain />
            <h3>4. Model Training</h3>
            <p>
              Logistic Regression is trained to classify resume-job pairs into
              Strong Fit, Moderate Fit, or Weak Fit.
            </p>
          </div>

          <div className="metric">
            <Database />
            <h3>5. Metrics</h3>
            <p>
              Accuracy, precision, recall, F1-score, and confusion matrix are
              calculated and displayed inside the secure dashboard.
            </p>
          </div>

          <div className="metric">
            <Lock />
            <h3>6. Protected API</h3>
            <p>
              Only authenticated users can analyze resumes, upload files, view
              history, or access model performance metrics.
            </p>
          </div>
        </div>
      </section>

      <section className="grid-3 section">
        <div className="card">
          <h2>Resume Input</h2>
          <p>
            Users can either paste resume text manually or upload a resume file
            in PDF/DOCX format.
          </p>
        </div>

        <div className="card">
          <h2>Skill Gap Analysis</h2>
          <p>
            The AI extracts matched skills, missing skills, skill match
            percentage, confidence score, and improvement suggestions.
          </p>
        </div>

        <div className="card">
          <h2>History Tracking</h2>
          <p>
            Every resume analysis is saved in MongoDB and can be reviewed later
            from the History page.
          </p>
        </div>
      </section>

      <footer className="footer">
        Built for AI project requirements using Next.js, FastAPI, MongoDB, JWT,
        PDF/DOCX parsing, and machine learning.
      </footer>
    </main>
  );
}
