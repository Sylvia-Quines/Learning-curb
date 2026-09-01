Girls = ["Adwoa", "Sandy", "Doreen"]

#Accessing the elements of an array
u = Girls[1]
print(u)

#Modifying array
Girls[2] = "Selena"
Girls[1] = "Sheila"
print(Girls)

d = len(Girls) #This gets the length of the array
print(d)


#Lopping through arrays

for t in Girls:
    print(t)

Girls.append("Faith") 
print(Girls)

Girls.pop(1)
print(Girls)

Girls.reverse()
print(Girls)