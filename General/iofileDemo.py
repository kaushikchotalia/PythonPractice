myfile = open('test.txt')

print(myfile.read())

myfile.seek(0)
print('---------------------------------------------------------')
contents = myfile.read()
print(contents)
print('---------------------------------------------------------')
myfile.seek(0)

print(myfile.readlines())
print('---------------------------------------------------------')
myfile.seek(0)

print(myfile.readline())

myfile.close()



with open('test1.txt', mode='a') as f:
    f.write('\nFOUR on FOURTH')

my_new_file = open('test1.txt')
print(my_new_file.read())
my_new_file.close()

file2 = open('test3.txt', mode='w')
file2.write('I CREATED THIS FILE')
#same can be written as
with open('test4.txt', mode='w') as f1:
    f1.write('I CREATED THIS file')