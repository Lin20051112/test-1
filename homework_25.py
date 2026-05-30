import pandas as pd

file_path = "Grocery_Inventory_and_Sales_Dataset.csv"
df = pd.read_csv(file_path)

if 'Unit_Price' in df.columns:
    df['Unit_Price'] = df['Unit_Price'].astype(str).str.replace('$', '', regex=False).str.strip()

if 'Sales_Volume' in df.columns:
    df['Sales_Volume'] = df['Sales_Volume'].astype(str).str.replace(',', '', regex=False).str.strip()

if 'Stock_Quantity' in df.columns:
    df['Stock_Quantity'] = df['Stock_Quantity'].astype(str).str.replace(',', '', regex=False).str.strip()

df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')
df['Sales_Volume'] = pd.to_numeric(df['Sales_Volume'], errors='coerce')
df['Stock_Quantity'] = pd.to_numeric(df['Stock_Quantity'], errors='coerce')

df['Unit_Price'] = df['Unit_Price'].fillna(0)
df['Sales_Volume'] = df['Sales_Volume'].fillna(0)
df['Stock_Quantity'] = df['Stock_Quantity'].fillna(0)

print("--- 資料集前五行預覽 ---")
print(df.head())
print("\n" + "="*50 + "\n")

df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']

print("(1) 每個商品的總庫存價值 (前 10 筆)：")
print(df[['Product_Name', 'Stock_Quantity', 'Unit_Price', 'Total_Inventory_Value']].head(10))
print("\n" + "="*50 + "\n")

best_selling_product = df.sort_values(by='Sales_Volume', ascending=False).iloc[0]

print(f"(2) 最暢銷的商品是：")
print(f"    商品名稱: {best_selling_product['Product_Name']}")
print(f"    總銷售量: {best_selling_product['Sales_Volume']} 單位")
print("\n" + "="*50 + "\n")

df['Revenue_90_Percent'] = df['Sales_Volume'] * df['Unit_Price'] * 0.9
total_discounted_revenue = df['Revenue_90_Percent'].sum()

print(f"(3) 所有商品在打 9 折後的「總收入」為: ${total_discounted_revenue:,.2f}")

df.to_csv("Grocery_Analysis_Results.csv", index=False)
print("\n[提示] 分析結果已成功匯出至 'Grocery_Analysis_Results.csv'")