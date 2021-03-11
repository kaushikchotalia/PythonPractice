myset = set()
myset.add(1)

print(myset)

myset.add(2)
print(myset)

# sets can hold only unique values, even though below entry is added again, the set will still show output {1, 2} instead of {1, 2, 2}
myset.add(2)
print(myset)

my_list = [1,1,1,1,1,1,2,2,2,2,1,3,3,3,3,2,4,4,4,4]
setfrommylist = set(my_list)

print(setfrommylist)

print(set('Mississippi'))