import pandas as pd
data = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]
df = pd.DataFrame(data, columns=["fruits", "cost", "buy"])
print(df.head())


df = pd.DataFrame({
    "fruits": ["Apple", "Banana", "Orange", "Mango", "Grape","Guava"],
    "cost": [30, 20, 25, 60, 45, 35],
    "buy": [100, 150, 80, 60, 90, 54]
})
print(df.tail())


print(df.shape)
print(df.columns)

print(df.info())

print(df.describe().round(2))
df.to_csv('0520_stock2.csv',index=False)