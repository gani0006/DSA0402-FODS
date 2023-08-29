item_prices = [2.5, 1.0, 3.0, 4.5]  
quantities = [3, 2, 1, 4]            
discount_rate = 10                  
tax_rate = 8                        


total_cost_before_discount = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))
discount_amount = (discount_rate / 100) * total_cost_before_discount


total_cost_after_discount = total_cost_before_discount - discount_amount

tax_amount = (tax_rate / 100) * total_cost_after_discount

final_total_cost = total_cost_after_discount + tax_amount

print("Total cost before discount:", total_cost_before_discount)
print("Discount amount:", discount_amount)
print("Total cost after discount:", total_cost_after_discount)
print("Tax amount:", tax_amount)
print("Final total cost:", final_total_cost)
