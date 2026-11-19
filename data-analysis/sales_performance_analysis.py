daily_sales = [120, 250, 180, 90, 300, 150, 210]
total = sum(daily_sales)
average = total / len(daily_sales)
highest = max(daily_sales)
lowest = min(daily_sales)

print("------ WEEKLY SALES REPORT ------")
print("\n[Daily Sales: 120, 250, 180, 90, 300, 150, 210]")

print(f"\nTotal weekly sales: ${total}")
print(f"Average weekly sales: ${average:.2f}")

print(f"\nHighest sales: ${highest}")
print(f"Lowest sales: ${lowest}")

sales_over_200 = sum(1 for sale in daily_sales if sale > 200)
print(f"\nSales above $200: {sales_over_200}")

sales_below_150 = sum(1 for sale in daily_sales if sale < 150)
print(f"Sales below $150: {sales_below_150}")
