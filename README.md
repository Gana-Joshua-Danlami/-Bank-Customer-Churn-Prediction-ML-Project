# 🗂️ Bank-Customer-Churn-Prediction-ML-Project
Predicting bank customer churn using machine learning to help businesses retain high-risk customers.
---
This project uses machine learning to predict whether a customer will leave a bank (churn), based on demographic and account-related data. Churn prediction helps banks retain high-value customers by identifying early signs of dissatisfaction.

## Dataset
- Source: Kaggle  
- File: `Churn_Modelling.csv`  
- Location: `data/raw/`
  
---

## Project Goals
- Understand key drivers of customer churn
- Build a predictive machine learning model
- Visualize churn trends using Tableau
- Recommend retention strategies based on insights

---

## 🛠️ Tools & Tech
- Python (Pandas, Scikit-learn, XGBoost)
- Tableau (for dashboard storytelling)
- Google Colab
- Git & GitHub

## 📁 Project Structure

 ### data/

│   ├── raw_data.csv

│   └── processed_data.csv

### notebooks/

│   └── churn_prediction_modeling.ipynb

### scripts/

│   └── churn_model_pipeline.py

### outputs/

│   ├── churn_strategy.md

│   ├── feature_importance_ranking.txt

│   ├── threshold_evaluation.txt

│   ├── top_10_percent_churn_risk.csv

│   ├── churn_feature_importance.png

│   ├── churn_confusion_matrix.png

│   ├── churn_persona_breakdown.md

│   ├── churn_strategy_recommendations.md

│   └── churn_precision_recall_curve.png

### models/

│   └── xgb_churn_model.pkl

├── README.md

├── requirements.txt

└── .gitignore
---

## 📊 Tableau Dashboard: Visual Insight Layer

Explore churn behavior across customer groups with this clean, client-facing dashboard:

**🔗 [View Tableau Dashboard](https://public.tableau.com/views/BankCustomerChurnAnalysis_17535099327740/BankCustomerChurnAnalysis)**

**Key Views Include:**
- KPI Overview: Churn %, Retention %, Total Customers
- Churn by Geography, Tenure Bands, Gender & Age Groups
- Dynamic filters for deeper exploration across customer segments

The dashboard was designed to mirror real business use cases and is fully interactive for exploration and insight storytelling.

---

## 📤 Output Files Explained

- `feature_importance_ranking.txt`: Top features influencing churn
- `threshold_evaluation.txt`: Model behavior across decision thresholds
- `top_10_percent_churn_risk.csv`: Highest-risk customers with persona labels
- `churn_persona_breakdown.md`: Persona clusters based on churn behavior
- `churn_strategy_recommendations.md`: Strategy memo for retention
- Visuals: Feature importance, PR curve, confusion matrix

---

## 🔍 Key Churn Insights

**Top Predictors:**
- Lack of Active Membership
- Fewer Products Owned
- Geography (especially Germany and Spain)
- Age & Tenure bands

**Surprising Insight:**
Financial metrics like salary and credit score were **less predictive** engagement and behavior mattered more.

---

## Recommendations

- Run churn-triggered interventions for users with low engagement
- Tailor campaigns for Germany & Spain segments
- Build re-engagement flows for "mid-tenure, inactive" personas
- Personalize upsell campaigns for active single-product users
- Launch A/B retention tests with loyalty incentives

---

## Summary

This project simulates a real business use case using data and machine learning to drive **customer retention** strategy. It bridges both technical implementation and stakeholder-ready insights through the final Tableau dashboard.




