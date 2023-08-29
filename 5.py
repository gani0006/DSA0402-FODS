import numpy as np


fuel_efficiency = np.array([25, 30, 28, 22, 35, 27, 29, 31])


average_fuel_efficiency = np.mean(fuel_efficiency)


model1_efficiency = fuel_efficiency[0]  
model2_efficiency = fuel_efficiency[3]  
percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100

print("Average fuel efficiency:", average_fuel_efficiency, "MPG")
print("Percentage improvement between Model 1 and Model 2:", percentage_improvement, "%")
