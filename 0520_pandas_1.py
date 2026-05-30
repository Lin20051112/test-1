import pandas as pd
stock1 = pd.Series([120, 80, None, 60, 95, None, 110])
print("stock1\n",stock1)

stock2 = pd.Series({"Apple":120,"Banana":80,"Orange":None,"Mango":60, "Grape":95, "Peach":None, "Melon":110 })
print("stock2\n",stock2)

stock3 = stock2.to_dict()
print("stock3\n",stock3)



print("Banana庫存",stock2["Banana"])
print("缺失檢查",stock2.isna())
print("缺失數量",stock2.isna().sum())
stock2.to_csv('0520_stock.csv',index=False)