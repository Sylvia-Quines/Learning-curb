thistuple = ('Yaw', 'Akwasi', 'Prince', 'Mark')
print(thistuple)
print(len(thistuple))

fruits = ('apple',) #you have to add a comma when you create a tupple with one item else python will not recognize as a tuple 
print(type(fruits))

#Tuple items can be of any data type 
tuple1 = (1,2,3,4,5,6,7)
tuple2 = ('apple','banana', 'mango')
tuple3 = ('True', 'False', 23)
print(type(tuple3))

#The Tuple constructor
thisExample =tuple(('apple','banana', 'mango'))
print(thisExample)

#ACCESS TUPLE ITEMS
thisExample =tuple(('apple','banana', 'mango'))
print(thisExample[1])
print(thisExample[2])
print(thisExample[-1])


tuple1 = (1,2,3,4,5,6,7)
print(tuple1[2:5])
print(tuple1[:4])
print(tuple1[-5:-1])

if 1 in tuple1:
    print('Yes it is!')

#UPDATE TUPLES
tuple1 = (1,2,3,4,5,6,7)
tu2 = list(tuple1)
tu2[2] = 9 
tuple1 = tuple(tu2)
print(tuple1)
   
tuple2 = ('apple','banana', 'mango')
tu1 = list(tuple2)
tu1[0] = 'strawberry'
tuple2 = tuple(tu1)
print(tuple2)

tuple2 = ('apple','banana', 'mango')
tu3 = list(tuple2)
tu3.append('lime')
tuple2 = tuple(tu3)
print(tuple2)

tuple2 = ('apple','banana', 'mango')
tuple1 = (1,2,3,4,5,6,7)
tuple2 += tuple1
print(tuple2)

tuple2 = ('apple','banana', 'mango')
tu3 = list(tuple2)
tu3.remove('apple')
tuple2 = tuple(tu3)
print(tuple2)

tuple2 = ('apple','banana', 'mango')
del tuple2
print(tuple2)

