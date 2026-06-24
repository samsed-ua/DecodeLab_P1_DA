# DecodeLabs Data Analytics Internship

This repository contains the four projects completed as part of the **DecodeLabs Data Analytics Internship Program**. Each project builds on the output of the previous one, using a single synthetic e-commerce dataset throughout.

**Pipeline:** [Project 1 (Cleaning)](#project-1--data-cleaning--preparation) → [Project 2 (EDA)](#project-2--exploratory-data-analysis-eda) → [Project 3 (SQL Analysis)](#project-3--sql-data-analysis) → [Project 4 (Visualization)](#project-4--data-visualization)

## Notebooks

| Project | Notebook | Link |
|---|---|---|
| 1 | Data Cleaning & Preparation | [Data_Analytics_Project_1.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_1.ipynb) |
| 2 | Exploratory Data Analysis | [Data_Analytics_Project_2.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_2.ipynb) |
| 3 | SQL Data Analysis | [Data_Analytics_Project_3.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_3.ipynb) |
| 4 | Data Visualization | [Data_Analytics_Project_4.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_4.ipynb) |

---

## Dataset

| | |
|---|---|
| **Raw input** | `Dataset for Data Analytics.csv` |
| **Cleaned output** (used by Projects 2–4) | `Cleaned_Dataset.xlsx` |
| **Size** | 1,200 rows × 14 columns |
| **Time span** | January 2023 – June 2025 |
| **Fields** | `OrderID`, `CustomerID`, `Date`, `Product`, `Quantity`, `UnitPrice`, `TotalPrice`, `PaymentMethod`, `OrderStatus`, `TrackingNumber`, `ItemsInCart`, `CouponCode`, `ReferralSource`, `ShippingAddress` |

---

## Project 1 — Data Cleaning & Preparation

**Notebook:** [Data_Analytics_Project_1.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_1.ipynb)

Takes the raw CSV export and produces an analysis-ready dataset.

**What it does:**
- Initial data audit (`.info()`, `.describe()`) and distribution check on `TotalPrice`
- Converts `UnitPrice` and `TotalPrice` to numeric, coercing invalid values
- Checks and reports missing values (count + percentage per column)
- Fills missing `CouponCode` values with `'NO_COUPON'`
- Checks for duplicate rows
- Standardizes the `Date` column to proper `datetime`
- Cleans formatting on text/object columns
- Re-validates dtypes and memory usage after cleaning

**Outputs:**
- `cleaned_data.csv`
- `cleaned_data.xlsx`
- `cleaned_data_custom.csv` (UTF-8, NaNs replaced with `'NULL'`)
- `download_data.csv` (Jupyter `FileLink` download trigger)

**Tools:** Python, pandas, numpy, seaborn

---

## Project 2 — Exploratory Data Analysis (EDA)

**Notebook:** [Data_Analytics_Project_2.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_2.ipynb)

Reads `Cleaned_Dataset.xlsx` and surfaces the core statistical patterns in the data.

**What it does:**
1. **Basic statistics** — count, mean, median for `Quantity`, `UnitPrice`, `TotalPrice`, `ItemsInCart`; most common `Product`, `PaymentMethod`, and `OrderStatus`
2. **Trends** — revenue by year, revenue by product, order status counts
3. **Outlier detection** — IQR method applied to all four numeric columns, with flagged order IDs printed
4. **Charts** — a 2-panel matplotlib figure: distribution of order value (with mean/median lines) and revenue by product
5. **Key observations** — a plain-language summary covering average vs. median order value, cancellation/return rate, top revenue product, and outlier interpretation

**Outputs:**
- `eda_charts.png`

**Tools:** Python, pandas, matplotlib

---

## Project 3 — SQL Data Analysis

**Notebook:** [Data_Analytics_Project_3.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_3.ipynb)

Loads the cleaned dataset into an in-memory **SQLite** database and answers 10 business questions using progressively advanced SQL, with a markdown business-question/insight pair before and after every query.

**SQL concepts demonstrated:**

| # | Query | Concept |
|---|---|---|
| 1 | First 10 orders | `SELECT` |
| 2 | Cancelled orders | `WHERE` (equality) |
| 3 | Orders ≥ $2,000 | `WHERE` (comparison) + `ORDER BY` |
| 4 | Laptop orders | `WHERE LIKE` (pattern matching) |
| 5 | Top 10 highest-value orders | `ORDER BY` + `LIMIT` |
| 6 | Orders per product | `GROUP BY` + `COUNT` |
| 7 | Revenue by payment method | `GROUP BY` + `SUM` |
| 8 | Avg order value by referral source | `GROUP BY` + `AVG` |
| 9 | Products earning > $150,000 | `GROUP BY` + `HAVING` |
| 10 | Coupon performance on delivered orders | `WHERE` + `GROUP BY` + `ORDER BY` (combined) |

**Key insights:**
- Facebook referrals produce the highest **average** order value (not necessarily the most orders)
- `SAVE10` had the highest average order value among delivered, coupon-using orders, ahead of `FREESHIP`

**Outputs:**
- `SQL_Query_Results.xlsx` — each query's result set on its own sheet
- `queries.sql` — standalone, reusable SQL script

**Tools:** Python, `sqlite3`, pandas, openpyxl

---

## Project 4 — Data Visualization

**Notebook:** [Data_Analytics_Project_4.ipynb](https://github.com/samsed-ua/DecodeLab_P1_DA/blob/main/Data_Analytics_Project_4.ipynb)

An **optional mastery milestone** focused on data storytelling rather than exploratory charting — translating findings into boardroom-ready visuals with action titles, a single highlight color, and a "so what?" takeaway under every chart.

**Design rules followed:**
- No pie/donut/3D charts
- Bar chart axes always start at zero (no truncated-axis distortion)
- Minimal gridlines/borders; direct data labeling instead of legends where possible
- One highlight color per chart; everything else neutral grey
- Action titles that state the conclusion, not just the topic

**Charts produced:**

| # | Chart | Type | Insight |
|---|---|---|---|
| 1 | Monthly revenue trend | Line | Revenue declined 6.4% from Jan 2023 to Jun 2025, peaking Jun 2024 |
| 2 | Revenue by product | Horizontal bar | Chair is the top revenue product |
| 3 | Cart size vs. order value | Scatter + trend line | Moderate positive relationship |
| 4 | Orders by referral source | Horizontal bar | Instagram drives the most orders |
| 5 | Monthly revenue trend, top 3 products | Multi-line | Laptop, Chair, Printer all show volatile month-to-month revenue |
| 6 | Referral source quality (avg. order value) | Horizontal bar | Facebook has the highest average order value, despite lower order volume than Instagram |
| 7 | Quarterly revenue trend | Line | Used to check whether the decline is seasonal or sustained |

**Also includes:**
- An **Executive KPI summary** table (total revenue, total orders, AOV, average cart size, peak month, top product, top channel)
- A **business recommendations** table tying each finding to a suggested action
- A final written conclusion synthesizing all charts into one narrative

**Outputs:**
- 7 chart PNGs (saved individually)
- KPI summary and recommendations tables (in-notebook)

**Tools:** Python, pandas, matplotlib

---

## How to Run

1. Open each notebook in Jupyter, in order (1 → 2 → 3 → 4) — or click the links above to view them directly on GitHub
2. Update the file path at the top of each notebook to point to your local copy of the dataset (`Cleaned_Dataset.xlsx` for Projects 2–4)
3. Run all cells top to bottom

**Requirements:**
```
pandas
numpy
matplotlib
seaborn
openpyxl
```

---

## Author

**[samsed-ua](https://github.com/samsed-ua)** — Internship project completed as part of the **DecodeLabs Data Analytics Internship Program**.
