from arrayDictionary import arrayDictionary as dict

#initialization of dictionary and tests isEmpty
a = dict()
print('Is empty? ' + str(a.isEmpty()))

#tests put method (1,2,3) and size method
a.put('one', 1)
a.put('two', 2)
a.put('three', 3)
print('Size: ' + str(a.size()))

#tests remove and contains
print('Removing key/element at two:' + str(a.remove('two')))
print('Does the dict contain key of three? ' + str(a.contains('three')))

#tests the get values and get keys methods,
#also checks if previous methods have worked
print('Values: ' + str(a.get_values()))
print('Keys: ' + str(a.get_keys()))