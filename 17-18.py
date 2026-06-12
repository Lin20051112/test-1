import pandas as pd

# 1. 讀取 CSV 檔案
file_path = "supermarket_sales.csv"
df = pd.read_csv(file_path)

print(f"原始資料總筆數：{df.shape[0]} 筆")
print(f"原始資料總欄數：{df.shape[1]} 個")
print("-" * 50)

# 統一欄位名稱格式（去空格、變小寫）
df.columns = df.columns.str.strip().str.lower()

# ======= 💡 核心修正：將 'sales' 改為 'total' (或你檢查後對應的欄位) =======
# 如果你的 CSV 欄位真的是 sales，請忽略此處修改；但如果是 Kaggle 標準資料集，請用 'total'
target_sales_col = 'total'  # 如果欄位叫 total，就填 'total'；如果是 'sales' 就填 'sales'

df[target_sales_col] = pd.to_numeric(df[target_sales_col], errors='coerce').fillna(0)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)

# 修正後續篩選時的欄位名稱（注意：customer type 和 product line 也要確認小寫後的名稱）
filtered_df = df[
    (df['branch'].astype(str).str.startswith('A', na=False)) &
    (df['customer type'] == 'Member')
]

print("【篩選後的資料預覽】：")
print(filtered_df[['branch', 'customer type', 'product line', target_sales_col]].head())
print("\n" + "="*60 + "\n")

# 分組統計
product_summary = df.groupby('product line').agg(
    Total_Sales=(target_sales_col, 'sum'),
    Average_Rating=('rating', 'mean')
).round(2)

city_gender_summary = df.groupby(['city', 'gender']).agg(
    Average_Sales=(target_sales_col, 'mean'),
    Transaction_Count=(target_sales_col, 'count')
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

output_file = "17-18OK.CSV"
product_summary.to_csv(output_file, encoding='utf-8-sig')
print(f"\n[成功] 彙總資料已成功輸出至檔案：{output_file}")