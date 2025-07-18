# 🗂️ Bank-Customer-Churn-Prediction-ML-Project
Predicting bank customer churn using machine learning to help businesses retain high-risk customers.
---
This project uses machine learning to predict whether a customer will leave a bank (churn), based on demographic and account-related data. Churn prediction helps banks retain high-value customers by identifying early signs of dissatisfaction.

## Dataset
- Source: Kaggle  
- File: `Churn_Modelling.csv`  
- Location: `data/raw/`

## Project Goals
- Understand key drivers of customer churn
- Build a predictive model using ML
- Provide insights to reduce churn risk

## 🛠️ Tools & Tech
- Python (Pandas, Scikit-learn, XGBoost)
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
### 📤 Output Files Explained

- `feature_importance_ranking.txt`: Ranked list of top predictors of churn.
- `threshold_evaluation.txt`: Summary of how model performance varies at different probability thresholds.
- `top_10_percent_churn_risk.csv`: Contains the top 10% highest-risk customers and their associated persona labels.
- `churn_feature_importance.png`: Visual plot of feature importance scores.
- `churn_confusion_matrix.png`: Confusion matrix showing final prediction performance.
- `churn_persona_breakdown.md`: Summarizes top churn-risk customer personas
- `churn_strategy_recommendations.md`: Actionable business strategies to reduce churn
---
## 💡 Business Insight Summary: Key Drivers of Customer Churn

Our trained XGBoost model identified the top predictors of customer churn, helping us uncover which behaviors and traits most strongly influence a customer’s decision to leave.

### 🔑 Top Churn Drivers:

1. **Active Membership Status**

   * The most influential feature. Customers who are **not active members** are significantly more likely to churn.

2. **Number of Products Owned**

   * Fewer products → higher churn risk. Cross-sell opportunities (getting customers to use more services) may improve retention.

3. **Gender**

   * Gender showed influence, suggesting possible behavioral or engagement differences worth exploring further.

4. **Country (especially Germany & Spain)**

   * Customers in **Germany** showed higher churn risk. Spain also featured prominently, highlighting the need for region-specific strategies.

5. **Age & Tenure Group**

   * **Older customers** and those in certain tenure bands (e.g. "New" or "Mid") had higher risk. Lifecycle-based retention strategies could help.

6. **Behavioral Combos**

   * Features like `has_credit_and_active` indicate **combinations of engagement** (e.g. having credit + being active) are valuable for retention.

7. **Credit Score & Salary Had Low Impact**

   * Surprisingly, financial metrics like `estimated_salary`, `balance_salary_ratio`, and `credit_score` were **less predictive** of churn in this dataset, suggesting that **behavioral and demographic factors** are more critical.

---

### What This Means for the Business:

* **Retention focus should prioritize engagement behaviors** (activity, number of products) over purely financial metrics.
* **Targeted campaigns** in countries like Germany and among new customers can deliver quick wins.
* **Personalized outreach** for low-engagement segments (inactive, single-product customers) may reduce churn significantly.

---

### **Business Recommendations & Churn Prevention Strategy**
---

## High-Risk Customer Personas & Churn Strategy

### 🎯 Top At-Risk Personas:

| Persona                    | % of Churn Risk Customers | Suggested Action                                                                                      |
| -------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------- |
| `Other, Active`          | 14%                       | Conduct satisfaction survey, these customers are engaged but may lack reward or progression          |
| `, Other, Not Active`      | 12%                       | Low activity customers test automated check-ins or loyalty perks                                    |
| `, Germany, Other, Active` | 11%                       | Germany-based active users segment-specific campaigns in local language, offer region-based rewards |
| `Mid, Other, Not Active`   | 8%                        | Customers with some tenure but dropping activity build   re-engagement flows                          |
| `, Spain, Not Active`      | 6%                        | Spain-based low-activity users explore language support or cultural barriers                        |
| `Mid, Spain, Active`       | 5%                        | Actively engaged in Spain, nurture and upsell with premium product lines                             |

### General Recommendations:

* Launch **churn-triggered campaigns** using model scores (threshold ≥ 0.70)
* Develop **rewards tiers** based on tenure and product usage
* Offer **live support or onboarding refreshers** to older users not using all products
* **Personalize messages** for Germany and Spain top churn geographies
* Run **retention A/B tests** with incentives for `not active + credit card` groups

---


