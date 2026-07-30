a = int(input())
a_set = set(map(int, input().split())) 

b = int(input())
b_set = set(map(int, input().split())) 

unique = sorted(a_set.symmetric_difference(b_set))

for i in unique:
    print(i)


