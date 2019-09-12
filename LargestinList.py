numbers = [1,21,4234,423432,42345,324]
largest = numbers[0] 

for x in numbers:
    if largest < x:
        largest = x
print(f'The largest value is : {largest}')
