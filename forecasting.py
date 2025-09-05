import pandas as pd
import matplotlib.pyplot as plt

# Example: load sample sales data
# (Later replace 'sales.csv' with your actual dataset in dataset/ folder)
data = pd.DataFrame(
{
    "Date": pd.date_range(start="2023-01-01", periods=30, freq="D"),
    "Sales": [100, 120, 130, 90, 150, 160, 200, 180, 175, 190,
              210, 230, 250, 240, 260, 270, 300, 310, 305, 320,
              330, 340, 360, 370, 380, 390, 400, 410, 420, 430]
}
)

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])

# Plot sales trend
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Sales'], marker='o')
plt.title("Sample Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("sales_trend.png")  # Saves the chart as an image
plt.show()
