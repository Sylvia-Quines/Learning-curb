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

myColor = ['red', 'indigo', 'pink', 'blue']
myColor[1:3] = ['white', 'black']       
print(myColor)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)       


myColor = ['red', 'indigo', 'pink', 'blue']
myColor.insert(1, 'green')      
print(myColor)

#ADD ITEMS
myColor = ['red', 'indigo', 'pink', 'blue'] 
myColor.append('grey') #Append - add items to the end of the list
print(myColor)

myColor = ['red', 'indigo', 'pink', 'blue'] 
thislist = ["apple", "banana", "cherry"]# EXTEND - add two lists
thislist.extend(myColor)
print(thislist)

#EXTEND can add list and tuple,set and dict.together
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

myColor = ['red', 'indigo', 'pink', 'blue'] 
myColor.remove('red')
print(myColor)

myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
myColor.remove('indigo')
print(myColor)


myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
myColor.pop(1)
print(myColor)
