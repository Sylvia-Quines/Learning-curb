import pandas as pd

mydataset = {
    "cars": ["BMW","Volvo","Ford"],
    "passings" : [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print(pd.__version__)

a = [1, 5, 8]
myVar = pd.Series(a,index = ['x', 'y', 'z'])
print(myVar)
print(myVar['x'])

distance = {'day1': 32, 'day2': 45, 'day3': 61}
mydistance = pd.Series(distance, index = ['day1','day2'])
print(mydistance)

data = {
 'names': ['Adwoa', 'Yaw', 'Sam', 'Seth', 'Andrew'],
 'age': [12, 8, 9, 4, 7]
 }
mychildren = pd.DataFrame(data)
print(mychildren)
