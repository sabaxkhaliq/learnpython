def cube(n):
    
    z = n * n * n
    return z
    
def main():
    num = int(input("Enter the Number :: "))
    result = cube(num)
    print("Cube is :: ", result)
    
if __name__ == "__main__":
    main()