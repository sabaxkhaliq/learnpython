menu = {
    'Pizza' : 800,
    'Sandwich' : 100,
    'Burger' : 100,
    'Pasta' : 150,
    'Cold Drink' : 90,
    'Coffee' : 50

}

def main():
    print("Welcome to Resturant")
    print(" Pizza : Rs 800\n Sandwich : Rs 100\n Burger : Rs 100\n Pasta : Rs 150 ")
    print(" Cold Drink : Rs 90\n Coffee : Rs 50 ")

    total_order = 0

    item = input("Enter the Name of Item :: ").title()
    if item in menu:
        total_order += menu[item]
        print(f"Your Item {item} has been added ")
    else : 
        print(f"This item {item} is Not Available")

    while(1):
        order = input("Do You Want to add another item (Yes/ No) ")
        if order == "yes":
            items = input("Enter the Name of Item :: ").title()
            if items in menu :
                total_order += menu[items]
                print(f"Your Item {items} has been added ")
            else : 
                print(f"This item {items} is Not Available")
        else :
            print(f"Total Amount of Items is {total_order}")
            exit()

    print(f"Total Amount of Items is {total_order}")

if __name__ == "__main__":
    main()