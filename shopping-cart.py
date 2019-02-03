#shopping-cart.py

import datetime
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ]

#for p in products:
#   print(p)

#x = 1 #counter variable
#x = 2 + 1
#x = x + 1

#while x < 5:
#    x = input("Please input a product id: ")
#    print(x)
#    x = x + 1

#x = 1

#running_total = 0 



#while x < 5: 
#    product = {
#        "id":1,
#        "name": "Chocolate Sandwich Cookies",
#        "department": "snakcs",
#        "aisle": "Cookies cakes",
#        "price": 3.50
#}





#print("THE TOTAL PRICE IS: " + str(running_total))

idnum_L = []
sum_price = 0

while True:
    idnum = input("Please enter your product identifier (DONE if you do not have another product): ")
    if idnum == "DONE":
        break
    else:
        #match_prods = [p for p in products if str(p["id"]) == str(idnum)]
        #match_prods = match_prods[0]
        #sum_price = sum_price + match_prods["price"]
        #print("The product you have selected is: " + match_prods["name"] + " " + str(match_prods["price"]))
        idnum_L.append(idnum)




#for idnum in idnum_L:
    #match_prods = [p for p in products if str(p["id"]) == str(idnum)]
    #match_prods = match_prods[0]
    #sum_price = sum_price + match_prods["price"]
    ######print("The product you have selected is: " + match_prods["name"] + " " + str(match_prods["price"]))
        
        
######print("The Total Price is: " + str(sum_price))


#price_round = {0:.2f}.format(idnum["price"])


print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("---------------------------------")
time = datetime.datetime.now()

a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")
d = time.strftime("%I")
e = time.strftime("%M")
f = time.strftime("%p")

print("CHECKOUT AT: " + a + "-" + b + "-" + c + " " + d + ":" + e + " " + f)


print("---------------------------------")
print("SELECTED PRODUCTS:")
for idnum in idnum_L:
    match_prods = [p for p in products if str(p["id"]) == str(idnum)]
       
    match_prod_prime = match_prods[0]
    
    price_round = " (${0:.2f})".format(match_prod_prime["price"])
    
 
    sum_price = sum_price + match_prod_prime["price"]
    print("... " + match_prod_prime["name"] + " " + str(price_round)) #str(match_prods["price"])) # str(price_round)

print("---------------------------------")



tax = sum_price * .06
Total = tax + sum_price

Alpha = " {0:.2f}".format(tax)

Beta = " {0:.2f}".format(Total)

print("SUBTOTAL: $" + str(sum_price))
print("TAX: $" + Alpha)
print("TOTAL: $" + Beta)

print("---------------------------------")

print("THANKS, SEE YOU AGAIN SOON!")

print("---------------------------------")
