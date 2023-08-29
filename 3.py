import numpy as np

csv_file_path = "D:/FODS/data sets/house_bedroom_sales.csv"
house_data = np.loadtxt(csv_file_path, delimiter=',')


bedrooms_column = house_data[:, 0]  
condition = bedrooms_column > 4
filtered_houses = house_data[condition]


average_sale_price = np.mean(filtered_houses[:, -1])  

print("Average sale price of houses with more than four bedrooms:", average_sale_price)
