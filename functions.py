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
    return "Hello sir, goodmorning!"