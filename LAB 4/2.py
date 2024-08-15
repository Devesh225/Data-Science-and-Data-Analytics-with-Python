s = input("Enter a comma separated sequence of words: ")
words = s.split(',')
words = [word.strip() for word in words]
words.sort()
s = ', '.join(words)
print(f"Sorted Words: {s}")
