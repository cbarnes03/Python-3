lovely_loveseat_description = " Lovely Loveseat. Tufeted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or White."
stylish_settee_description = " Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "
luxurious_lamp_description = " Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15
sales_tax = 0.088

customer_one_total = 0              #Initialize customer 1 total
customer_one_itemization = ""       #Initialize customer 1 list
customer_one_total += lovely_loveseat_price   #add price to total
customer_one_itemization += lovely_loveseat_description   #add descrip to list
customer_one_total += luxurious_lamp_price #add price to total
customer_one_itemization += luxurious_lamp_description #add descrip to list
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items: " + customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

