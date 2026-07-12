# union of sets

num = int(input())
eng = set(input().split())

num2 = int(input())
fre = set(input().split())

inters = eng.union(fre)
total = len(inters)
print(total)

# intersction of sets

num = int(input())
eng = set(input().split())

num2 = int(input())
fre = set(input().split())

inters = eng.intersection(fre)
total = len(inters)
print(total)

