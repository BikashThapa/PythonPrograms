from Utils import find_max

numbers = int(input("Enter how many numbers:::"))
numberlists = []
for loop in range(numbers):
    no = int(input("Enter Numbers:"))
    numberlists.append(no)

maximun = find_max(numberlists)

print(f'the numbers list is {numberlists}')
print(f'The maximum number is {maximun}')