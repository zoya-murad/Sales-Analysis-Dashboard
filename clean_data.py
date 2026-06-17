# ============================================================
# Project  : Sales Analysis Dashboard
# Script   : clean_data.py
# Purpose  : Load raw data, clean it and engineer new features
# Author   : Zoya
# Date     : 2026
# ============================================================

import pandas as pd

# ── Load raw data ─────────────────────────────────────────────
df = pd.read_csv('raw_sales_data.csv')
print("✅ Raw data loaded!")
print(f"📊 Shape : {df.shape}")

# ── Convert Date column to datetime ──────────────────────────
df['Date'] = pd.to_datetime(df['Date'])

# ── Extract time-based features ───────────────────────────────
# Month name is used for labels in charts
# Month number is used for sorting in Power BI
# Quarter is used for quarterly trend analysis
df['Month']          = df['Date'].dt.month_name()
df['Month_Num']      = df['Date'].dt.month
df['Quarter']        = df['Date'].dt.quarter.apply(lambda x: f'Q{x}')

# ── Calculate Profit Margin ───────────────────────────────────
# Profit Margin % shows how much profit we make per dollar of revenue
df['Profit_Margin_%'] = round((df['Profit'] / df['Revenue']) * 100, 2)

# ── Data quality checks ───────────────────────────────────────
print(f"\n🔍 Duplicate rows  : {df.duplicated().sum()}")
print(f"🔍 Missing values  :\n{df.isnull().sum()}")

# ── Save clean data to Excel ──────────────────────────────────
df.to_excel('clean_sales_data.xlsx', index=False)

print("\n✅ Clean data saved successfully!")
print(f"📊 Rows    : {len(df)}")
print(f"📋 Columns : {df.columns.tolist()}")
print("📁 Saved   : clean_sales_data.xlsx")
print("🎉 Ready for Power BI!")
