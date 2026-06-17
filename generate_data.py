# ============================================================
# Project  : Sales Analysis Dashboard
# Script   : generate_data.py
# Purpose  : Generate 1000 rows of realistic sales data
# Author   : Zoya
# Date     : 2026
# ============================================================

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ── Reproducibility ──────────────────────────────────────────
np.random.seed(42)
n = 1000

# ── Product & Region definitions ─────────────────────────────
products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Headphones', 'Printer']
regions  = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

categories = {
    'Laptop'     : 'Electronics',
    'Phone'      : 'Electronics',
    'Tablet'     : 'Electronics',
    'Monitor'    : 'Peripherals',
    'Keyboard'   : 'Peripherals',
    'Headphones' : 'Accessories',
    'Printer'    : 'Accessories'
}

# ── Generate random dates within 2023 ────────────────────────
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 364)) for _ in range(n)]

# ── Generate sales columns ────────────────────────────────────
product_col = [random.choice(products) for _ in range(n)]
revenue     = [round(random.uniform(200, 3000), 2) for _ in range(n)]
units       = [random.randint(1, 20) for _ in range(n)]
cost_ratio  = [round(random.uniform(0.4, 0.7), 2) for _ in range(n)]
profit      = [round(revenue[i] * (1 - cost_ratio[i]), 2) for i in range(n)]

# ── Build DataFrame ───────────────────────────────────────────
df = pd.DataFrame({
    'Date'      : dates,
    'Product'   : product_col,
    'Category'  : [categories[p] for p in product_col],
    'Region'    : [random.choice(regions) for _ in range(n)],
    'Units_Sold': units,
    'Revenue'   : revenue,
    'Cost'      : [round(revenue[i] * cost_ratio[i], 2) for i in range(n)],
    'Profit'    : profit,
})

# ── Save to CSV ───────────────────────────────────────────────
df.to_csv('raw_sales_data.csv', index=False)

print("✅ Raw data generated successfully!")
print(f"📊 Rows : {len(df)}")
print(f"📋 Cols : {df.columns.tolist()}")
print("📁 Saved : raw_sales_data.csv")
