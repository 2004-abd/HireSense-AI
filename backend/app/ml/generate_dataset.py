from pathlib import Path
import csv
import random

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "resume_job_fit_dataset.csv"

ROLE_BANK = {
    "backend": {
        "skills": ["python", "fastapi", "django", "flask", "mongodb", "postgresql", "mysql", "docker", "jwt", "oauth2", "rest api", "testing", "git", "redis", "microservices", "linux"],
        "titles": ["Backend Developer", "Python API Engineer", "Server Side Engineer", "Backend Software Engineer"],
        "tasks": ["build secure REST APIs", "design database schemas", "implement authentication", "write automated tests", "deploy backend services"],
    },
    "frontend": {
        "skills": ["react", "next.js", "typescript", "javascript", "tailwind", "html", "css", "ui ux", "recharts", "api integration", "responsive design", "git"],
        "titles": ["Frontend Developer", "React Developer", "Next.js Engineer", "UI Engineer"],
        "tasks": ["build responsive interfaces", "create reusable components", "integrate APIs", "develop dashboards", "implement form validation"],
    },
    "data_ai": {
        "skills": ["python", "pandas", "numpy", "scikit-learn", "machine learning", "nlp", "data analysis", "data cleaning", "data visualization", "statistics", "model evaluation", "classification"],
        "titles": ["Data Scientist", "Machine Learning Engineer", "Data Analyst", "AI Engineer"],
        "tasks": ["clean datasets", "train machine learning models", "evaluate metrics", "build dashboards", "perform NLP analysis"],
    },
    "devops": {
        "skills": ["aws", "azure", "docker", "kubernetes", "linux", "ci cd", "github actions", "cloud", "monitoring", "terraform", "deployment", "networking"],
        "titles": ["DevOps Engineer", "Cloud Engineer", "Infrastructure Engineer", "Platform Engineer"],
        "tasks": ["deploy cloud infrastructure", "maintain CI CD pipelines", "monitor services", "manage containers", "automate deployments"],
    },
    "cybersecurity": {
        "skills": ["cybersecurity", "linux", "networking", "python", "incident response", "threat monitoring", "security reporting", "risk analysis", "vulnerability assessment", "siem", "firewall"],
        "titles": ["Cybersecurity Analyst", "Security Engineer", "SOC Analyst", "Information Security Analyst"],
        "tasks": ["monitor security alerts", "investigate incidents", "assess vulnerabilities", "write security reports", "analyze risks"],
    },
    "mobile": {
        "skills": ["flutter", "firebase", "dart", "ui ux", "api integration", "git", "mobile app", "android", "ios", "authentication", "responsive layout"],
        "titles": ["Mobile App Developer", "Flutter Developer", "Mobile Engineer"],
        "tasks": ["build mobile screens", "integrate Firebase", "connect APIs", "implement authentication", "prepare app releases"],
    },
    "design": {
        "skills": ["figma", "photoshop", "illustrator", "ui ux", "user research", "wireframes", "prototyping", "design systems", "usability testing", "branding", "accessibility"],
        "titles": ["UI UX Designer", "Product Designer", "UX Researcher", "Visual Designer"],
        "tasks": ["create wireframes", "build prototypes", "conduct user research", "design user flows", "maintain design systems"],
    },
    "marketing": {
        "skills": ["digital marketing", "seo", "sem", "google ads", "facebook ads", "social media marketing", "content marketing", "copywriting", "email marketing", "crm", "analytics", "campaign management"],
        "titles": ["Digital Marketing Specialist", "SEO Specialist", "Content Marketer", "Marketing Analyst"],
        "tasks": ["manage campaigns", "improve search rankings", "write content", "analyze marketing metrics", "generate leads"],
    },
    "finance": {
        "skills": ["financial analysis", "accounting", "bookkeeping", "excel", "quickbooks", "xero", "budgeting", "financial modeling", "forecasting", "risk management", "reporting"],
        "titles": ["Financial Analyst", "Accountant", "Bookkeeper", "Finance Assistant"],
        "tasks": ["prepare financial reports", "analyze budgets", "manage accounts", "forecast revenue", "track expenses"],
    },
    "business": {
        "skills": ["business analysis", "project management", "agile", "scrum", "jira", "kpi analysis", "process improvement", "documentation", "presentation", "stakeholder management", "operations management"],
        "titles": ["Business Analyst", "Project Manager", "Operations Analyst", "Product Manager"],
        "tasks": ["gather requirements", "manage projects", "analyze KPIs", "improve processes", "prepare stakeholder reports"],
    },
    "sales_support": {
        "skills": ["customer service", "sales", "negotiation", "crm", "communication", "lead generation", "hubspot", "salesforce", "problem solving", "customer support", "email handling"],
        "titles": ["Sales Executive", "Customer Support Specialist", "Account Executive", "Client Success Associate"],
        "tasks": ["support customers", "manage CRM records", "generate leads", "resolve complaints", "close sales deals"],
    },
    "hr": {
        "skills": ["recruitment", "hr management", "employee relations", "payroll", "onboarding", "training", "communication", "documentation", "policy writing", "interviews"],
        "titles": ["HR Assistant", "Recruiter", "HR Coordinator", "Talent Acquisition Specialist"],
        "tasks": ["screen candidates", "schedule interviews", "manage employee records", "support onboarding", "prepare HR documents"],
    },
    "education": {
        "skills": ["teaching", "lesson planning", "curriculum development", "training", "coaching", "communication", "assessment", "research", "presentation", "classroom management"],
        "titles": ["Teacher", "Trainer", "Education Coordinator", "Curriculum Developer"],
        "tasks": ["prepare lessons", "teach students", "assess learning", "develop curriculum", "coach learners"],
    },
    "healthcare": {
        "skills": ["patient care", "medical records", "clinical documentation", "healthcare management", "communication", "attention to detail", "teamwork", "compliance", "scheduling"],
        "titles": ["Healthcare Assistant", "Medical Receptionist", "Clinical Coordinator", "Patient Support Specialist"],
        "tasks": ["support patient care", "manage medical records", "coordinate appointments", "document clinical information", "follow compliance rules"],
    },
}

UNRELATED_PROFILES = [
    ("Restaurant Manager", ["customer service", "inventory management", "staff scheduling", "cash handling", "operations management", "leadership"]),
    ("Graphic Designer", ["photoshop", "canva", "branding", "poster design", "social media", "visual design"]),
    ("Data Entry Operator", ["typing", "excel", "email handling", "admin support", "documentation", "file management"]),
    ("Retail Sales Associate", ["sales", "customer service", "cashier", "product knowledge", "communication"]),
    ("Content Writer", ["copywriting", "seo", "wordpress", "research", "editing", "blog writing"]),
    ("Warehouse Assistant", ["inventory management", "logistics", "packing", "operations", "teamwork"]),
    ("Receptionist", ["communication", "scheduling", "customer service", "admin support", "phone handling"]),
]

LEVELS = ["Junior", "Associate", "Mid-level", "Experienced", "Senior"]
DOMAINS = ["fintech", "healthcare", "education", "ecommerce", "logistics", "banking", "retail", "SaaS", "real estate", "telecom", "hospitality"]
IMPACTS = ["improved workflow efficiency", "reduced manual work", "delivered measurable results", "worked with cross-functional teams", "created reports", "solved practical problems", "managed deadlines"]


def pick(items, min_count, max_count):
    count = random.randint(min_count, min(max_count, len(items)))
    return random.sample(items, count)


def make_job(role_key):
    spec = ROLE_BANK[role_key]
    title = random.choice(spec["titles"])
    domain = random.choice(DOMAINS)
    skills = pick(spec["skills"], 7, 12)
    tasks = pick(spec["tasks"], 3, 5)
    return (
        f"We are hiring a {title} for a {domain} organization. "
        f"The candidate should be able to {', '.join(tasks)}. "
        f"Required skills include {', '.join(skills)}."
    )


def make_strong_resume(role_key):
    spec = ROLE_BANK[role_key]
    title = random.choice(spec["titles"])
    skills = pick(spec["skills"], 9, 14)
    tasks = pick(spec["tasks"], 4, 5)
    impacts = pick(IMPACTS, 2, 4)
    return (
        f"{random.choice(LEVELS)} {title} with strong experience in {', '.join(skills)}. "
        f"I have handled responsibilities such as {', '.join(tasks)}. "
        f"My work {', '.join(impacts)}."
    )


def make_moderate_resume(role_key):
    spec = ROLE_BANK[role_key]
    other_key = random.choice([k for k in ROLE_BANK if k != role_key])
    other = ROLE_BANK[other_key]
    skills = list(dict.fromkeys(pick(spec["skills"], 3, 6) + pick(other["skills"], 4, 7)))
    title = random.choice(other["titles"])
    tasks = pick(other["tasks"], 2, 4)
    return (
        f"{random.choice(LEVELS)} {title} with transferable experience in {', '.join(skills)}. "
        f"I have worked on tasks such as {', '.join(tasks)} and I am improving job-specific skills."
    )


def make_weak_resume():
    title, skills_base = random.choice(UNRELATED_PROFILES)
    skills = pick(skills_base, 4, 6)
    return (
        f"{random.choice(LEVELS)} {title} with experience in {', '.join(skills)}. "
        f"I handled daily work responsibilities, supported teams, communicated with people, and completed assigned tasks."
    )


def main():
    random.seed(2026)
    rows = []

    # 14 roles * 240 examples * 3 labels = 10080 rows
    per_role_per_label = 240

    for role_key in ROLE_BANK:
        for _ in range(per_role_per_label):
            rows.append([make_strong_resume(role_key), make_job(role_key), "Strong Fit"])
        for _ in range(per_role_per_label):
            rows.append([make_moderate_resume(role_key), make_job(role_key), "Moderate Fit"])
        for _ in range(per_role_per_label):
            rows.append([make_weak_resume(), make_job(role_key), "Weak Fit"])

    random.shuffle(rows)
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    with DATA_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["resume_text", "job_description", "match_category"])
        writer.writerows(rows)

    print(f"Dataset generated successfully: {DATA_PATH}")
    print(f"Total rows: {len(rows)}")


if __name__ == "__main__":
    main()
