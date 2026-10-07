def square(a):
    b = a * a
    return b
    
def main():
    num = int(input("Enter the Number :: "))
    sq = square(num)
    print("Square is ", sq)

if __name__ == "__main__":
    main()