import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/covid_19_clean_complete.csv")

print("\nFirst 5 Rows of Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.fillna(0)

df['Date'] = pd.to_datetime(df['Date'])

country_cases = df.groupby('Country/Region')['Confirmed'].max()

top_10_cases = country_cases.sort_values(ascending=False).head(10)

print("\nTop 10 Countries by Confirmed Cases:")
print(top_10_cases)

plt.figure(figsize=(12,6))

plt.barh(top_10_cases.index, top_10_cases.values)

plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("graphs/confirmed_cases.png")
plt.show()

country_deaths = df.groupby('Country/Region')['Deaths'].max()

country_confirmed = df.groupby('Country/Region')['Confirmed'].max()

death_rate = (country_deaths / country_confirmed) * 100

death_rate = death_rate.sort_values(ascending=False).head(10)

print("\nTop 10 Countries by Death Rate:")
print(death_rate)

plt.figure(figsize=(12,6))

plt.barh(death_rate.index, death_rate.values)

plt.title("Top 10 Countries by Death Rate")
plt.xlabel("Death Rate (%)")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("graphs/death_rate.png")
plt.show()

country_recovered = df.groupby('Country/Region')['Recovered'].max()

recovery_rate = (country_recovered / country_confirmed) * 100

recovery_rate = recovery_rate.sort_values(ascending=False).head(10)

print("\nTop 10 Countries by Recovery Rate:")
print(recovery_rate)

plt.figure(figsize=(12,6))

plt.barh(recovery_rate.index, recovery_rate.values)

plt.title("Top 10 Countries by Recovery Rate")
plt.xlabel("Recovery Rate (%)")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("graphs/recovery_rate.png")
plt.show()

global_trend = df.groupby('Date')['Confirmed'].sum()

print("\nGlobal Trend Data:")
print(global_trend.head())

plt.figure(figsize=(14,6))

plt.plot(global_trend.index, global_trend.values)

plt.title("Global COVID-19 Confirmed Cases Trend")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("graphs/global_trend.png")
plt.show()

df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

active_cases = df.groupby('Country/Region')['Active'].max()

top_active = active_cases.sort_values(ascending=False).head(10)

print("\nTop 10 Countries by Active Cases:")
print(top_active)

plt.figure(figsize=(12,6))

plt.barh(top_active.index, top_active.values)

plt.title("Top 10 Countries by Active Cases")
plt.xlabel("Active Cases")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("graphs/active_cases.png")
plt.show()

print("\nProject Insights:")
print("1. USA, India, and Brazil were among the highest affected countries.")
print("2. Recovery rates improved significantly over time.")
print("3. Some countries had high death rates despite lower confirmed cases.")
print("4. Global confirmed cases increased rapidly during peak pandemic periods.")

print("\nCOVID-19 Data Analysis Completed Successfully!")