lines = []
print("Enter a sequence of lines (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == '':
        break
    lines.append(line)
    
for line in lines:
    print(line.upper())
