weight = 1.5
#ground shipping:
if weight <= 2 and weight > 0:
  ground_cost = 20 + (1.50 * weight)
  print("Ground Shipping $ " + str(ground_cost))
elif weight > 2 and weight <= 6:
  ground_cost = 20 + (3.00 * weight)
  print("Ground Shipping $ " + str(ground_cost))
elif weight > 6 and weight <= 10:
  ground_cost = 20 + (4.00 * weight)
  print("Ground Shipping $ " + str(ground_cost))
elif weight > 10:
  ground_cost = 20 + (4.75 * weight)
  print("Ground Shipping $ " + str(ground_cost))
else:
  print("Invalid Weight")
#Premium Ground Shipping
premium_ground_cost = 125.00
print("Premium Ground Shipping $ " + str(premium_ground_cost))

#Drone Shipping
if weight <= 2 and weight > 0:
  drone_cost = 4.50 * weight
  print("Drone Shipping $ " + str(drone_cost))
elif weight > 2 and weight <= 6:
  drone_cost = 9.00 * weight
  print("Drone Shipping $ " + str(drone_cost))
elif weight > 6 and weight <= 10:
  drone_cost = 12.00 * weight
  print("Drone Shipping $ " + str(drone_cost))
elif weight > 10:
  drone_cost = 14.25 * weight
  print("Drone Shipping $ " + str(drone_cost))
else:
  print("Invalid Weight")
