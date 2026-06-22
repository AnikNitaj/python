import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Set style for cleaner graphs
sns.set_theme(style="whitegrid")

# 1. Load the data safely
try:
    df = pd.read_csv('weather.csv')
    print("✅ Data successfully loaded!")
    print(f"📋 Found columns: {list(df.columns)}\n")
except Exception as e:
    print(f"❌ Error loading data: {e}")
    sys.exit()

# 2. Smart Detection: Find Date and Temperature columns case-insensitively
date_col = next((col for col in df.columns if 'date' in col.lower()), None)
temp_col = next((col for col in df.columns if 'temp' in col.lower()), None)

if not date_col or not temp_col:
    print("❌ Error: Could not automatically find both a 'Date' and a 'Temperature' column.")
    sys.exit()

print(f"🔍 Using '{date_col}' for dates and '{temp_col}' for temperature.")

# Convert string data to proper numeric and datetime objects
df[date_col] = pd.to_datetime(df[date_col])
df[temp_col] = pd.to_numeric(df[temp_col], errors='coerce')
print("🛠️  Successfully converted data types!\n")


# ==========================================
# 1. Temperature Overview
# ==========================================
avg_temp = df[temp_col].mean()
print("--- 1. Temperature Overview ---")
print(f"Average Temperature for the entire dataset: {avg_temp:.2f}\n")


# ==========================================
# 2. Monthly Temperature
# ==========================================
df['Month'] = df[date_col].dt.strftime('%B')
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

monthly_avg = df.groupby('Month')[temp_col].mean().reindex(month_order)

print("--- 2. Monthly Temperature ---")
print(monthly_avg.round(2))
print("\nSaving monthly bar plot as 'monthly_average_temp.png'...")

# Reset chart layout size using modern rcParams instead of .figure()
plt.clf()
plt.rcParams['figure.figsize'] = [10, 5]

ax = sns.barplot(x=monthly_avg.index, y=monthly_avg.values, hue=monthly_avg.index, palette="coolwarm")
if ax.get_legend() is not None:
    ax.get_legend().remove()

plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_average_temp.png')


# ==========================================
# 3. Highs and Lows
# ==========================================
print("\n--- 3. Highs and Lows ---")
hottest_day = df.loc[df[temp_col].idxmax()]
coldest_day = df.loc[df[temp_col].idxmin()]

print("🔥 Hottest Day Info:")
print(hottest_day.to_frame().T)
print("\n❄️ Coldest Day Info:")
print(coldest_day.to_frame().T)
print("\n")


# ==========================================
# 4. Temperature Trends & Seasons
# ==========================================
print("--- 4. Temperature Trends ---")
print("Saving overall temperature trend line graph as 'temperature_trends_over_time.png'...")

plt.clf()
plt.rcParams['figure.figsize'] = [12, 5]
plt.plot(df[date_col], df[temp_col], color='teal', linewidth=1)
plt.title('Temperature Changes Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.tight_layout()
plt.savefig('temperature_trends_over_time.png')

# b. Seasonal Average Temperature
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['Season'] = df[date_col].dt.month.map(get_season)
season_order = ['Spring', 'Summer', 'Fall', 'Winter']
seasonal_avg = df.groupby('Season')[temp_col].mean().reindex(season_order)

print("\nSeasonal Average Temperature:")
print(seasonal_avg.round(2))
print("\nSaving seasonal line plot as 'seasonal_average_temp.png'...")

plt.clf()
plt.rcParams['figure.figsize'] = [8, 5]
plt.plot(seasonal_avg.index, seasonal_avg.values, marker='o', color='darkorange', linewidth=2, markersize=8)
plt.title('Seasonal Average Temperature')
plt.xlabel('Season')
plt.ylabel('Average Temperature')
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.savefig('seasonal_average_temp.png')

# Rotate the dates on the bottom so they don't overlap
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 1. Save the chart as a permanent image file first
plt.savefig("hottest_days_chart.png")

# 2. Show the chart in a pop-up window on your screen next
plt.show()

# 3. Clean up the background memory after the window is closed
plt.close()

print("\n🎉 Weather chart saved AND displayed successfully!")