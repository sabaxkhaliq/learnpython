

def add_set(sets):

    new_set = {1, 2, 3, 4, 5}
    print(new_set)
    elemet = input("Enter the Element ::")

    sets.add(elemet)
    print(sets)

    print("Set Added Successfully")
    return sets

def remove_set(sets):
    var = input("Enter the Element :: ")
    if var in sets:
        sets.remove(var)
        print("Removed Sucessfully...")


def clear_set(sets):
    sets.clear()
    print("Sets Cleared....")

def main():

    sets = set()
   
    while True:
        print("\nMenu")
        print("1.Add set\n 2.Remove set\n 3.Clear set\n 4.Exit")

        choice = int(input("Enter The Choice :: "))
        

        if choice == 1:
            sets = add_set(sets)

        elif choice == 2:
            remove_set(sets)

        elif choice == 3:
            clear_set(sets)
        
        elif choice == 4:
            print("------EXIT")
            exit()
        else:
            print("Invalid Choice.......")

if __name__ == "__main__":
    main()