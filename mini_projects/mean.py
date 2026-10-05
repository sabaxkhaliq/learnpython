import statistics

def main():
    list_num = [21 , 35, 2, 89, 16, 78, 61, 91, 17]
    data = statistics.mean(list_num)
    print("The mean value is :: ", data) 

if __name__ == "__main__":
    main()