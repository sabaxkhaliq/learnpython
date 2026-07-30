first = int(input("Enter the First Number :: "))
second = int(input("Enter the Second Number :: "))
third = int(input("Enter the Third Number :: "))

if first > second and first > third:
    print("The Largest Number is First ::", first)

elif second > first and second > third :
    print("The Largest Number is Second ::", second)

elif third > first and third > second :
    print("The Largest Number is Third ::", third)

else:
    print("All the Numbers are Equal")