sales = {
    "January": 12500,
    "February": 14800,
    "March": 11200,
    "April": 16700,
    "May": 18500,
    "June": 15300,
    "July": 21000,
    "August": 19500
}

print("------ ======== SALES ANALYSIS REPORT ========")

total_sales = sum(sales.values())
average_sales = total_sales / len(sales.values())
print(f"\nTotal Sales: {total_sales:,.2f}")
print(f"Average monthly Sales: ${average_sales:,.2f}")

#Find the Best month in sales
best_month = max(sales, key=sales.get)
best_sales = sales[best_month]
print(f"\nBest month: {best_month} - ${best_sales:,.2f}")

#Find the worst month in sales
worst_month = min(sales, key=sales.get)
worst_sales = sales[worst_month]
print(f"Worst month: {worst_month} - ${worst_sales:,.2f} ")

#calculate the difference between the best month and the worst
print(f"\nSales difference: ${(best_sales - worst_sales):,.2f}")

print("\n===========================================")


