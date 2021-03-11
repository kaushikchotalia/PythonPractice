mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)
    print('Hello')

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(f'Even number: {num}')
    else:
        print(f'Odd number: {num}')


list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)


mystring = 'Hello World'

for letter in mystring:
    print(letter)

tup = (1,2,3)

for item in tup:
    print(item)