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

myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
del myColor[2]
print(myColor)

myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
del myColor


myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
myColor.clear()
print(myColor)


#LOOP THROUGH A LIST
myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
for x in myColor:
    print(x)
    
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

myColor = ['red', 'indigo', 'pink', 'blue', 'indigo']     
x = 0 # set counter variable starting from 0
while x < len(myColor):  # x<3 so loop runs
    print(myColor[x]) # print the current item
    x = x + 1 # increment the counter so the loop moves to the next item


myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] 
[print (x) for x in myColor]

myColor = ['red', 'indigo', 'pink', 'blue', 'indigo'] #creates a list
newBatch = [] #creates a new empt list
for x in myColor: #loop through myColor
    if 'i' in x: # check if there is i in the items
        newBatch.append(x) #add to the new list
        
print(newBatch)  

myColor = ['red', 'indigo', 'pink', 'blue', 'indigo']
newColor = []
i = 0
while i < len(myColor):
    if 'a' in myColor[i]:
        newColor.append(i)
    i = i + 1
print(newColor)        


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)    

naMes = ['Yaw', 'Shack', 'Ama', 'Bernice', 'Esther', 'Comfort']
naMes.sort()
print(naMes)

aGes = [132, 5634, 876, 34, 100, 865, 453, 234, 333, 564]
aGes.sort()
print(aGes)


aGes = [132, 5634, 876, 34, 100, 865, 453, 234, 333, 564]
aGes.sort(reverse= True)
print(aGes)

naMes = ['Yaw', 'Shack', 'Ama', 'Bernice', 'Esther', 'Comfort']
naMes.sort(reverse=True)
print(naMes)