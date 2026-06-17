# ============================================================
# Project  : Sales Analysis Dashboard
# Script   : eda.py
# Purpose  : Exploratory Data Analysis — generate 5 insight charts
# Author   : Zoya
# Date     : 2026
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load clean data ───────────────────────────────────────────
df = pd.read_excel('clean_sales_data.xlsx')
sns.set_theme(style='whitegrid')

print("✅ Data loaded!")
print(f"📊 Shape : {df.shape}")

# ── Chart 1 : Monthly Revenue Trend ──────────────────────────
# Shows whether revenue is growing or declining over the year
monthly_revenue = df.groupby(['Month_Num', 'Month'])['Revenue'].sum().reset_index()
monthly_revenue = monthly_revenue.sort_values('Month_Num')

plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_revenue, x='Month', y='Revenue',
             marker='o', color='steelblue', linewidth=2.5)
plt.title('Monthly Revenue Trend 2023', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('eda_monthly_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 1 saved — Monthly Revenue Trend")

# ── Chart 2 : Revenue by Region ──────────────────────────────
# Identifies which region is the top performer
region_revenue = df.groupby('Region')['Revenue'].sum().reset_index()
region_revenue = region_revenue.sort_values('Revenue', ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=region_revenue, x='Region', y='Revenue', palette='Blues_d')
plt.title('Total Revenue by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.tight_layout()
plt.savefig('eda_region_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 2 saved — Revenue by Region")

# ── Chart 3 : Profit by Product ──────────────────────────────
# Shows which products generate the most profit
product_profit = df.groupby('Product')['Profit'].sum().reset_index()
product_profit = product_profit.sort_values('Profit', ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(data=product_profit, x='Product', y='Profit',
            hue='Product', palette='Greens_d', legend=False)
plt.title('Total Profit by Product', fontsize=16, fontweight='bold')
plt.xlabel('Product', fontsize=12)
plt.ylabel('Total Profit ($)', fontsize=12)
plt.tight_layout()
plt.savefig('eda_product_profit.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 3 saved — Profit by Product")

# ── Chart 4 : Revenue by Category (Pie) ──────────────────────
# Shows the revenue share of each product category
category_revenue = df.groupby('Category')['Revenue'].sum().reset_index()

plt.figure(figsize=(6, 6))
plt.pie(
    category_revenue['Revenue'],
    labels=category_revenue['Category'],
    autopct='%1.1f%%',
    colors=['steelblue', 'coral', 'mediumseagreen'],
    startangle=90,
    explode=[0.05, 0.05, 0.05]
)
plt.title('Revenue by Category', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('eda_category_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 4 saved — Revenue by Category")

# ── Chart 5 : Correlation Heatmap ────────────────────────────
# Shows relationships between numeric columns
# Strong correlation between Revenue & Profit confirms healthy pricing
plt.figure(figsize=(7, 5))
corr = df[['Revenue', 'Cost', 'Profit', 'Units_Sold', 'Profit_Margin_%']].corr()
sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('eda_correlation.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 5 saved — Correlation Heatmap")

print("\n🎉 All 5 charts generated and saved successfully!")
