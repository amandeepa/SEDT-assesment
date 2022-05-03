#create food oreder system

def foodorderingsystem():
    print("Welcome to eat with aman")
    print("Please select the food option below:")
    print("Pepperoni Pizza")
    print("Burger")
    print("Exit The Program")
restaurant=["Awesome pizza place", "wild burer"]
price=[20, 15]

foodorderingsystem()
order=[]
option= input("enter your option:").capitalize()
while option !="exit the program":
    if option == "Pepperoni pizza":
        order.append(option)
        print(restaurant[0], ",", "Pepperoni pizza", ",", "$",price[0] )
        break
    elif option == "Burger":
            print(restaurant[1],",", "burger", ",", "$", price[1])
            break
    else:
         print("invalid option. ")
         foodorderingsystem()
         break

