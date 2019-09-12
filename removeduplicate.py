numbers = [11,22,33,11,32,21,22]
new = []
for number in numbers:
    if number not in new:
        new.append(number)

print(new)
