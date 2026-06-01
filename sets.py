mySet = {'food', 'money', 'house', 'shoe', 'bag'}
print(mySet)

mySet = {'food', 'money', 'bag', 'house', 'shoe', 'bag'} #set cannot have duplicates
print(mySet)

#True and 1 are considered the same values in set same as false and 0
thisSet = {True, False, 'Another', 1 ,6}
print(thisSet)

mySet = {'food', 'money', 'house', 'shoe', 'bag'}
print(len(mySet))

#SETS CAN BE OF ANY DATA TYPE
set1 = {1,2,3,4,5,6}
set2 = {'Dog', 'Cat', 'Pig'}
print(type(set1))

mySet = {'food', 'money', 'house', 'shoe', 'bag'}
for x in mySet:
    print(x)
    

mySet = {'food', 'money', 'house', 'shoe', 'bag'}
print('yam' not in mySet)


mySet = {'food', 'money', 'house', 'shoe', 'bag'}
print('money' in mySet)


mySet = {'food', 'money', 'house', 'shoe', 'bag'}
mySet.add('Car')
print(mySet)

set1 = {1,2,3,4,5,6}
set2 = {'Dog', 'Cat', 'Pig'}
set1.update(set2)
print(set1)

