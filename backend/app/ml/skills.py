# A broad skill dictionary for a general resume-job fit analyzer.
# This is not limited to software jobs. It covers technology, business,
# design, marketing, finance, healthcare, education, operations, and soft skills.

TECH_SKILLS = [
    # Programming / Software
    "python", "java", "javascript", "typescript", "c++", "c#", "php", "ruby", "go",
    "rust", "swift", "kotlin", "dart", "scala", "r", "matlab", "sql", "html", "css",
    "bash", "powershell", "shell scripting", "oop", "data structures", "algorithms",

    # Web / Backend / Frontend
    "react", "next.js", "vue", "angular", "svelte", "node.js", "express", "nestjs",
    "fastapi", "django", "flask", "spring boot", "laravel", "asp.net", "rest api",
    "graphql", "api integration", "microservices", "websocket", "jwt", "oauth2",
    "authentication", "authorization", "responsive design", "tailwind", "bootstrap",
    "material ui", "redux", "zustand", "recharts", "chart.js",

    # Databases
    "mongodb", "mysql", "postgresql", "sqlite", "oracle", "sql server", "redis",
    "elasticsearch", "dynamodb", "firebase", "supabase", "database design",
    "data modeling", "query optimization", "etl", "data warehouse",

    # DevOps / Cloud
    "docker", "kubernetes", "aws", "azure", "gcp", "cloud", "linux", "nginx",
    "apache", "ci cd", "github actions", "gitlab ci", "jenkins", "terraform",
    "ansible", "monitoring", "prometheus", "grafana", "deployment", "serverless",
    "lambda", "load balancing", "infrastructure", "networking", "containers",

    # AI / Data
    "machine learning", "deep learning", "nlp", "computer vision", "data science",
    "data analysis", "data cleaning", "data visualization", "feature engineering",
    "model evaluation", "classification", "regression", "clustering", "recommendation system",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "keras", "opencv",
    "hugging face", "transformers", "llm", "prompt engineering", "statistics",
    "probability", "a/b testing", "power bi", "tableau", "excel", "google sheets",

    # Cybersecurity
    "cybersecurity", "information security", "network security", "incident response",
    "threat monitoring", "vulnerability assessment", "penetration testing", "siem",
    "firewall", "risk analysis", "access control", "security reporting", "owasp",
    "encryption", "malware analysis", "soc", "compliance",

    # Design / Product
    "figma", "adobe xd", "photoshop", "illustrator", "canva", "ui ux", "user research",
    "wireframes", "prototyping", "design systems", "usability testing", "visual design",
    "branding", "typography", "accessibility", "user flows", "product design",
    "product management", "roadmapping", "agile", "scrum", "jira", "trello",

    # Marketing / Sales
    "digital marketing", "seo", "sem", "google ads", "facebook ads", "social media marketing",
    "content marketing", "copywriting", "email marketing", "crm", "salesforce",
    "hubspot", "lead generation", "sales", "negotiation", "market research",
    "brand strategy", "campaign management", "analytics", "conversion optimization",

    # Business / Finance / Admin
    "business analysis", "business reporting", "kpi analysis", "forecasting",
    "financial analysis", "accounting", "bookkeeping", "quickbooks", "xero",
    "budgeting", "financial modeling", "investment analysis", "risk management",
    "project management", "operations management", "process improvement",
    "supply chain", "inventory management", "procurement", "logistics",
    "customer service", "data entry", "admin support", "documentation",
    "presentation", "microsoft office", "word", "powerpoint",

    # Healthcare / Education / HR / Legal
    "patient care", "medical records", "clinical documentation", "healthcare management",
    "teaching", "lesson planning", "curriculum development", "training", "coaching",
    "recruitment", "hr management", "employee relations", "payroll", "onboarding",
    "legal research", "contract drafting", "compliance", "policy writing",

    # Soft Skills
    "communication", "leadership", "teamwork", "problem solving", "critical thinking",
    "time management", "adaptability", "creativity", "attention to detail",
    "decision making", "collaboration", "conflict resolution", "public speaking",
    "research", "writing", "report writing", "analytical thinking"
]


def normalize_skill_name(skill: str) -> str:
    aliases = {
        "api": "rest api",
        "nextjs": "next.js",
        "node": "node.js",
        "sklearn": "scikit-learn",
        "cicd": "ci cd",
        "ui/ux": "ui ux",
        "ms office": "microsoft office",
    }
    skill = skill.lower().strip()
    return aliases.get(skill, skill)


def extract_skills(text: str) -> set[str]:
    normalized = " " + text.lower().replace("/", " ").replace("-", " ").replace(",", " ") + " "
    found = set()

    for skill in TECH_SKILLS:
        lookup = skill.lower().replace("-", " ")
        if lookup in normalized:
            found.add(normalize_skill_name(skill))

    return found


def build_suggestions(missing_skills: list[str], fit_category: str) -> list[str]:
    suggestions = []

    if missing_skills:
        suggestions.append(
            "Add proof of these missing job skills in your resume: "
            + ", ".join(missing_skills[:8])
            + "."
        )

    if fit_category == "Weak Fit":
        suggestions.append("Rewrite your professional summary to target this role directly.")
        suggestions.append("Add relevant projects, work examples, certifications, or achievements related to this job.")
        suggestions.append("Improve keyword alignment with the job description before applying.")
    elif fit_category == "Moderate Fit":
        suggestions.append("Add more role-specific keywords from the job description.")
        suggestions.append("Highlight achievements with numbers, outcomes, and business impact.")
        suggestions.append("Move the most relevant experience closer to the top of the resume.")
    else:
        suggestions.append("Your resume is strongly aligned; polish formatting and add measurable achievements.")
        suggestions.append("Add portfolio links, project outcomes, or proof of impact to strengthen credibility.")

    suggestions.append("Use action verbs such as built, improved, managed, analyzed, led, deployed, optimized, and delivered.")
    return suggestions
