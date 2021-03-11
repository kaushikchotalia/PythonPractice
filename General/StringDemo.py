# Strings

# Printing a String

print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')

# We can use this to print a string backwards
s = "Kaushik"
print(s[::-1])


print('\n')
print('This is a String {}'.format('INSERTED'))

print('The {} {} {}'.format('fox','brown','quick'))

print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {0} {0} {0}'.format('fox','brown','quick'))

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

result= 100/700
print("The result was {r}".format(r=result))

#another way of using format
name = "KC"
print(f'Hello, my name is  {name}')