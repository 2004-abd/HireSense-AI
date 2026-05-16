
# HireSense AI

HireSense AI is a full-stack AI web application that analyzes how well a resume matches a job description. It supports text input and PDF/DOCX resume upload, predicts Strong Fit, Moderate Fit, or Weak Fit, shows matched/missing skills, stores history in MongoDB, and displays model metrics.

## Features

- User registration and login
- Password hashing with Bcrypt
- JWT-based authentication
- Protected dashboard, history, and metrics pages
- Resume text analysis
- PDF/DOCX resume upload
- Job description matching
- AI fit prediction
- Matched and missing skill extraction
- Skill match percentage
- Analysis charts
- MongoDB history tracking
- Model performance dashboard
- Confusion matrix visualization

## Tech Stack

### Frontend
- Next.js
- React
- TypeScript
- Recharts
- CSS

### Backend
- FastAPI
- Python
- Pydantic
- Uvicorn
- JWT Authentication
- Passlib / Bcrypt

### Database
- MongoDB
- Motor async MongoDB driver

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Pandas
- NumPy
- Joblib

### File Processing
- pypdf for PDF parsing
- python-docx for DOCX parsing

## Project Structure

```text
hiresense-ai/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── ml/
│   │   ├── routes/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── security.py
│   ├── data/
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── package.json
│
└── README.md
````

## AI Workflow

1. **Data Gathering**
   Dataset is generated using `generate_dataset.py`. It contains 10,000+ resume-job examples across technology, business, marketing, finance, healthcare, HR, education, design, operations, and support roles.

2. **Data Cleaning**
   The training pipeline removes missing values, duplicate rows, short text rows, extra spaces, and formatting noise.

3. **Feature Engineering**
   Resume text and job descriptions are combined and converted into numerical features using TF-IDF Vectorizer.

4. **Model Training**
   Logistic Regression is used to classify resume-job pairs into:

   * Strong Fit
   * Moderate Fit
   * Weak Fit

5. **Model Evaluation**
   The system calculates:

   * Accuracy
   * Precision
   * Recall
   * F1 Score
   * Confusion Matrix

## MongoDB Collections

```text
users
analyses
model_metrics
system_logs
```

MongoDB stores registered users, hashed passwords, analysis history, logs, and model metrics.

## Environment Variables

Create `backend/.env`:

```env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=hiresense_ai
JWT_SECRET=your_secret_key_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
FRONTEND_ORIGIN=http://localhost:3000
```

Create `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## How to Run

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app/ml/generate_dataset.py
python app/ml/train_model.py
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

### Frontend

Open a new terminal:

cd frontend
npm install
npm run dev


Frontend runs on:


http://localhost:3000


## Main Pages


/           Landing Page
/register   Register Page
/login      Login Page
/dashboard  Protected AI Dashboard
/history    Protected Analysis History
/accuracy   Protected Model Metrics Page
/about      Project Documentation Page


## API Endpoints

### Authentication


POST /auth/register
POST /auth/token


### Resume Analysis

POST /analysis/resume-fit
POST /analysis/resume-fit-file
GET  /analysis/history


### Metrics

GET /metrics/model


## Security

* Passwords are hashed before saving in MongoDB.
* JWT token is generated after login.
* Protected routes require a valid token.
* Dashboard, history, and metrics pages are not accessible without login.
* `.env` and `.env.local` should not be uploaded to GitHub.

## Testing Flow

1. Open `http://localhost:3000`
2. Register a new account
3. Login
4. Open Dashboard
5. Paste resume text or upload PDF/DOCX resume
6. Paste job description
7. Click Analyze Resume
8. View fit score, matched skills, missing skills, chart, and suggestions
9. Open History page
10. Open Metrics page




