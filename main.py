import os
import csv

# File path
file_path = os.path.join("Resources", "sales_data.csv")

total_orders = 0
total_sales = 0.0
products = []
product_sales = {}

# Skip header row and read data
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header= next(csvreader)

    for row in csvreader:
        total_orders += 1
        total_sales += int(row[2])

        product = row[1]

        if product not in products:
            products.append(product)

        if product not in product_sales:
            product_sales[product] = 0
        
        product_sales[product] += int(row[2])
    
    top_product = max(
        product_sales,
        key=product_sales.get
        )

# Analysis
results = []

results.append("Sales Analysis")
results.append(f"------------------------------------------")
results.append(f"Total Orders: {total_orders}")
results.append(f"Total Sales: ${total_sales:.2f}")
results.append(f"------------------------------------------")
results.append("Product List:")
for product in products:
    results.append(product)

results.append(f"------------------------------------------")
results.append("Sales by Product:")
for product, sales in product_sales.items():
    results.append(f"{product}: ${sales}")
    
results.append(f"------------------------------------------")
results.append(f"Top Product: {top_product}")

analysis = "\n".join(results)
# Print to terminal
print(analysis)

# Output to text file
output_path = os.path.join("analysis", "sales_analysis.txt")

with open(output_path, "w") as txt_file:
    txt_file.write(analysis)

print(f"Results saved to {output_path}")