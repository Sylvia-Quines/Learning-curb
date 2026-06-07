thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])


#ONLY ONE OF THE SAME VALUES WILL BE PRINTED
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

mydict = dict(name = 'Yaw', age = 23, height = 34, gender = 'male')
print(mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
x = thisdict["brand"]
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
#ACCESS ITEMS
x = thisdict.get("year")
y = thisdict.keys()
print(x)
print(y)

thisdict['car']= 'Toyota'
print(y)
g = thisdict.values()
print(g)
v = thisdict.items()
print(v)

if 'model' in thisdict:
  print('Yes "model" is present!')
  
 
 
 #CHANGE ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
thisdict["car"] = 'Ford'
thisdict.update({'year' : 3485})
c = thisdict.items()
print(c)

#ADD ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
thisdict['color'] = 'green'
print(thisdict)
thisdict.update({'color': 'blue'})
print(thisdict)

#REMOVE ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  
}
thisdict.pop('year')
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  
}
for x in thisdict:
  print(x)
  
for x in thisdict.keys():
  print(x)  
  
for x in thisdict.values():
  print(x)  
  
for x, y in thisdict.items():
  print(x,y)  
  
#COPY DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  
}
mydict = thisdict.copy()
print(mydict)  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  
}

yourdict = dict(thisdict)
print(yourdict)