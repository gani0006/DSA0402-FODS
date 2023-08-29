import pandas as pd


order_data = pd.read_csv("D:/FODS/data sets/customer orders.csv")


orders_per_customer = order_data.groupby('customer_id').size()


avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()


earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total number of orders made by each customer:")
print(orders_per_customer)

print("\nAverage order quantity for each product:")
print(avg_order_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
