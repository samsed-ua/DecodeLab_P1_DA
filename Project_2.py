#!/usr/bin/env python
# coding: utf-8

# In[11]:


"""
======================================================
  DecodeLabs | Data Analytics - Project 2
  Exploratory Data Analysis (EDA)
======================================================
  INPUT  : Cleaned_Dataset.xlsx
  GOAL   : Understand patterns, trends, distributions
           - Basic statistics (mean, median, count)
           - Trends and outliers
           - Key observations
======================================================
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
"""
======================================================
  DecodeLabs | Data Analytics - Project 2
  Exploratory Data Analysis (EDA)
======================================================
  INPUT  : Cleaned_Dataset.xlsx
  GOAL   : Understand patterns, trends, distributions
           - Basic statistics (mean, median, count)
           - Trends and outliers
           - Key observations
======================================================
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\urmee\\OneDrive - University of Surrey\\Desktop\\Deodelab_DA\\Cleaned_Dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])

numeric_cols = ["Quantity", "UnitPrice", "TotalPrice", "ItemsInCart"]

# ─────────────────────────────────────────────
# 1. BASIC STATISTICS
# ─────────────────────────────────────────────
print("=" * 50)
print("BASIC STATISTICS")
print("=" * 50)

stats = df[numeric_cols].agg(["count", "mean", "median"]).round(2)
print(stats)

print("\nMost common product:", df["Product"].mode()[0])
print("Most common payment method:", df["PaymentMethod"].mode()[0])
print("Most common order status:", df["OrderStatus"].mode()[0])

# ─────────────────────────────────────────────
# 2. TRENDS
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("TRENDS")
print("=" * 50)

revenue_by_year = df.groupby(df["Date"].dt.year)["TotalPrice"].sum().round(2)
print("\nRevenue by year:")
print(revenue_by_year)

revenue_by_product = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False).round(2)
print("\nRevenue by product:")
print(revenue_by_product)

status_counts = df["OrderStatus"].value_counts()
print("\nOrder status counts:")
print(status_counts)

# ─────────────────────────────────────────────
# 3. OUTLIERS (IQR method)
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("OUTLIERS")
print("=" * 50)

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"\n{col}: {len(outliers)} outliers (outside {lower:.2f} - {upper:.2f})")
    if len(outliers) > 0:
        print(outliers[["OrderID", col]].to_string(index=False))

# ─────────────────────────────────────────────
# 4. SIMPLE CHARTS
# ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df["TotalPrice"], bins=20, color="#1F3864")
axes[0].axvline(df["TotalPrice"].mean(), color="red", linestyle="--", label="Mean")
axes[0].axvline(df["TotalPrice"].median(), color="green", label="Median")
axes[0].set_title("Distribution of Order Value")
axes[0].set_xlabel("TotalPrice")
axes[0].legend()

axes[1].bar(revenue_by_product.index, revenue_by_product.values, color="#1F3864")
axes[1].set_title("Revenue by Product")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Total Revenue")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("eda_charts.png", dpi=150)
print("\nCharts saved to eda_charts.png")

# ─────────────────────────────────────────────
# 5. KEY OBSERVATIONS
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("KEY OBSERVATIONS")
print("=" * 50)

mean_val = df["TotalPrice"].mean()
median_val = df["TotalPrice"].median()
cancelled_returned = status_counts.get("Cancelled", 0) + status_counts.get("Returned", 0)
top_product = revenue_by_product.index[0]

print(f"""
1. Average order value is ${mean_val:.2f}, but the median is ${median_val:.2f} -
   a few large orders are pulling the average up.

2. {cancelled_returned} orders ({cancelled_returned/len(df)*100:.1f}%) were Cancelled
   or Returned - worth looking into why.

3. "{top_product}" brings in the most revenue overall.

4. A small number of orders (TotalPrice outliers) are much higher value than
   the rest - these look like genuine big purchases, not data errors.
""")
df["Date"] = pd.to_datetime(df["Date"])

numeric_cols = ["Quantity", "UnitPrice", "TotalPrice", "ItemsInCart"]

# ─────────────────────────────────────────────
# 1. BASIC STATISTICS
# ─────────────────────────────────────────────
print("=" * 50)
print("BASIC STATISTICS")
print("=" * 50)

stats = df[numeric_cols].agg(["count", "mean", "median"]).round(2)
print(stats)

print("\nMost common product:", df["Product"].mode()[0])
print("Most common payment method:", df["PaymentMethod"].mode()[0])
print("Most common order status:", df["OrderStatus"].mode()[0])

# ─────────────────────────────────────────────
# 2. TRENDS
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("TRENDS")
print("=" * 50)

revenue_by_year = df.groupby(df["Date"].dt.year)["TotalPrice"].sum().round(2)
print("\nRevenue by year:")
print(revenue_by_year)

revenue_by_product = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False).round(2)
print("\nRevenue by product:")
print(revenue_by_product)

status_counts = df["OrderStatus"].value_counts()
print("\nOrder status counts:")
print(status_counts)

# ─────────────────────────────────────────────
# 3. OUTLIERS (IQR method)
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("OUTLIERS")
print("=" * 50)

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"\n{col}: {len(outliers)} outliers (outside {lower:.2f} - {upper:.2f})")
    if len(outliers) > 0:
        print(outliers[["OrderID", col]].to_string(index=False))

# ─────────────────────────────────────────────
# 4. SIMPLE CHARTS
# ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df["TotalPrice"], bins=20, color="#1F3864")
axes[0].axvline(df["TotalPrice"].mean(), color="red", linestyle="--", label="Mean")
axes[0].axvline(df["TotalPrice"].median(), color="green", label="Median")
axes[0].set_title("Distribution of Order Value")
axes[0].set_xlabel("TotalPrice")
axes[0].legend()

axes[1].bar(revenue_by_product.index, revenue_by_product.values, color="#1F3864")
axes[1].set_title("Revenue by Product")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Total Revenue")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("eda_charts.png", dpi=150)
print("\nCharts saved to eda_charts.png")

# ─────────────────────────────────────────────
# 5. KEY OBSERVATIONS
# ─────────────────────────────────────────────
print("\n" + "=" * 50)
print("KEY OBSERVATIONS")
print("=" * 50)

mean_val = df["TotalPrice"].mean()
median_val = df["TotalPrice"].median()
cancelled_returned = status_counts.get("Cancelled", 0) + status_counts.get("Returned", 0)
top_product = revenue_by_product.index[0]

print(f"""
1. Average order value is ${mean_val:.2f}, but the median is ${median_val:.2f} -
   a few large orders are pulling the average up.

2. {cancelled_returned} orders ({cancelled_returned/len(df)*100:.1f}%) were Cancelled
   or Returned - worth looking into why.

3. "{top_product}" brings in the most revenue overall.

4. A small number of orders (TotalPrice outliers) are much higher value than
   the rest - these look like genuine big purchases, not data errors.
""")


# In[ ]:





# In[13]:


import os
import glob

# Check current working directory
print("Current working directory:", os.getcwd())

# Search for your specific file
file_pattern = "*eda_charts*.png"
matching_files = glob.glob(file_pattern)

if matching_files:
    print(f"\nFound matching files:")
    for file in matching_files:
        print(f"  - {os.path.abspath(file)}")
else:
    print(f"\nNo files matching '{file_pattern}' found in current directory")

# Also search in common subdirectories
common_dirs = ['images', 'plots', 'figures', 'output', 'charts']
for dir_name in common_dirs:
    if os.path.exists(dir_name):
        dir_files = glob.glob(os.path.join(dir_name, file_pattern))
        if dir_files:
            print(f"\nFound in '{dir_name}' directory:")
            for file in dir_files:
                print(f"  - {os.path.abspath(file)}")


# In[ ]:





# In[15]:





# In[ ]:




