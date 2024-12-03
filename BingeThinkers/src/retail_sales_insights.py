from datetime import datetime, timedelta  # Import timedelta along with datetime
import random

# Sample retail data generation
products = ['T-Shirt', 'Jeans', 'Jacket', 'Sweater']
product_prices = {'T-Shirt': 20.00, 'Jeans': 40.00, 'Jacket': 55.00, 'Sweater': 30.00}
sales_data = []

# Helper function to generate random dates within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)  # Use timedelta to add days

# Function to generate sales data for 500 orders
def generate_sales_data(num_orders):
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    for order_id in range(1, num_orders + 1):
        order_date = random_date(start_date, end_date)
        product = random.choice(products)
        quantity = random.randint(1, 5)
        price = product_prices[product]
        revenue = quantity * price
        sales_data.append((order_id, order_date, product, quantity, price, revenue))

# Generate sales data for 500 orders
generate_sales_data(500)

# Conversion rate from USD to INR
exchange_rate = 83  # 1 USD = 83 INR

# 1. Seasonal Sales Patterns (Monthly Sales in INR)
monthly_sales = {}
for order in sales_data:
    order_date = order[1]
    month = order_date.month
    revenue = order[5] * exchange_rate  # Convert to INR
    if month not in monthly_sales:
        monthly_sales[month] = 0
    monthly_sales[month] += revenue

# Print monthly sales patterns in INR
print("Seasonal Sales Patterns (Monthly Revenue in INR):")
for month, total_revenue in sorted(monthly_sales.items()):
    print(f"Month {month}: ₹{total_revenue:.2f}")

# 2. Top Products by Quantity and Revenue in INR
product_sales = {'T-Shirt': {'quantity': 0, 'revenue': 0},
                 'Jeans': {'quantity': 0, 'revenue': 0},
                 'Jacket': {'quantity': 0, 'revenue': 0},
                 'Sweater': {'quantity': 0, 'revenue': 0}}

for order in sales_data:
    product = order[2]
    quantity = order[3]
    revenue = order[5] * exchange_rate  # Convert to INR
    product_sales[product]['quantity'] += quantity
    product_sales[product]['revenue'] += revenue

# Print top products by quantity and revenue in INR
print("\nTop Products by Quantity and Revenue in INR:")
for product, sales in product_sales.items():
    print(f"{product} - Quantity Sold: {sales['quantity']}, Total Revenue: ₹{sales['revenue']:.2f}")

# 3. Monthly Revenue Trends in INR
monthly_revenue_trends = {}
for order in sales_data:
    order_date = order[1]
    month = order_date.month
    revenue = order[5] * exchange_rate  # Convert to INR
    if month not in monthly_revenue_trends:
        monthly_revenue_trends[month] = []
    monthly_revenue_trends[month].append(revenue)

# Print monthly revenue trends (average revenue in INR for the month)
print("\nMonthly Revenue Trends (Average per Month in INR):")
for month, revenues in sorted(monthly_revenue_trends.items()):
    avg_revenue = sum(revenues) / len(revenues)
    print(f"Month {month}: ₹{avg_revenue:.2f}")
