def average(array):
    # your code goes here
    height = set(array)
    length = len(height)
    
    arg = sum(height) / length
    return arg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)