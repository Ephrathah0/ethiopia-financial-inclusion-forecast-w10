import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Load processed/enriched dataset ---
df = pd.read_csv('../data/processed/processed_data.csv')

# --- Prepare Access & Usage ---
access_df = df[df['pillar'] == 'access'].sort_values('observation_date').copy()
usage_df = df[df['pillar'] == 'usage'].sort_values('observation_date').copy()

# Convert dates
access_df['observation_date'] = pd.to_datetime(access_df['observation_date'])
usage_df['observation_date'] = pd.to_datetime(usage_df['observation_date'])

# Linear trend forecasting
from sklearn.linear_model import LinearRegression

def forecast_pillar(df_pillar, pillar_name):
    df_pillar['year'] = df_pillar['observation_date'].dt.year
    X = df_pillar['year'].values.reshape(-1,1)
    y = df_pillar['value_numeric'].values
    model = LinearRegression()
    model.fit(X, y)
    future_years = np.array([2025, 2026, 2027]).reshape(-1,1)
    forecast = model.predict(future_years)
    return pd.DataFrame({
        'year':[2025,2026,2027],
        f'{pillar_name}_Base': forecast,
        f'{pillar_name}_Optimistic': forecast*1.05,
        f'{pillar_name}_Pessimistic': forecast*0.95
    })

access_forecast_df = forecast_pillar(access_df, 'Access')
usage_forecast_df = forecast_pillar(usage_df, 'Usage')

# Merge forecasts for download
forecast_df = pd.merge(access_forecast_df, usage_forecast_df, on='year')

# --- Streamlit layout ---
st.title("Ethiopia Financial Inclusion Dashboard")
st.markdown("""
Explore Access (Account Ownership) and Usage (Digital Payments) trends in Ethiopia, including forecasts and scenarios.
""")

# Sidebar filters
st.sidebar.header("Filters")
pillar_option = st.sidebar.selectbox("Select Pillar", ["Access", "Usage", "Both"])
years_selected = st.sidebar.slider("Select Years", int(df['observation_date'].dt.year.min()), 2027, (2011,2027))

# Plotting
st.subheader("Observed Data + Forecasts")

plt.figure(figsize=(10,5))
sns.set_style("whitegrid")

if pillar_option in ["Access", "Both"]:
    sns.lineplot(x='year', y='value_numeric', data=access_df, marker='o', label='Access Observed')
    sns.lineplot(x='year', y='Access_Base', data=access_forecast_df, marker='o', label='Access Base Forecast')
    sns.lineplot(x='year', y='Access_Optimistic', data=access_forecast_df, marker='o', linestyle='--', label='Access Optimistic')
    sns.lineplot(x='year', y='Access_Pessimistic', data=access_forecast_df, marker='o', linestyle='--', label='Access Pessimistic')

if pillar_option in ["Usage", "Both"]:
    sns.lineplot(x='year', y='value_numeric', data=usage_df, marker='o', label='Usage Observed')
    sns.lineplot(x='year', y='Usage_Base', data=usage_forecast_df, marker='o', label='Usage Base Forecast')
    sns.lineplot(x='year', y='Usage_Optimistic', data=usage_forecast_df, marker='o', linestyle='--', label='Usage Optimistic')
    sns.lineplot(x='year', y='Usage_Pessimistic', data=usage_forecast_df, marker='o', linestyle='--', label='Usage Pessimistic')

plt.xlim(years_selected)
plt.ylabel("Percentage (%)")
plt.xlabel("Year")
plt.title("Financial Inclusion Trends & Forecasts")
plt.legend()
st.pyplot(plt)

# Data download
st.subheader("Download Forecast Data")
csv = forecast_df.to_csv(index=False)
st.download_button("Download CSV", csv, file_name="ethiopia_fi_forecast.csv", mime="text/csv")
