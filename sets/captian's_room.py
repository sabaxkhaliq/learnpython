# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
list_rooms = list(map(int, input().split()))

unique_room = set(list_rooms)

captian_room = ((sum(unique_room) * k ) - (sum(list_rooms) )) // (k - 1)
print(captian_room)


# k=int(input())
# s=list(map(int,input().split()))
# c=set(s)
# cap=((sum(c)*k)-sum(s))//(k-1)
# print(cap)