

def add(first , second):
    sum = first + second
    print("Sum of the Numbers is :: ", sum)


def subtract(first , second):
    sub = first - second
    print("Subtract of the Numbers is :: ", sub)


def multiplication(first , second):
    multiply = first * second
    print("Multiplication of the Numbers is ::", multiply)


def division(first , second):
    if second != 0:
        divide = first / second
        print("Division of the Numbers is :: ", divide)
    else:
        print ("The Second input is Not Valid")




def main():
    
    while(1):
        first = int(input("Enter the Number :: "))
        second = int(input("Enter the Number :: "))

        print("1. Addition \n2. Subtraction \n3. Multiplicaton \n4. Divide \n5. Modulus \n6. Exit")
        num = int(input("Enter Your Choice ::"))

        
        if num == 1:
            add(first, second)
            
        elif num == 2:
            subtract(first, second)

        elif num == 3:
            multiplication(first, second)

        elif num == 4:
            division(first, second)

        elif num == 5:
            modulus(first, second)

        elif num == 6:
            print("Program Exit")
            exit()

        else :
            print("Invalid Choice")
        
if __name__ == "__main__":
    main()

