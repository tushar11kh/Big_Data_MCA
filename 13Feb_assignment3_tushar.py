##Q1
print("Q1\n")

import pandas as pd

data = {
    'Tid': [1, 2, 3, 4, 5,6,7,8,9,10],
    'Refund': ['yes', 'no', 'no', 'yes', 'no','no','yes','no','no','no'],
    'Marital Status': ['married', 'single', 'married', 'single', 'divorced','married','divorced','single','married','single'],
    'Taxable Income': [125000, 100000, 70000, 120000, 95000,60000,220000,85000,75000,90000],
    'Cheat': ['no', 'no', 'yes', 'no', 'yes','no','no','yes','no','yes']
}

df = pd.DataFrame(data)

print(df)

##Q2
print("\nQ2\n")

rows = df.iloc[[0, 4, 7, 8]]

print(rows)

##Q3
print("\nQ3\n")

df2 = pd.read_csv('data.csv')
print(df2)