myvar = "John"
print(myvar)
my_var = "John"
print(my_var)


_my_var = "John"
print(_my_var)

myVar = "John"
print(myVar)
MYVAR = "John"
print(MYVAR)

myvar2 = "John"
print(myvar2)


# MULTI WORDS VARIABLE NAMES
# CAMEL CASE(Each word except the first start with a capital letter)

myVariableName = 'Jesus'
print(myVariableName)

numberOfIssues = 7
print(numberOfIssues)

# PASCAL CASE(Everyword starts with a capital letter)
MyVariableName = 'She is a good girl'
print(MyVariableName)

NumberOfIssues = 8
print(NumberOfIssues)

# SNAKE CASE(Everyword is separated with an underscore)
my_variable_name = 'Jesus is king'
print(my_variable_name)

number_Of_Issues = 12
print(number_Of_Issues)


# ASSIGNING MULTIPLE VALUES TO MANY VARIABLES

X,Y,Z = 'Orange', 'Banana', 'Cococnut'
print(X)
print(Y)
print(Z)

# ASSIGNING ONE VALUE TO MULTIPLE VARIABLES
S=T=U = 'Car'
print(S)
print(T)
print(U)



S,T,U = 'Car'
print(S)
print(T)
print(U)


# UNPACKING A COLLECTION
Fruits = ['She', 'He', 'Them']
x, y, z = Fruits
print(x)
print(y)
print(z)

# OUTPUT VARIABLES(Print is used to often output variables)
l = 'python is awesome'

# USING , TO OUPUT MULTIPLE VARIABLES WITH PRINT
b = 'Python'
c = 'is'
d = 'awesome'
print(b,c,d)

# USING + TO OUPUT MULTIPLE VARIABLES WITH PRINT
B = 'Python '
C = 'is '
D = 'awesome'
print(B+C+D)

r = 'Ewura is'
s = 7
print(r,7)

# GLOBAL VARIABLES (Variables that are created outside a function)
x = 'awesome'
def myfunc():
    print('Python is ' + x)
    
myfunc() 
print('She is ' + x)

# LOCAL VARIABLES
def myfunc():
    x = 'awesome'
    print('Python is ' + x)
    
myfunc() 

# THE VARIABLE OUTIDE THE FUNCTION STAYS THE SAME 
x = 'awesome'
def myfunc():
    X = 'nice'
    print('Python is ' + X)
    
myfunc() 

def myfunc():
    global y
    y = 'husband'
    print ('Alex is Ewura ' + y)

myfunc()    
    
print("Python is " + y)




x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

