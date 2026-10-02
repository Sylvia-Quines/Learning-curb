import pandas as pd
from pathlib import Path

titanic = pd.read_csv('titanic.csv')
print(titanic.to_string())