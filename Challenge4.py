#create food oreder system

def foodorderingsystem():
    print("Welcome to eat with treat")
    
    print("Please select the food option below:")
    
    print("Pepperoni Pizza")
    
    print("Burger")
    
    print("Exit\n")
    
restaurant=["Awesome pizza place", "Wild Burger"]
price=[20, 15]

foodorderingsystem()

option= input("Please enter your option:\n ").capitalize()
while option!= "Exit":
    if option == "Pepperoni pizza":
        print("Your order detail are mentioned below':\n")
        print("Restaurant:", restaurant[0], ",", "Food option: Pepperoni pizza", ",", "price: $",price[0] )
        break
    elif option == "Burger":
        print("Your order detail are mentioned below:\n")
        print("Restaurant:", restaurant[1],",", "Food option: Burger", ",", "Price: $", price[1])
        break
    
    else:
        print("Invalid option")
    print()
    foodorderingsystem()
    option= input("Please enter your option:\n ").capitalize()
print()
print("Thank You for using our systen for food order.Have good day")
    



    

