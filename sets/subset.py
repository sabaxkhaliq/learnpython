
cases = int(input())

for i in range(cases):
    a = int(input())
    a_set = set(map(int, input().split()))     
    b = int(input())
    b_set = set(map(int, input().split())) 
    c  = a_set.issubset(b_set)
    print(c)