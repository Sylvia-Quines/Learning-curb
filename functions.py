def my_function ():
    a = "She didn't come"
    print(a)
    
age = 23
time = 5
if time <= 6:
    my_function()
else:
    print("She was available")
    
def fahrenheit_to_celsius(fahrenheit):
   celsius = (fahrenheit - 32) *5 / 9
   return celsius #Return stops excuting and sends the result.

print(fahrenheit_to_celsius(43))

def m_greeting():
    return ("Hello sir, goodmorning!")

print(m_greeting())

def identity_info(fname): #fname is a parameter. Parameter is an information that is passed into a functon
    print(fname + " Asare")
    
identity_info("Ennin")
identity_info("Esther")

def my_func():
    pass  #Pass is used when the function placeholder created has no code.

def my_details(name):#name is a parameter
    print("This is my name: " + name) 

my_details("Sylvia Quines")

def my_details(name, age):
    print("This is my name: " + name)
    print(f"I am {age}")

my_details("Sylvia Quines", 65)
my_details("John Doe", 76)


def student_details(name, index):
    print(f"{name.strip().upper()} {index}")

student_details(input("Enter your name: "), input("Enter your index number: "))

#Default parameters: when the function is acalled without any assigned argument it uses the deafualt value
def origin(country = "Norway"):
    print("I am from ", country)
    
origin("Germany")
origin()

#Keyword Arguments
def my_function(animal, name):
    print("Ï have a ", animal)
    print("My ", animal + "'s name is ", name)
    
my_function(animal= "cat", name= "Chuck")


def my_function(fruits):
   for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Returning values
def second_func(x , y):
    return x + y

results = second_func(3,6)
print(results)

#Returns a tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)