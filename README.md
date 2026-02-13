# Credit Scoring MLOps Platform

Production machine learning system for point-of-sale credit decisioning.

**Live Demo:** https://samkul-swe.github.io/claritypay-mlops-demo  
**API:** https://claritypay-mlops-demo.onrender.com/docs  
**Code:** https://github.com/samkul-swe/claritypay-mlops-demo

---

## What This Is

An end-to-end MLOps system that makes real-time credit decisions. Built to demonstrate production ML capabilities for fintech lending platforms.

**Try it:** Visit the live demo, click a button, see the API make a credit decision in real-time.

---

## What's Built

**Credit Scoring Model**
- XGBoost classifier trained on 10,000 applications
- 85% accuracy
- Predicts default risk and recommends loan terms

**Production API**
- FastAPI serving predictions in <200ms
- Automatic documentation at `/docs`
- Input validation and error handling
- Health monitoring

**Cloud Deployment**
- Docker containerized
- Deployed on Render (live 24/7)
- AWS S3 for model storage
- Databricks for distributed training

**Explainability**
- Shows why each decision was made
- Required for lending compliance (ECOA/FCRA)
- Identifies top risk factors

---

## How It Works
```
1. User submits application data (age, income, debt, etc.)
   ↓
2. API validates the input
   ↓
3. XGBoost model predicts default risk
   ↓
4. System calculates credit score (0-850)
   ↓
5. Assigns loan terms based on score (APR, months, payment)
   ↓
6. Explains the decision (top factors)
   ↓
7. Returns JSON response
```

**Example:**
```bash
curl -X POST "https://claritypay-mlops-demo.onrender.com/predict" \
  -d '{"age": 35, "annual_income": 65000, ...}'

# Returns:
{
  "credit_score": 720,
  "approval_recommendation": "APPROVED",
  "recommended_terms": {
    "term_months": 12,
    "apr": 8.99,
    "monthly_payment": 318.73
  },
  "explanation": [...]
}
```

---

## Technology

**ML Stack:** Python, XGBoost, Scikit-learn, MLflow  
**API:** FastAPI, Pydantic, Uvicorn  
**Deployment:** Docker, Render  
**Cloud:** AWS S3, Databricks, MongoDB Atlas  

---

## MLOps Capabilities Shown

✅ **Complete ML Lifecycle** - Training → Deployment → Monitoring  
✅ **Production API** - Real-time inference with documentation  
✅ **Cloud Integration** - AWS and Databricks  
✅ **Containerization** - Docker for consistent deployment  
✅ **Model Monitoring** - Health checks and logging  
✅ **Explainability** - Compliance-ready decisions  

---

## Cloud Architecture

**AWS S3**
- Stores model artifacts
- Data lake for training data
- Bucket: `s3://claritypay-mlops-demo-data/`

**Databricks**
- Distributed model training
- Spark for data processing
- MLflow integration
- Community Edition demo completed

**MongoDB** (Code Complete)
- Prediction logging
- Statistics tracking
- Ready for production (requires SSL-compatible hosting)

**Docker + Render**
- Containerized deployment
- Auto-scaling ready
- Currently serving live API

---

## Quick Start

**Try It Online:**
https://samkul-swe.github.io/claritypay-mlops-demo

**Run Locally:**
```bash
git clone https://github.com/samkul-swe/claritypay-mlops-demo.git
cd claritypay-mlops-demo
docker build -t credit-scoring .
docker run -p 8000:8000 credit-scoring
# Visit: http://localhost:8000/docs
```

---

## Project Structure
```
├── src/api/main.py           # FastAPI application
├── models/credit_model.pkl   # Trained model
├── Dockerfile                 # Container config
├── requirements.txt           # Dependencies
└── index.html                 # Demo interface
```

---

## Author

**Sampada Kulkarni**  
📧 kulkarni.samp@northeastern.edu  
🔗 [linkedin.com/in/samkul-swe](https://linkedin.com/in/samkul-swe)

Built to demonstrate production MLOps capabilities for fintech ML infrastructure.

**Background:** 3 years at IBM building AIOps platforms (monitoring, deployment, data integration)

---

MIT License
