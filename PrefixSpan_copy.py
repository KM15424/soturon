import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

# Excelファイルを読み込む
excel_data = pd.read_excel('./data/houou_dan_data4.xlsx')
# データフレームからリストへ変換
data_list = excel_data.values.tolist()

df = pd.DataFrame(data_list, columns=['mae', 'ato'])
df['mae'] = df['mae'].apply(lambda x: eval(x) if isinstance(x, str) else x)
df['ato'] = df['ato'].apply(lambda x: eval(x) if isinstance(x, str) else x)

# 各リストの要素を文字列に変換
data_list_str = [[str(item) for item in sublist] for sublist in data_list]

# TransactionEncoderを使用してバイナリ形式のデータに変換
te = TransactionEncoder()
te_ary = te.fit(data_list_str).transform(data_list_str)

# バイナリ形式のデータをデータフレームに変換
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# minsupの定義
minsup = 0.0001

# FPGrowthアルゴリズムの適用
frequent_itemsets = fpgrowth(df_encoded, min_support=minsup, use_colnames=True)

# 最小長と最大長でフィルタリング
filtered_itemsets = frequent_itemsets[
    (frequent_itemsets['itemsets'].apply(len) >= 2) &
    (frequent_itemsets['itemsets'].apply(len) <= 3)
]

# 結果の表示
pd.set_option('display.max_rows', 1000)
print(filtered_itemsets)