# Churn Insights Summary : EDA Findings

This report summarizes key customer behavior patterns that correlate with churn. The goal is to help business stakeholders understand where churn is coming from and who is most likely to leave.

---

## Churn Rate Overview

- Churn rate is **~20%**, meaning 1 in 5 customers are leaving.
- The dataset is slightly imbalanced, mitigation will be handled during model training (SMOTE, class weights).

---

## Bivariate Insights

### 1. Balance vs Churn
- Customers with **zero balance** have noticeably higher churn.
- Indicates a segment that maintains accounts without using them.

### 2. Age vs Churn
- Churn rate increases with **age**, especially from age 45 upward.
- Older customers may feel underserved or be targeted by competitors.

### 3. Products Number vs Churn
- Customers with **only one product** are far more likely to churn.
- Suggests that upselling additional products could reduce churn.

### 4. Credit Card Ownership
- Slightly higher churn among customers **without credit cards**.
- May reflect lower financial engagement or less stickiness.

### 5. Active Members
- **Inactive members** are significantly more likely to churn.
- Engagement is a key churn predictor.

### 6. Tenure vs Churn
- No strong linear pattern, but slight increase in churn around **mid-tenure years (3–6)**.

---

## Geographic Patterns

- Churn is highest in **Germany**, followed by **France**, and lowest in **Spain**.
- Location-based strategies may be necessary.

---

## Gender

- **Slightly higher churn** observed among **female customers**, but not drastically different.

---

## Key Takeaways

- **Inactive**, **single-product**, **older** customers with **zero balance** are at highest risk.
- Targeting these groups with engagement campaigns or personalized offers could reduce churn significantly.
- Germany-based users should be monitored more closely to explore reasons via customer feedback or service data.



