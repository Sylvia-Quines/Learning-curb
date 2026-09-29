import pandas as pd

data = {
    "calories": [520, 320, 300, 610],
    "duration": [10, 40, 50, 30]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3", "day4"])

print(df)
print(df.loc["day1"]) #this returns a row
print(df.loc[["day1", "day2"]])

df = pd.read_csv("data.csv") #this loads a comma separated file into dataframe.

