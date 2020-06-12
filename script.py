def ground_shipping(weight):
  if weight <= 2:
    cost = 20.00 + weight * 1.50
  elif 2 < weight <= 6:
    cost = 20.00 + weight * 3.00
  elif 6 < weight <= 10:
     cost = 20.00 + weight * 4.00
  else:
     cost = 20.00 + weight * 4.75
  return cost
  
print(ground_shipping(8.4))

premium_ground_shipping = 125.00 

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif 2 < weight <= 6:
    cost = weight * 9.00
  elif 6 < weight <= 10:
     cost = weight * 12.00
  else:
     cost = weight * 14.25
  return cost

print(drone_shipping(1.5))

def cheap_shipping(weight):
  g_shipping = ground_shipping(weight)
  d_shipping = drone_shipping(weight)

  if  (g_shipping < d_shipping) and (g_shipping < 125.0):
    print("ground shipping is cheapest")
    return g_shipping
  elif (d_shipping < g_shipping) and (d_shipping < 125.0):
    print("Drone shipping is cheapest")
    return d_shipping
  else:
    print("Premium ground shipping is cheapest")
    return premium_ground_shipping

print(cheap_shipping(4.8))
print(cheap_shipping(41.5))
