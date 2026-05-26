# Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# A list with strings, integers and boolean values 
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# Using the list() constructor to make a List: 
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# ACCESSING LIST 
mylist = ["ice cream", "vanilla", "oreo"]
print(mylist[1])
print(mylist[0])
print(mylist[-2])

mylist = ["ice cream", "vanilla", "oreo"]
print(mylist[1:2])
print(mylist[0:2])
print(mylist[0:2])
print(mylist[-2:-1])

if 'ice' in mylist:
    print('It is in!')
    
else:
    print('It is not!') 
    
    
mylist = ["ice cream", "vanilla", "oreo"]
mylist[2] = 'Strawberry'    
print(mylist)

mylist = ["ice cream", "vanilla", "oreo"]
mylist[1:2] = ['mango']
print(mylist)

mylist = ["ice cream", "vanilla", "oreo"]
mylist[1:2] = ['mango', 'water']
print(mylist)

mylist = ["ice cream", "vanilla", "oreo"]
mylist[0:2] = ['water']
print(mylist)
       
#CHANGE ITEM VALUE
myColor = ['red', 'indigo', 'pink', 'blue']
myColor[2] = 'white'       
print(myColor)
       