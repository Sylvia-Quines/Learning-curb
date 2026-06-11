a = 30
b = 20
if a > b:
    print("You are right!")
    
Age = 52
if Age > 50:
    print("You are allowed")
    print('You are respected.')
    print('You caanot drink.')
       
is_legal  = True
if is_legal:
    print('You can vote.')           


q = 23
x = 66
if q > x:
    print("Try again!")
elif x > q:        
    print("Finally")
    
score = 80

if score >= 100:
    print('GRADE A')
elif score >= 75:
    print("GRADE B")    
elif score >= 50:
    print('GRADE C')   
    
day = 6

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")             
elif day == 3:
    print("Wednesday") 
elif day == 4:
    print("Thursday") 
elif day == 5:
    print("Friday") 
elif day == 6:
    print("Saturday") 
elif day == 7:
    print("Sunday")                     
    
a =  4
d = 34
if a == d:
    print('It is less')  
elif a > d:
    print('Try again')    
else:
    print('b is greater than a')     
    
a = 30
b = 20
if a > b:
    print("You are right!")
else:
    print('It is not!')
    
username = 'Adwoa'
if len(username) > 0:
    print(f'Welcome, {username}!')
else:
    print('Username cannot be empty.')         


#SHORTHAND IF...ELSE
a = 23
n= 32
print('Yes') if n > a else print('Oh no.')    #This is called a conditional expression or a ternary operator


a = 23
n= 32
b = a if a > n else n
print('Bigger is', b)

#LOGICAL OPERATORS
a = 230
b = 120
c = 324
if a > b and c > a:  # And prints true if both statements are true
    print('You are right')

a = 230
b = 120
c = 324
if a > b or c < a:  # OR prints true if at least one of the statements is true
    print('You are right')
    
    
a = 33
b = 120
if not a > b:  #Not operator prints the reverse of the result
    print("The result will be a reverse of the correct answer")        
    
    
    
    
    
    