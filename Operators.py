sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

print(sum1)
print(sum2)
print(sum3)

# ARITHMETIC OPERATORS 
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5

print(x / y)  #returns a float
print(x//y) #returns an integer

# COMPARISON OPERATORS 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5

print(1 < x < 10)

print(1 < x and x < 10)

x = 5

print(x > 0 and x < 10)


# Identity Operators 


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# ASSIGNMENT OPERATORS

x = 5

x += 3
x -= 4
x *= 7
x %= 3
x /= 4
x //= 4
print(x)

# WALRUS OPERATOR (:=) ASSIGNS A VALUE TO A VARIABLE AND USES THE VALUE AT THE SAME TIME

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 7:
    print(f"List has {count} elements")
    
else:
    print(f'List does not have {count} elements')
    

numbers = [1, 2, 3, 4, 5]

# Without walrus — 2 lines
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")   # List has 5 elements

# With walrus — 1 line, same result
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")   # List has 5 elements  


# LOGICAL OPRATORS 
x = 5
print(x > 0 and x < 10) 

x = 5
print(x < 2 or x > 10)

x = 5
print(not(x > 3 and x < 10))

# IDENTITY OPERATORS 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #x and z point to the same memory location
print(x is y)# False — x and y have same values but live in different memory locations
print(x == y)


x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)


text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)