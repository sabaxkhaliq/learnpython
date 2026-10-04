def product(x, y):
    
    z = x * y
    return z

def main():
    a = int(input("Enter the 1 Number :: "))
    b = int(input("Enter the 2 Number :: "))
    result = product(a, b)
    print("Product is :: ", result)

if __name__ == "__main__":
        main()