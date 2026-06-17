i = 1
while i < 6:
    print(i)
    i += 1 # this is the update step, without it i stays at 1 forever and you would have an infinite loop
    
x = 2

while x < 32:
    print(x)
    if x == 30:
        break # loop stops when it gets to 30
    x += 2  
    
    
x = 2

while x < 32:
    x += 1
    if x == 3:
        continue # loop starts when it gets to 4
    print(x)