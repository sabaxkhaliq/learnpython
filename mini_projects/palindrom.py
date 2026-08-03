# Palindrom Checker 

words = input("Enter a word :: ")
reverse = ""

for character in words:
    reverse = character +  reverse
    
if reverse == words:
    print(f"The Word {words} is Palindrom...")
else:
    print(f"The Word {words} is Not Palindrom")