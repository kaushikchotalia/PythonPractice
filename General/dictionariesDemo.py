my_dict = {'key1':'value1','key2':'value2'}

print(my_dict['key1'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.99}

print(prices_lookup['apple'])

d = {'k1':123, 'k2':[1,2,3,4],'k3':{'insideKey':100}}

print(d['k2'])
print(d['k2'][2])
print(d['k3']['insideKey'])

d1 = {'k4':['a','b','c','d']}

print(d1['k4'][2].upper())

#add new key pair in dictionary

d2 = {'k5':100, 'k6':200}
d2['k7'] = 300
print(d2)

# Update existing value
d2['k5'] = 'NEW VALUE'
print(d2)

print(d2.keys())
print(d2.values())
print(d2.items())