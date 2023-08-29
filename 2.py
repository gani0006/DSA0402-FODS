import numpy as np

sales_data = np.array([[10, 20, 15],
                       [30, 25, 40],
                       [15, 10, 5]])

average_price_per_product = np.mean(sales_data, axis=0)


average_price_total = np.mean(average_price_per_product)

print("Average price per product:", average_price_per_product)
print("Average price of all products:", average_price_total)
