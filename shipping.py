
def calculateShipping(weight,shipping_type):
    while True: #Allows us to rerun if there's an invalid ship type
        if(shipping_type.lower() == 'ground'):
            if (int(weight)) <=2:
                cost = (int(weight)) * 1.5 + 20
            elif (int(weight)) >2 and (int(weight)) <= 6:
                cost = (int(weight)) * 3 + 20
            elif (int(weight)) >6 and (int(weight)) <= 10:
                cost = (int(weight)) * 4 + 20
            else:
                cost = (int(weight)) * 4.75 + 20
            return cost
        elif (shipping_type.lower()=='drone'):
            if (int(weight)) <=2:
                cost = (int(weight)) * 4.50
            elif (int(weight)) >2 and (int(weight)) <= 6:
                cost = (int(weight)) * 9
            elif (int(weight)) >6 and (int(weight)) <= 10:
                cost = (int(weight)) * 12
            else:
                cost = (int(weight)) * 14.25
                return cost
        elif(shipping_type.lower()=='premium ground'):
            cost=125
            return cost
        else:
            shipping_type=input('Invalid shipping type. Would you like ground shipping or drone shipping? Please enter ground, premium ground, or drone. ')
            continue
        


#Initial greeting, weight input, and shipping type selection
response = input("Welcome! Would you like to ship a package today? Please enter yes or no.")  
if response == "yes": 
    weight = input("Great! Please enter the weight of your package.")
    shipping_type = input("Would you like ground shipping or drone shipping? Please enter ground, premium ground, or drone.")
    print('Your total is',calculateShipping(weight, shipping_type),'dollars')
elif response == "no":
    print ("Thank you! Please come again.")
    exit()
else:
    print ("Invalid response. Please try again.")
    exit()


