import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================================
# 1. INTEGRATED CSV DATA GENERATION PART
# This automatically creates a perfect 'weather.csv' file in your folder
# =========================================================================
weather_data = {
    "Date": [
        "2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05",
        "2026-01-06", "2026-01-07", "2026-01-08", "2026-01-09", "2026-01-10",
        "2026-07-01", "2026-07-02", "2026-07-03", "2026-07-04", "2026-07-05",
        "2026-07-06", "2026-07-07", "2026-07-08", "2026-07-09", "2026-07-10"
    ],
    "Temperature": [
        -2.5, -4.0, -5.8, -1.2, -3.1, -6.0, -4.5, -2.0, -5.2, -3.8,  # 10 Cold Days (Lows)
        32.1, 34.5, 31.0, 35.9, 33.4, 30.2, 36.5, 32.8, 31.7, 34.0   # 10 Hot Days (Highs)
    ]
}

# Turn the data dictionary into a DataFrame and save it as 'weather.csv'
pd.DataFrame(weather_data).to_csv("weather.csv", index=False)


# =========================================================================
# 2. CHART GENERATION PART (No Background Dots/Gridlines)
# =========================================================================
# Set a solid clean white background with NO dots or gridlines
sns.set_theme(style="white")

# Read the CSV file we just created
df = pd.read_csv("weather.csv")
df["Temperature"] = pd.to_numeric(df["Temperature"], errors='coerce')

# Extract top 10 highs and top 10 lows
highs_df = df.sort_values(by="Temperature", ascending=False).head(10)
lows_df = df.sort_values(by="Temperature", ascending=True).head(10)

# Combine them sequentially
extremes_df = pd.concat([highs_df, lows_df])
extremes_df["Date"] = extremes_df["Date"].astype(str)

# Build the chart window
plt.figure(figsize=(15, 8))
bar_colors = ['tomato'] * 10 + ['skyblue'] * 10

# Plot the bars
plt.bar(extremes_df["Date"],
        extremes_df["Temperature"],
        color=bar_colors)

# Labels and Styling
plt.title("Weather Extremes: Top 10 Highs vs. Top 10 Lows", fontsize=16, fontweight='bold')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the file secretly first, then show the clean pop-up window
plt.savefig("highs_and_lows_chart.png")
plt.show()
plt.close()