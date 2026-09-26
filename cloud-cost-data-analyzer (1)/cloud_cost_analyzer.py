import pandas as pd
import matplotlib.pyplot as plt

# Load the sample cloud-cost dataset
df = pd.read_csv("cloud_costs.csv")

# Basic data checks
print("=== Cloud Cost Analytics ===")
print(f"Rows analyzed: {len(df)}")
print(f"Missing values: {df.isna().sum().sum()}")

# Overall cost
total_cost = df["cost_usd"].sum()
print(f"Total cost: ${total_cost:,.2f}")

# Cost by service
cost_by_service = (
    df.groupby("service")["cost_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCost by service:")
print(cost_by_service)

# Cost by department
cost_by_department = (
    df.groupby("department")["cost_usd"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCost by department:")
print(cost_by_department)

# Monthly cost
monthly_cost = (
    df.groupby("month")["cost_usd"]
    .sum()
)

print("\nMonthly cost:")
print(monthly_cost)

# Highest-cost service
highest_service = cost_by_service.idxmax()
highest_service_cost = cost_by_service.max()
print(
    f"\nHighest-cost service: {highest_service} "
    f"(${highest_service_cost:,.2f})"
)

# Month-over-month change
monthly_change = monthly_cost.pct_change() * 100
print("\nMonth-over-month change (%):")
print(monthly_change.round(2))

# Create charts
plt.figure(figsize=(9, 5))
cost_by_service.plot(kind="bar")
plt.title("Cloud Cost by Service")
plt.xlabel("Service")
plt.ylabel("Cost (USD)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("cost_by_service.png")
plt.show()

plt.figure(figsize=(9, 5))
monthly_cost.plot(kind="line", marker="o")
plt.title("Monthly Cloud Spending")
plt.xlabel("Month")
plt.ylabel("Cost (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_cloud_cost.png")
plt.show()
