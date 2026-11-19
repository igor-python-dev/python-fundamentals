print("====== QUARTERLY SALES REPORT ======")
print("")
sales = {
    "January": 12500,
    "February": 14800,
    "March": 11200
}
for month, value in sales.items():
    print(f"{month}: ${value:,.2f}")

total_sales = sum(sales.values())
print(f"\nTotal Sales: ${total_sales:,.2f}")

average_sales = total_sales / len(sales.values())
print(f"Average Monthly Sales: ${average_sales:,.2f}")


difference = sales["March"] - sales["January"]
sign = "-" if difference < 0 else ""
print(f"\nJanuary to March difference: {sign}${abs(difference):,.2f}")

#Sales change
sales_change = ((sales["March"] - sales["January"]) / sales["January"]) * 100
print(f"Sales change: {sales_change:,.2f}%")

print("\n====== END OF REPORT ======")

