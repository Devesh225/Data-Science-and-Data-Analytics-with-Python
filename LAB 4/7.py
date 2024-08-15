s = input("Enter a sequence of words: ")
words = s.split()
digitWords = [word for word in words if word.isdigit()]
print(digitWords)
