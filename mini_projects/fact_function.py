def factorial(n):
    fact = 0
    for i in range(1, n+1):
        fact = fact * i
    return fact
    
def main():
    num = int(input("Enter the Number :: "))
    
    fact_result = factorial(num)
    print("Factorial is :: ", fact_result )
    
if __name__ == "__main__":
    main()