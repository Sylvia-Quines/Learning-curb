# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print('Hello')
print("Hello")

# QUOTES INSIDE QUOTES
print('The pen is Jonny"s')
print("The pen is Jonny's")

a = 'She is his wife'
print(a)


# MULTILINE STRING
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# STRINGS ARE ARRAYS
a = ('She is a student')
print(a[4])
print(3)

# LOOPING THROUGH A STRING
for x in 'She is back':
    print(x)
    
for y in 'I am fine':
    print(y)    

# Geting the length of a string
g = 'When is my mum coming?'
print(len(g))

#CHECK STRING
txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are !"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  
  
  
  
#SLICING
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])  

b = "Hello, World!"
print(b[-2])

b = "Hello, World!"
print(b[3:])

b = "Hello, World!"
print(b[0:])

b = "Hello, World!"
print(b[-5:-2])

# MODIFYING STRINGS

w = 'Come back home!'
print(w.upper())

print(w.lower())

# The strip() removes the whitespaces before and after the text
w = '  Come back home!  '
print(w.strip())

w = 'Come back home!  '
print(w.strip())

w = '  Come back home!'
print(w.strip())

# Replace- replaces a string with another string 
w = '  Come back home!  '
print(w.replace('c', 'k'))  


# The split() method returns a list where the text between the specified separator becomes the list items. 
a = "Hello, World!"
print(a.split(",")) 
  
txt = "apple,banana,mango"
print(txt.split(","))

txt = "2024-05-16"
print(txt.split("-"))

v = 'She is good'  
print(v.split('is'))

# STRING CONCATENATION 
a = 'She'
b = ' went'
print(a+b)


# F-STRING(FORMAT) - TO COMBINE STRINGS WITH NUMBERS 
age = 36
txt = "My name is John, I am " + str(age)
print(txt)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# PLACEHOLDERS(the {} inside an f-string that will be filled when the code runs) & MODIFIERS(an instruction inside the {} that controls how a value is displayed) 
  
price = 400000000
name = 'Rita'
age = 23

print(f'Adwoa is {age}') 
print(f'Change my {price:,}')
print(f'The pice is {price:.2f}')
print(f'The pice is {6 + 7}')

# The escape character allows you to use double quotes when you normally would not be allowed 

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
  
  