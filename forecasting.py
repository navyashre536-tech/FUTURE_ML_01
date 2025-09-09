# forecasting.py

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet   # install with: pip install prophet

# Load dataset
data = pd.read_csv("datasales.csv")

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])

# Prophet requires columns: ds (date), y (value)
df = data.rename(columns={'Date': 'ds', 'Sales': 'y'})

# Build Prophet model
model = Prophet(daily_seasonality=True, yearly_seasonality=True)
model.fit(df)

# Create future dataframe for next 6 months (180 days)
future = model.make_future_dataframe(periods=180, freq='D')

# Forecast
forecast = model.predict(future)

# Plot forecast
fig1 = model.plot(forecast)
plt.title("Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("forecast_trend.png")

# Plot seasonality
fig2 = model.plot_components(forecast)
plt.savefig("forecast_seasonality.png")

print("✅ Forecast completed! Plots saved as 'forecast_trend.png' and 'forecast_seasonality.png'")
