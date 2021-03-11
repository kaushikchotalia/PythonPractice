my_list = [1,2,3]
my_list1 = ['String',100,23.2] # Python list can hol multipe data type items in single list


print(len(my_list))

mylist3 = ['one','two','three']
print(mylist3)
print(mylist3[0])
print(mylist3[1:])

mylist4 = ['four','five','six']

new_list = mylist3 + mylist4
print(new_list)

new_list[0] = 'ONE ALL CAPS'
print(new_list)

#add element in list
new_list.append('SEVEN')
print(new_list)

#remove item in the list from last
popped_item = new_list.pop()
print(popped_item)
print(new_list)
popped_item1 = new_list.pop()
print(popped_item1)
print(new_list)

#remove item in the list by idex
popped_item2 = new_list.pop(0)
print(popped_item2)
print(new_list)

#sort list
new_list1 = ['a','e','x','b','c','d']
num_list = [4,1,5,9,7]

new_list1.sort()
print(new_list1)
num_list.sort()
print(num_list)

#revers a list
new_list1.reverse()
print(new_list1)
num_list.reverse()
print(num_list)