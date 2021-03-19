#Initial greeting, weight input, and shipping type selection
response = input("Welcome! Would you like to ship a package today? Please enter yes or no.")  
 
if response == "yes": 
    weight = input("Great! Please enter the weight of your package.")
    shipping_type = input("Would you like ground shipping or drone shipping? Please enter ground, premium ground, or drone.")
elif response == "no":
    print ("Thank you! Please come again.")
else:
    print ("Invalid response. Please try again.")

#Ground shipping costs
if (int(weight)) <=2:
    cost_ground = (int(weight)) * 1.5 + 20
elif (int(weight)) >2 and (int(weight)) <= 6:
    cost_ground = (int(weight)) * 3 + 20
elif (int(weight)) >6 and (int(weight)) <= 10:
    cost_ground = (int(weight)) * 4 + 20
else:
    cost_ground = (int(weight)) * 4.75 + 20

ground_ship_premium = 125

# Drone shipping costs
if (int(weight)) <=2:
    cost_drone = (int(weight)) * 4.50
elif (int(weight)) >2 and (int(weight)) <= 6:
    cost_drone = (int(weight)) * 9
elif (int(weight)) >6 and (int(weight)) <= 10:
    cost_drone = (int(weight)) * 12
else:
    cost_drone = (int(weight)) * 14.25


if shipping_type == "ground":
    print ("Your total is", cost_ground, "dollars")
elif shipping_type == "premium ground":
    print ("Your total is", ground_ship_premium, "dollars")
elif shipping_type == "drone":
    print ("Your total is", cost_drone, "dollars")
else:
    print ("Invalid shipping type. Please try again.")