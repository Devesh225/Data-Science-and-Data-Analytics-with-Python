s = input("Enter a string: ")
slen = len(s)
print(f"Length of the string: {slen}")
if 'country' in s:
    print("The substring 'country' is found in the input string.")
else:
    print("The substring 'country' is not found in the input string.")

wc = {}
s = s.replace('.', '').replace(',', '').lower()
words = s.split()
for word in words:
    wc[word] = wc.get(word, 0) + 1

print("Occurrences of each word in the string :-")
for word, count in wc.items():
    print(f"{word}: {count}")
