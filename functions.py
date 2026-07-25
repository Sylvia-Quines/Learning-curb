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
