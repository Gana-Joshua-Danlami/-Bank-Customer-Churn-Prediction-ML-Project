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

