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

set1 = {1,2,3,4,5,6}
list1 = ['Dog', 'Cat', 'Pig']

set1.update(list1)
print(set1)

set2 = {'Dog', 'Cat', 'Pig'}
set2.remove('Dog')
print(set2)


#Will not raise an error if the item does not exist but remove will if the item does not exist
set2 = {'Dog', 'Cat', 'Pig'}
set2.discard('mice')
print(set2)


#Will remove a random item
set2 = {'Dog', 'Cat', 'Pig'}
set2.pop()
print(set2)

set2 = {'Dog', 'Cat', 'Pig'}
y = set2.pop()
print(y) #return value is the removed item
print(set2)

#UNION
set1 = {1,2,3,4,5,6}
set2 = {'Dog', 'Cat', 'Pig'}

set3 = set1.union(set2)
print(set3)

set1 = {1,2,3,4,5,6}
set2 = {'Dog', 'Cat', 'Pig'}

set3 = set1|set2
print(set3)

x = {1,2,3,4,5,6}
y = ['Dog', 'Cat', 'Pig']

q = x.union(y)
print(q)
#The | operator allows joining of set and set alone


#INTERSECTION
x = {1,2,3,4,5,6, 'milk'}
y = {'Dog', 'Cat','milk', 'Pig'}

w = x.intersection(y)
print(w)


x = {1,2,3,4,5,6, 'milk'}
y = {'Dog', 'Cat','milk', 'Pig'}

w = x & y
print(w)