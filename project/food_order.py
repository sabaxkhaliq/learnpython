import json



def load_data():
    with open("food.json", "r") as file:
        data = json.load(file)
        return data
    
def order(item_name , price):
    id = input("Enter Your ID :: ")
    name = input("Enter Your Name :: ")
    quantity = int(input("Enter Quantity :: "))

    bill = price * quantity
    print("Your Bill is :: ", bill)


    data = {
        "id" : id,
        "name" : name,
        "Item" : item_name,
        "price" : price,
        "quantity": quantity,
        "bill": bill
    }
    return data
    
def save_data(data):
    with open("food.json", "w") as file:
        json.dump(data, file, indent=4)



def main ():

    data = load_data() 

    while True:
        print("1.Burger \n  price : 250 ")
        print("2.Pizza \n  price : 800 ")
        print("3.Fries \n  price : 150 ")
        print("4.Cold Drink \n  price : 100 ")
        print("5. Exit")

        choice = int(input("Enter Your Order :: "))

        
        if choice == 1: 
            user_order  = order("Burger", 250)
            data.append(user_order)
            save_data(data)
            
                

        elif choice == 2:
             user_order  = order("Pizza", 800)
             data.append(user_order)
             save_data(data)

                    
        elif choice == 3:
             user_order  = order("Fries", 150)
             data.append(user_order)
             save_data(data)

                
        elif choice == 4:
             user_order  = order("Cold_Drink", 100)
             data.append(user_order)
             save_data(data)


        elif choice == 5:
            print("Good Bye")
            exit()

        else :
            print ("Invalid Choice")


        



if __name__ == "__main__":
    main()




















