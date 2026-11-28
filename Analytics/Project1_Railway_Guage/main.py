"""
Railway Gauge Analysis
======================
Dataset : railway_gauges.csv  (Indian railway track length by gauge, 1964-65 to 2012-13)
Output  : All charts are saved to the  graphs/  folder.

Project structure
-----------------
railway_project/
├── railway_analysis.py   <- this file
├── railway_gauges.csv    <- dataset
└── graphs/               <- generated charts (commit this folder to GitHub)

Run with:  python railway_analysis.py
"""

# ---------------------------------------------------------------------------
# 0. IMPORTS AND SETUP
# ---------------------------------------------------------------------------

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")             # save graphs to files, no pop-up windows
import matplotlib.pyplot as plt

os.makedirs("graphs", exist_ok=True)   # create the graphs folder


# ---------- SCENARIO 1: Load and clean the data ----------

'''1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
'''
df = pd.read_csv("railway_gauges.csv")     # 1. load the CSV file
print(df.head())                            # 2. show first 5 rows
print(df.columns)                           # 2. show column names

df = df.fillna(0)                           # 3. missing values become 0

for col in ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]:
    df[col] = pd.to_numeric(df[col])        # 4. make them numbers

# Make a Start Year column: "1964-65" becomes 1964
df["Start Year"] = df["Year"].str[:4].astype(int)


# ---------- SCENARIO 2: Line graph of Total ----------
'''
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing
'''
plt.plot(df["Start Year"], df["Total"], marker="o")
plt.title("Growth of Total Railway Network Over Time")
plt.xlabel("Year")
plt.ylabel("Total Tracks")
plt.savefig("graphs/1_total_line_graph.png")
plt.close()

print("First year total:", df["Total"].iloc[0])
print("Last year total:", df["Total"].iloc[-1])
print("Trend: increasing overall (with some ups and downs)")


# ---------- SCENARIO 3: Bar chart after 2000 ----------

'''
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years.
'''
recent = df[df["Start Year"] > 2000]        # only years after 2000
gauges = recent[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]]
gauges.index = recent["Year"]               # use the year as the label

gauges.plot(kind="bar", figsize=(12, 6))
plt.title("Gauge Track Lengths After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend(title="Gauge")
plt.savefig("graphs/2_recent_grouped_bar.png")
plt.close()

print("Biggest gauge after 2000: Broad Gauge")


# ---------- SCENARIO 4: Pie chart of all years ----------
'''
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most.
'''
totals = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()
print(totals)

plt.pie(totals, labels=totals.index, autopct="%.1f%%")
plt.title("Share of Each Gauge (All Years)")
plt.savefig("graphs/3_gauge_pie_chart.png")
plt.close()


# ---------- SCENARIO 5: Percentages, growth and more graphs ----------

'''
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
�
�
“Is the railway system shifting towards a single dominant gauge?”
'''
# Percentage of each gauge in the total
df["% Broad Gauge"] = df["Broad Gauge"] / df["Total"] * 100
df["% Metre Gauge"] = df["Metre Gauge"] / df["Total"] * 100
df["% Narrow Gauge"] = df["Narrow Gauge"] / df["Total"] * 100

# Yearly growth using np.diff (this year minus last year)
growth = np.diff(df["Total"])
best = growth.argmax()
print("Biggest growth:", growth[best], "tracks in year", df["Start Year"].iloc[best + 1])

# Line graph of the percentages
plt.plot(df["Start Year"], df["% Broad Gauge"], label="Broad")
plt.plot(df["Start Year"], df["% Metre Gauge"], label="Metre")
plt.plot(df["Start Year"], df["% Narrow Gauge"], label="Narrow")
plt.title("Percentage Share of Each Gauge")
plt.xlabel("Year")
plt.ylabel("Percent (%)")
plt.legend()
plt.savefig("graphs/4_percentage_line_graph.png")
plt.close()

# Stacked bar chart of the track lengths
stacked = df.set_index("Start Year")[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]]
stacked.plot(kind="bar", stacked=True, figsize=(14, 6))
plt.title("Track Composition by Year")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.savefig("graphs/5_stacked_bar_chart.png")
plt.close()

# Bar chart of yearly growth (biggest year in red)
years = df["Start Year"].iloc[1:]
colors = ["red" if i == best else "steelblue" for i in range(len(growth))]
plt.bar(years, growth, color=colors)
plt.title("Yearly Growth of Total Tracks (Biggest in Red)")
plt.xlabel("Year")
plt.ylabel("Change from Previous Year")
plt.savefig("graphs/6_yearly_growth.png")
plt.close()

# Conclusion
print("Broad Gauge share:", round(df["% Broad Gauge"].iloc[0], 1), "% ->",
      round(df["% Broad Gauge"].iloc[-1], 1), "%")
print("Answer: Yes, the railway is moving towards one main gauge (Broad Gauge).")
print("Done! Graphs are saved in the graphs folder.")
