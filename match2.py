import collections
import pandas as pd
import sys
import os
import re

seqDB = collections.defaultdict(dict) # 系列DB
input_tenhou = pd.ExcelFile('tenhou_v3.xlsx') # ファイル読み込み
input_sheet_name = input_tenhou.sheet_names
input_tenhou_df = input_tenhou.parse(input_sheet_name[0])
input_tenhou_mae_df = input_tenhou_df[["mae"]] # 天鳳前系列系列DB
input_tenhou_ato_df = input_tenhou_df[["ato"]] # 天鳳後系列系列DB
length = int(len(input_tenhou_ato_df.index) -1) # 要素数

prevSeqs = [] #天鳳前系列
nextSeqs = [] #天鳳後系列

#天鳳前系列に格納
n = 0
while length >= n:
    youso = str([input_tenhou_mae_df.iat[n,0]])
    result = re.sub(r"\D", "", youso)
    prevSeqs.append(result)
    n += 1

#天鳳後系列に格納
n = 0
while length >= n:
    youso = str([input_tenhou_ato_df.iat[n,0]])
    result = re.sub(r"\D", "", youso)
    nextSeqs.append(result)
    n += 1

print(len(prevSeqs))
print(len(nextSeqs))















# prevSeqs = ['1234', '1234', '1234', '1234'] #前系列
# nextSeqs = ['123', '123', '234', '134'] #後系列

# # 系列DB 作成
# for i in range(len(prevSeqs)):
#     seqDB[prevSeqs[i]][nextSeqs[i]] = seqDB[prevSeqs[i]].get(nextSeqs[i], 0) + 1
#     # (前系列, 後系列) のペアの頻度を一つインクリメント
# # 系列DB の出力
# # print(seqDB)

# # 前系列'1234'について, 頻度最大となる後系列を選ぶ
# input = '1234'
# maxCount = 0
# maxKey = ''
# for key in seqDB[input].keys():
#     if seqDB[input][key] > maxCount:
#         maxCount = seqDB[input][key]
#         maxKey = key
# print("前系列:\'{}\' -> 後系列:\'{}\' | 頻度:{}".format(input, maxKey, maxCount))
# # 出力: 前系列:'1234' -> 後系列:'123' | 頻度:2

# # 捨て牌（の数字）を出力
# # 前系列input をselected にコピーし、後系列maxKey に含まれる文字を一文字ずつ削除
# selected = input
# for char in maxKey:
#     selected = selected.replace(char, '', 1) 
# print("捨て牌:\'{}\'".format(selected))
# # 出力: 捨て牌:'4'