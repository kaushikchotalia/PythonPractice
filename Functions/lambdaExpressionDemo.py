def square(num):
    result = num ** 2
    return result

print(square(3))

# with Lamda expressions - Also knows as anonymous function

mysquare = lambda num: num ** 2

print(mysquare(5))

# Use Lambda function with map
mynums = [1,2,3,4,5,6]
print(list(map(lambda num: num **2,mynums)))

# Use Lambda function with filter
print(list(filter(lambda num: num%2==0,mynums)))