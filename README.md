# Credit Scoring MLOps Platform

Production machine learning system for point-of-sale credit decisioning.

---

## What This Does

Makes real-time credit decisions using machine learning. You submit application data (age, income, debt history), and it returns a credit score, approval decision, and loan terms.

Try it: Click the live demo link above and hit "Get Credit Decision"

---

## What's Built

**ML Model**
- XGBoost classifier trained on 10,000 credit applications
- 85% accuracy predicting default risk
- Returns credit score (0-850) and recommended terms

**Production API**
- FastAPI serving real-time predictions
- Automatic documentation at /docs
- Input validation and error handling
- Deployed with Docker on Render (live 24/7)

**Explainability**
- Shows top factors influencing each decision
- Required for lending compliance (ECOA/FCRA)

**Cloud Integration**
- AWS S3 bucket for model storage
- Docker containerization
- MongoDB integration (code complete, SSL issue on free tier)

---

## How It Works
```
1. Application Data → FastAPI validates input
2. XGBoost Model → Predicts default risk  
3. Scoring Logic → Converts to 0-850 credit score
4. Terms Calculator → Determines APR and payment terms
5. Explainer → Identifies top risk factors
6. JSON Response → Returns decision
```

---

## Technology Stack

**ML:** Python, XGBoost, Scikit-learn, NumPy, Pandas  
**API:** FastAPI, Pydantic, Uvicorn  
**Deployment:** Docker, Render  
**Cloud:** AWS S3, MongoDB Atlas (integration ready)  
**MLOps:** MLflow (experiment tracking)

---

## MLOps Capabilities

✅ **Model Training** - XGBoost with proper train/test split  
✅ **Model Serving** - REST API with <200ms latency  
✅ **Deployment** - Docker containerization  
✅ **Monitoring** - Health checks and logging  
✅ **Explainability** - Compliance-ready decisions  
✅ **Cloud** - AWS S3 integration, production-ready architecture  

---

## Cloud Architecture

**Current Deployment:**
```
GitHub → Render (Docker build) → Live API
```

**Data Storage:**
- AWS S3 bucket
- Model artifacts stored in S3
- Training data in S3

**MongoDB Integration:**
- Code complete for prediction logging
- `/stats` and `/recent` endpoints implemented
- Currently has SSL compatibility issue on Render free tier
- Works locally, ready for production AWS deployment

---

## Quick Start

**Run Locally:**
```bash
docker build -t credit-scoring .
docker run -p 8000:8000 credit-scoring
# Visit: http://localhost:8000/docs
```

---

## Project Structure
```
├── src/api/
│   ├── main.py          # FastAPI application
│   └── database.py      # MongoDB logging (ready)
├── models/
│   └── credit_model.pkl # Trained XGBoost model
├── Dockerfile           # Container config
├── requirements.txt     # Dependencies
└── index.html          # Demo page
```

---

## Author

**Sampada Kulkarni**  
🔗 [linkedin.com/in/samkul-swe](https://linkedin.com/in/samkul-swe)

3 years building production ML systems at IBM (AIOps infrastructure for 500+ customers)
