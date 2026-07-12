num_student = int(input())
roll_no = set(input().split())

num = int(input())
roll = set(input().split())

total = roll_no.difference(roll)
length = len(total)

print(length)