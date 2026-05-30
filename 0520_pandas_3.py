import pandas as pd

# 1. 讀取 CSV 檔案
file_path = "SuperMarket Analysis.csv"
df = pd.read_csv(file_path)

print(f"原始資料總筆數：{df.shape[0]} 筆")
print(f"原始資料總欄數：{df.shape[1]} 個")
print("-" * 50)
print("原始前 5 筆資料內容預覽：")
print(df.head())
print("\n" + "="*60 + "\n")

df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()

df['sales'] = pd.to_numeric(df['sales'], errors='coerce').fillna(0)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)

filtered_df = df[
    (df['branch'].astype(str).str.startswith('A', na=False)) &
    (df['customer type'] == 'Member')
]

print("【篩選後的資料預覽】：")
print(filtered_df[['branch', 'customer type', 'product line', 'sales']].head())
print("\n" + "="*60 + "\n")

product_summary = df.groupby('product line').agg(
    Total_Sales=('sales', 'sum'),
    Average_Rating=('rating', 'mean')
).round(2)

city_gender_summary = df.groupby(['city', 'gender']).agg(
    Average_Sales=('sales', 'mean'),
    Transaction_Count=('sales', 'count')
).round(2)

print("【城市與性別分析】：")
print(city_gender_summary)
print("\n" + "="*60 + "\n")

best_selling_line = product_summary['Total_Sales'].idxmax()
best_selling_value = product_summary['Total_Sales'].max()

print(f"總銷售額最高的產品線為：{best_selling_line} ")
print(f"總銷售金額為：${best_selling_value:,.2f}")
print("\n" + "="*60 + "\n")

print("【產品線結果】：")
print(product_summary)
print("\n" + "="*60 + "\n")

output_file = "0520_pandas_3OK.CSV"
product_summary.to_csv(output_file, encoding='utf-8-sig')
print(f"\n[成功] 彙總資料已成功輸出至檔案：{output_file}")