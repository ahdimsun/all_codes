import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("transactions.csv")

# Convert timestamp to datetime
df['txn_timestamp'] = pd.to_datetime(df['txn_timestamp'])

# Extract date and month
df['date'] = df['txn_timestamp'].dt.date
df['month'] = df['txn_timestamp'].dt.to_period('M')
df['day'] = df['txn_timestamp'].dt.day

# Aggregate spending per day
daily_spending = df.groupby('date')['amount'].sum().reset_index()
daily_spending['day'] = pd.to_datetime(daily_spending['date']).dt.day
daily_spending['month'] = pd.to_datetime(daily_spending['date']).dt.to_period('M')

# Plot daily spending per month
plt.figure(figsize=(12,6))
for month, group in daily_spending.groupby('month'):
    plt.plot(group['day'], group['amount'], marker='o', label=str(month))

plt.title("Daily Spending Trends per Month")
plt.xlabel("Day of Month")
plt.ylabel("Total Spent")
plt.legend(title="Month")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
