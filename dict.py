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