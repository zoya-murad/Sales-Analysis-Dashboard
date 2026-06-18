# 🛒 Sales Analysis Dashboard

## 📌 Project Overview
An end to end automated sales data pipeline built with Python and Power BI. 
Generates 1000 rows of realistic sales data, cleans it, analyzes it 
and visualizes it in an interactive dashboard that auto refreshes every 24 hours.

## 🛠️ Tools Used
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=flat&logo=powerbi&logoColor=black)

## 📂 Project Structure
| File | Purpose |
|------|---------|
| `generate_data.py` | Generates 1000 rows of realistic sales data |
| `clean_data.py` | Cleans data and engineers new features |
| `eda.py` | Creates 5 exploratory analysis charts |
| `auto_refresh.py` | Automates full pipeline every 24 hours |


## 📊 Executive Summary of Findings

> **Analysis Period:** January – December 2023
> **Dataset:** 1,000 sales transactions across 5 regions and 7 products

| Metric | Value | Status |
|--------|-------|--------|
| Total Revenue | $1.63M | ✅ Strong |
| Total Profit | $735.6K | ✅ Excellent |
| Avg Profit Margin | 45% | ✅ Above Industry Average |
| Total Units Sold | 10.6K | ✅ Healthy Volume |

---

## 🔍 Key Findings

### 1. Revenue Trend
- Revenue showed **fluctuation throughout 2023** with a significant dip in mid-year (July–August)
- **Q4 was the strongest quarter** with $440K in revenue — 27% higher than Q1
- This seasonal pattern suggests **holiday-driven demand** in Q4

### 2. Regional Performance
- **Phoenix** is the top performing region by revenue
- **Chicago** follows closely in second place
- **Houston** is the weakest region — significantly behind others

### 3. Product Performance
- **Monitor** generates the highest revenue among all 7 products
- **Electronics category dominates** with 43.5% of total revenue
- **Peripherals** account for 30.7% — a strong second category
- **Headphones** is the lowest revenue generating product

### 4. Profitability
- Average profit margin of **45% is well above** the retail industry average of 20-30%
- **Laptop and Headphones** have the highest profit margins (~46%)
- **Keyboard and Monitor** have slightly lower margins (~44%) but compensate with high volume

### 5. Cost vs Profit
- Cost and profit are **well balanced** across all products
- No product is running at a loss — all 7 products are profitable
- Strong correlation between revenue and profit confirms **healthy pricing strategy**

---

## 💡 Recommendations

### 1. Address Mid-Year Revenue Dip
> **Finding:** Revenue drops significantly in July–August
>
> **Recommendation:** Launch mid-year promotions, discount campaigns or bundle offers in June–July to prevent revenue decline. Target existing customers with loyalty offers during this slow period.

### 2. Invest More in Q4 Preparation
> **Finding:** Q4 consistently outperforms all other quarters
>
> **Recommendation:** Increase inventory levels by 30% before Q4. Allocate 40% of annual marketing budget to Q3-Q4 to maximize peak season revenue.

### 3. Boost Houston Region Performance
> **Finding:** Houston significantly underperforms compared to other regions
>
> **Recommendation:** Investigate root causes — is it pricing, competition, or low brand awareness? Consider region-specific promotions or assign a dedicated sales team to Houston.

### 4. Double Down on Electronics
> **Finding:** Electronics drives 43.5% of total revenue
>
> **Recommendation:** Expand the Electronics product line. Introduce new SKUs in this category. Consider premium versions of top sellers like Monitor and Phone.

### 5. Revive Headphones Sales
> **Finding:** Headphones has the lowest revenue despite a healthy profit margin
>
> **Recommendation:** Headphones have good margins but poor sales volume. A targeted marketing campaign or bundle deal (e.g. Phone + Headphones) could significantly boost revenue without hurting profitability.

### 6. Maintain Pricing Strategy
> **Finding:** 45% profit margin across all products
>
> **Recommendation:** Current pricing strategy is working excellently. Maintain price points and focus on volume growth rather than price increases to stay competitive.

---

## ✅ Conclusion

The business is in a **strong financial position** with healthy revenue, excellent profit margins and diversified product performance. The primary opportunities for growth lie in:

1. **Smoothing seasonal revenue fluctuations** through mid-year campaigns
2. **Expanding the Electronics category** which shows the strongest demand
3. **Developing the Houston market** which is currently underperforming
4. **Leveraging Q4 peak season** with better inventory and marketing preparation

With these strategies implemented, the business has strong potential to grow revenue by **15-20% in the next fiscal year.**

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python (pandas, numpy) | Data generation & cleaning |
| Matplotlib & Seaborn | Exploratory data analysis |
| Power BI | Interactive dashboard & visualization |
| GitHub | Version control & portfolio |

## 📸 Dashboard Preview

### Executive Summary
<img src="Executive Summary.png" width="800"/>

### Sales Trends
<img src="Sales Trends.png" width="800"/>

### Regional Analysis
<img src="Regional Analysis.png" width="800"/>

### Product Performance
<img src="Product Performance.png" width="800"/>

### Profit Analysis
<img src="Profit Analysis .png" width="800"/>


## ⚙️ How to Run
```bash
# Step 1 - Generate data
python generate_data.py

# Step 2 - Clean data
python clean_data.py

# Step 3 - Run EDA charts
python eda.py

# Step 4 - Auto refresh every 24 hours
python auto_refresh.py
```

## 👩‍💻 Author
**Zoya Murad** — Data Analyst & Aspiring Data Scientist
