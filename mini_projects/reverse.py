# reverse the words

words = input("Enter a word :: ")
reverse = ""

for character in words:
    reverse = character +  reverse
print("Your reversed word is :: ", reverse)