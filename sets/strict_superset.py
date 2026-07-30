# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(int, input().split()))

n = int(input())
set_b = set(map(int, input().split()))

set_c = set(map(int, input().split()))


if set_a.issuperset(set_b):
    if set_a.issuperset(set_c):
        print("True")
    else:
        print("False")
else:
    print("False")
    