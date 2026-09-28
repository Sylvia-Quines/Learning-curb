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
    
    
#Combining the logical operators
age = 30
is_student = False
has_index = True
if (age > 20 or age > 35) and not is_student or has_index:
    print('Should have index.')
 
level = 200   
student_id = "23gh"
password = "1234"

if level > 200 and student_id and password:
    print("Can login to portal!")
else:
    print("Get id and password!")


#The inner if statement  will only execute if the outer  if expression is correct.
c = 23

if c > 20:
    print('Above it')
    if c > 25:
        print ('Right!')
    else:
        print('Try again!')  

age = 29
has_passport = True

if age >= 20:
    if has_passport:
        print("You can travel!")
    else:
        print("You can't drive!")
else:
    print("You are too young to travel!")
    

score = 70
attendance = 20
submitted_project = True

if score >= 70:
    if attendance > 15:
        if submitted_project:
            print("Congratulations, you have graduated!")
        else:
            print("You have to submit project before you can graduate.")
    else:
        print("Your attendace is not complete")
else:
    print("You are not eligible to graduate!")
    
    
#The above can be simplefied as:
score = 70
attendance = 20
submitted_project = True

if score >= 70 and attendance == 20 and submitted_project:
    print("Congratulations you can graduate!")
    


username = 'Sylvia Quines'
password = 'quines123'
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful!")
        else:
            print("Account not found!")
    else:
        print("Password required!")
else:
    print("username required!")
    
#OR    
username = 'Sylvia Quines'
password = 'quines123'
is_active = True

if username and password and is_active:
    print("Login sucessful")
else:
    print("Account not found!")    


#PASS STATEMENT (used to prevent getting errors for empty if statements)
age = 30
lenght = 3.6

if age > lenght:
    pass


day = 5
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday") 


#_ as the default match
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
    

# | checks multiple values in one case   
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    

