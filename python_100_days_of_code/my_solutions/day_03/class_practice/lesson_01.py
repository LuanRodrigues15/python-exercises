size = input("Size pizza: S, M or L: ")
pepperoni = input("Pepperoni? Y or N: ")
extra_cheese = input("Extra cheese? Y or N: ")

def price(size, pepperoni, extra_cheese):
    price = 0
    extraP = (pepperoni == "Y") 
    extraC = (extra_cheese == "Y")

    if size == "S":
        price += 15
        if extraP:
            price += 2
    elif size == "M":
        price += 20
    else:
        price += 25

    if size != "S" and extraP:
        price += 3

    if extraC: 
        price += 1

    return(price)

print(f"Price: {price(size, pepperoni, extra_cheese)}")