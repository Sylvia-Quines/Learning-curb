# The range() function can be called with 1, 2, or 3 arguments, using this syntax:
#range(start, stop, step). When the argument is one it is the stop argument 
# and the start argument is automatically 0
v = range(1, 10, 1)
x = range(20)
print(x)

# when it has two values the aarguments are start and stop
i = range(2, 22)


#RAnge isoften usedin for loops
for i in range(3,34):
    print(i)
    
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

#slicing range
r = range(10)
print(r[2])
print(r[:3])

#Membership testing

r = range(0, 10, 2)
print(6 in r)
print(7 in r)

#Getting the number of elements in a range
r = range(0, 10, 2)
print(len(r))


