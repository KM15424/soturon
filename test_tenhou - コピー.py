import collections
import pandas as pd
import sys
import os
import copy
import glob
import re

seqDB = collections.defaultdict(dict) # 系列DB
input_tenhou = pd.ExcelFile('tenhou_v3.xlsx') # ファイル読み込み
input_sheet_name = input_tenhou.sheet_names
input_tenhou_df = input_tenhou.parse(input_sheet_name[0])
input_tenhou_mae_df = input_tenhou_df[["mae"]] # 天鳳前系列系列DB
input_tenhou_ato_df = input_tenhou_df[["ato"]] # 天鳳後系列系列DB
length = int(len(input_tenhou_ato_df.index) -1) # 要素数

prevSeqs = [] #前系列
nextSeqs = [] #後系列

#前系列に格納
n = 0
while length >= n:
    youso = str([input_tenhou_mae_df.iat[n,0]])
    result = re.sub(r"\D", "", youso)
    prevSeqs.append(result)
    n += 1

#後系列に格納
n = 0
while length >= n:
    youso = str([input_tenhou_ato_df.iat[n,0]])
    result = re.sub(r"\D", "", youso)
    nextSeqs.append(result)
    n += 1

# 系列DB 作成
for i in range(len(prevSeqs)):
    seqDB[prevSeqs[i]][nextSeqs[i]] = seqDB[prevSeqs[i]].get(nextSeqs[i], 0) + 1
    # (前系列, 後系列) のペアの頻度を一つインクリメント
# 系列DB の出力
# print(seqDB)

#一致率を測る↓
dir_path = './houou_ittiyou' #牌譜までのファイルパス
files = os.listdir(dir_path)
count = 0
match_count = 0
match_count2 = 0
match_count3 = 0
c = 0
c2 = 0
c3 = 0
m = ["1m","2m","3m","4m","5m","6m","7m","8m","9m"]
p = ["1p","2p","3p","4p","5p","6p","7p","8p","9p"]
s = ["1s","2s","3s","4s","5s","6s","7s","8s","9s"]
j = ['東','南','西','北','白','發','中']

#ファイルの数だけ繰り返す
for file in files:
    file_path = os.path.join(dir_path, file)
    c += 1
    with open (file_path, encoding="utf-8") as f:
        dan0 = 0
        dan1 = 0
        dan2 = 0
        dan3 = 0
        #いらない部分を削除
        paihu = f.read()

        if dan := re.search('dan=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"',paihu):
            dan = dan.group()
            dan = dan.replace('dan=','')

            dan_group = re.findall(r"\d+", dan)
            dan_num = 0
            for data in dan_group :
                if dan_num == 0 and int(data) == 16:
                    dan0 = 1
                if dan_num == 1 and int(data) == 16:
                    dan1 = 1
                if dan_num == 2 and int(data) == 16:
                    dan2 = 1
                if dan_num == 3 and int(data) == 16:
                    dan3 = 1
                dan_num += 1
        
        paihu = re.sub(r'^.*(?=<TAIKYOKU)', r'', paihu)
        delete = re.search('<TAIKYOKU oya=\"\d\"/>',paihu)
        delete = delete.group()
        paihu = paihu.replace(delete,"",1)

        print(c)
        while True:
            if paihu[0:3] == "<UN":
                act = re.search('<UN\sn\d=\".{1,100}\"\s/>',paihu)
                act = act.group()
                paihu = paihu.replace(act,"",1)
            if paihu[0:2] == "<A": #上がりの場合
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:    
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:    
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:    
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:    
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:    
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:    
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
                if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                    if act.start() == 0:
                        act = act.group()
                        paihu = paihu.replace(act,"",1)
            if delete2 := re.search(r'<INIT\sseed=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sten=\"[0-9]{1,4},[0-9]{1,4},[0-9]{1,4},[0-9]{1,4}\"\soya=\"\d\"\shai0=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai1=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai2=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai3=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"/>',paihu):
                print(c2)
                c2 += 1
                tehai_m = []
                tehai_p = []
                tehai_s = []
                tehai_j = []
                tehai_m2 = []
                tehai_p2 = []
                tehai_s2 = []
                tehai_j2 = []

                tehai2_m = []
                tehai2_p = []
                tehai2_s = []
                tehai2_j = []
                tehai2_m2 = []
                tehai2_p2 = []
                tehai2_s2 = []
                tehai2_j2 = []

                tehai3_m = []
                tehai3_p = []
                tehai3_s = []
                tehai3_j = []
                tehai3_m2 = []
                tehai3_p2 = []
                tehai3_s2 = []
                tehai3_j2 = []

                tehai1_m = []
                tehai1_p = []
                tehai1_s = []
                tehai1_j = []
                tehai1_m2 = []
                tehai1_p2 = []
                tehai1_s2 = []
                tehai1_j2 = []
                hai = re.search('hai0=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai0=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai_s.append(str(hai_num) + 's')

                hai = re.search('hai1=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai1=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai1_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai1_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai1_s.append(str(hai_num) + 's')

                hai = re.search('hai2=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai2=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai2_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai2_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai2_s.append(str(hai_num) + 's')

                hai = re.search('hai3=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai3=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai3_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai3_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai3_s.append(str(hai_num) + 's')

                delete2 = delete2.group()

            elif delete2 := re.search(r'<INIT\sseed=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sten=\"[0-9]{1,4},[0-9]{1,4},[0-9]{1,4},[0-9]{1,4}\"\soya=\"\d\"\shai0=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai1=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai2=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai3=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\sshuffle=\".{0,100}\"/>',paihu):
                print(c2)
                c2 += 1
                tehai_m = []
                tehai_p = []
                tehai_s = []
                tehai_j = []
                tehai_m2 = []
                tehai_p2 = []
                tehai_s2 = []
                tehai_j2 = []

                tehai2_m = []
                tehai2_p = []
                tehai2_s = []
                tehai2_j = []
                tehai2_m2 = []
                tehai2_p2 = []
                tehai2_s2 = []
                tehai2_j2 = []

                tehai3_m = []
                tehai3_p = []
                tehai3_s = []
                tehai3_j = []
                tehai3_m2 = []
                tehai3_p2 = []
                tehai3_s2 = []
                tehai3_j2 = []

                tehai1_m = []
                tehai1_p = []
                tehai1_s = []
                tehai1_j = []
                tehai1_m2 = []
                tehai1_p2 = []
                tehai1_s2 = []
                tehai1_j2 = []
                hai = re.search('hai0=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai0=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai_s.append(str(hai_num) + 's')

                hai = re.search('hai1=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai1=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai1_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai1_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai1_s.append(str(hai_num) + 's')

                hai = re.search('hai2=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai2=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai2_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai2_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai2_s.append(str(hai_num) + 's')

                hai = re.search('hai3=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"',paihu)
                hai = hai.group()
                hai = hai.replace('hai3=','')

                start_tehai = re.findall(r"\d+", hai)
                start_tehai_int = []
                for data in start_tehai :
                    start_tehai_int.append(int(data))
                start_tehai_int.sort()
                for tehai in start_tehai_int:
                    hai_num = tehai // 4
                    amari = tehai % 4
                    if hai_num < 9:
                        hai_num += 1
                        tehai3_m.append(str(hai_num) + 'm')
                    elif hai_num < 18:
                        hai_num -= 8
                        tehai3_p.append(str(hai_num) + 'p')
                    elif hai_num < 27:
                        hai_num -= 17
                        tehai3_s.append(str(hai_num) + 's')

                delete2 = delete2.group()
            else:
                break

            paihu = paihu.replace(delete2,"",1)
            while True:
                if paihu[0:3] == "<UN":
                    act = re.search('<UN\sn\d=\".{1,100}\"\s/>',paihu)
                    act = act.group()
                    paihu = paihu.replace(act,"",1)
                if paihu[0:2] == "<B":
                    act = re.search('<BYE\swho=\"\d\"\s/>',paihu)
                    act = act.group()
                    paihu = paihu.replace(act,"",1)
                    while True:
                        if paihu[0:3] == "<UN":
                            act = re.search('<UN\sn\d=\".{1,100}\"\s/>',paihu)
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        if paihu[0:2] == "<B":
                            act = re.search('<BYE\swho=\"\d\"\s/>',paihu)
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        if paihu[0:2] == "<T" or paihu[0:2] == "<U" or paihu[0:2] == "<V" or paihu[0:2] == "<W" or paihu[0:2] == "<D" or paihu[0:2] == "<E" or paihu[0:2] == "<F" or paihu[0:2] == "<G":
                            if act := re.search('<[TUVWDEFG][0-9]{1,3}/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                elif act := re.search('<DORA\shai=\"[0-9]{1,3}\"\s/>',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                        elif paihu[0:2] == "<R": #リーチ、流局の場合
                            if act := re.search('<REACH\swho=\"\d\"\sstep=\"\d\"/>',paihu): 
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                            if act := re.search('<REACH\swho=\"\d\"\sten=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sstep=\"\d\"/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                            if act := re.search('<RYUUKYOKU\s',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                if act := re.search('type=\".{0,30}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('ba=\"\d,\d\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)       
                                if act := re.search('sc=\"[^a-zA-Z]{0,100}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai0=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai1=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai2=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai3=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('/>',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                        elif paihu[0:2] == "<N": #鳴きの場合
                            act = re.search('<N\swho=\"\d\"\sm=\"[0-9]{1,6}\"\s/>',paihu)
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        elif paihu[0:2] == "<A": #上がりの場合                           
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                        else:
                            break
                if paihu[0:2] == "<T" or (paihu[0:2] == "<U" and paihu[0:3] != "<UN") or paihu[0:2] == "<V" or paihu[0:2] == "<W" or paihu[0:2] == "<D" or paihu[0:2] == "<E" or paihu[0:2] == "<F" or paihu[0:2] == "<G": 
                    c3 += 1
                    act = re.search('<[TUVWDEFG][0-9]{1,3}/>',paihu)
                    act = act.group()
                    paihu = paihu.replace(act,"",1)
                    #自摸、打牌情報取得
                    act_num = re.sub(r"[^0-9]", "", act)
                    act_eng = re.sub(r"[^a-zA-Z]", "", act)
                    if act_eng == 'T':
                        hai2 = int(act_num) // 4
                        if hai2 < 9:
                            hai2 += 1
                            tehai_m.append(str(hai2) + 'm')
                            tsumohai = str(hai2) + 'm'
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai_p.append(str(hai2) + 'p')
                            tsumohai = str(hai2) + 'p'
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai_s.append(str(hai2) + 's')
                            tsumohai = str(hai2) + 's'

                    elif act_eng == 'D':
                        hai2 = int(act_num) // 4
                        tehai_m = sorted(tehai_m, key = m.index)
                        tehai_p = sorted(tehai_p, key = p.index)
                        tehai_s = sorted(tehai_s, key = s.index)
                        tehai_j = sorted(tehai_j, key = j.index)
                        tehai_m2 = tehai_m.copy()
                        tehai_p2 = tehai_p.copy()
                        tehai_s2 = tehai_s.copy()
                        tehai_j2 = tehai_j.copy()
                        if hai2 < 9:
                            hai2 += 1
                            tehai_m2.remove(str(hai2) + 'm')
                            if dan0 == 1:
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                    if input1 == str(re.sub(r"\D", "", str(tehai_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                             
                            tehai_m = tehai_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai_p2.remove(str(hai2) + 'p')
                            if dan0 == 1:
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                    if input2 == str(re.sub(r"\D", "", str(tehai_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1                 

                            tehai_p = tehai_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai_s2.remove(str(hai2) + 's')
                            if dan0 == 1:    
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                    if input3 == str(re.sub(r"\D", "", str(tehai_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1             

                            tehai_s = tehai_s2.copy()

                    elif act_eng == 'U':
                        hai2 = int(act_num) // 4
                        if hai2 < 9:
                            hai2 += 1
                            tehai1_m.append(str(hai2) + 'm')
                            tsumohai = str(hai2) + 'm'
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai1_p.append(str(hai2) + 'p')
                            tsumohai = str(hai2) + 'p'
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai1_s.append(str(hai2) + 's')
                            tsumohai = str(hai2) + 's'
                       
                    elif act_eng == 'E':
                        hai2 = int(act_num) // 4
                        tehai1_m = sorted(tehai1_m, key = m.index)
                        tehai1_p = sorted(tehai1_p, key = p.index)
                        tehai1_s = sorted(tehai1_s, key = s.index)
                        tehai1_j = sorted(tehai1_j, key = j.index)
                        tehai1_m2 = tehai1_m.copy()
                        tehai1_p2 = tehai1_p.copy()
                        tehai1_s2 = tehai1_s.copy()
                        tehai1_j2 = tehai1_j.copy()
                        if hai2 < 9:
                            hai2 += 1
                            tehai1_m2.remove(str(hai2) + 'm')
                            if dan1 == 1: 
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai1_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai1_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai1_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                    if input1 == str(re.sub(r"\D", "", str(tehai1_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai1_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai1_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai1_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai1_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai1_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1          

                            tehai1_m = tehai1_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai1_p2.remove(str(hai2) + 'p')
                            if dan1 == 1:  
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai1_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai1_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai1_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai1_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai1_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                    if input2 == str(re.sub(r"\D", "", str(tehai1_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai1_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai1_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai1_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1             

                            tehai1_p = tehai1_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai1_s2.remove(str(hai2) + 's')
                            if dan1 == 1:   
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai1_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai1_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai1_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai1_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai1_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai1_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai1_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                    if input3 == str(re.sub(r"\D", "", str(tehai1_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai1_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1         

                            tehai1_s = tehai1_s2.copy()
                        
                    elif act_eng == 'V':
                        hai2 = int(act_num) // 4
                        if hai2 < 9:
                            hai2 += 1
                            tehai2_m.append(str(hai2) + 'm')
                            tsumohai = str(hai2) + 'm'
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai2_p.append(str(hai2) + 'p')
                            tsumohai = str(hai2) + 'p'
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai2_s.append(str(hai2) + 's')
                            tsumohai = str(hai2) + 's'
                        
                    elif act_eng == 'F':
                        hai2 = int(act_num) // 4
                        tehai2_m = sorted(tehai2_m, key = m.index)
                        tehai2_p = sorted(tehai2_p, key = p.index)
                        tehai2_s = sorted(tehai2_s, key = s.index)
                        tehai2_j = sorted(tehai2_j, key = j.index)
                        tehai2_m2 = tehai2_m.copy()
                        tehai2_p2 = tehai2_p.copy()
                        tehai2_s2 = tehai2_s.copy()
                        tehai2_j2 = tehai2_j.copy()
                        if hai2 < 9:
                            hai2 += 1
                            tehai2_m2.remove(str(hai2) + 'm')
                            if dan2 == 1:  
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai2_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai2_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai2_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                    if input1 == str(re.sub(r"\D", "", str(tehai2_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai2_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai2_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai2_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai2_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai2_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1          

                            tehai2_m = tehai2_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai2_p2.remove(str(hai2) + 'p')
                            if dan2 == 1:  
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai2_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai2_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai2_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai2_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai2_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                    if input2 == str(re.sub(r"\D", "", str(tehai2_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai2_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai2_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai2_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1            

                            tehai2_p = tehai2_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai2_s2.remove(str(hai2) + 's')
                            if dan2 == 1:   
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai2_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai2_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai2_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai2_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai2_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai2_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai2_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                    if input3 == str(re.sub(r"\D", "", str(tehai2_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai2_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1            

                            tehai2_s = tehai2_s2.copy()
                        
                    elif act_eng == 'W':
                        hai2 = int(act_num) // 4
                        if hai2 < 9:
                            hai2 += 1
                            tehai3_m.append(str(hai2) + 'm')
                            tsumohai = str(hai2) + 'm'
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai3_p.append(str(hai2) + 'p')
                            tsumohai = str(hai2) + 'p'
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai3_s.append(str(hai2) + 's')
                            tsumohai = str(hai2) + 's'
                        
                    elif act_eng == 'G':
                        hai2 = int(act_num) // 4
                        tehai3_m = sorted(tehai3_m, key = m.index)
                        tehai3_p = sorted(tehai3_p, key = p.index)
                        tehai3_s = sorted(tehai3_s, key = s.index)
                        tehai3_j = sorted(tehai3_j, key = j.index)
                        tehai3_m2 = tehai3_m.copy()
                        tehai3_p2 = tehai3_p.copy()
                        tehai3_s2 = tehai3_s.copy()
                        tehai3_j2 = tehai3_j.copy()
                        if hai2 < 9:
                            hai2 += 1
                            tehai3_m2.remove(str(hai2) + 'm')
                            if dan3 == 1:     
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai3_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai3_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai3_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                    if input1 == str(re.sub(r"\D", "", str(tehai3_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai3_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai3_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai3_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai3_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai3_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1  

                            tehai3_m = tehai3_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai3_p2.remove(str(hai2) + 'p')
                            if dan3 == 1:  
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai3_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai3_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai3_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai3_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai3_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                    if input2 == str(re.sub(r"\D", "", str(tehai3_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai3_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1
                                # if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                #     if input3 == str(re.sub(r"\D", "", str(tehai3_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai3_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1            

                            tehai3_p = tehai3_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai3_s2.remove(str(hai2) + 's')
                            if dan3 == 1:    
                                count += 1
                                #萬子の系列調べ
                                youso1 = str(tehai3_m)
                                result = re.sub(r"\D", "", youso1)
                                input1 = str(result)
                                maxCount1 = 0
                                maxKey1 = ''
                                for key in seqDB[input1].keys():
                                    if seqDB[input1][key] > maxCount1:
                                        maxCount1 = seqDB[input1][key]
                                        maxKey1 = key

                                #筒子の系列調べ
                                youso2 = str(tehai3_p)
                                result = re.sub(r"\D", "", youso2)
                                input2 = str(result)
                                maxCount2 = 0
                                maxKey2 = ''
                                for key in seqDB[input2].keys():
                                    if seqDB[input2][key] > maxCount2:
                                        maxCount2 = seqDB[input2][key]
                                        maxKey2 = key

                                #索子の系列調べ
                                youso3 = str(tehai3_s)
                                result = re.sub(r"\D", "", youso3)
                                input3 = str(result)
                                maxCount3 = 0
                                maxKey3 = ''
                                for key in seqDB[input3].keys():
                                    if seqDB[input3][key] > maxCount3:
                                        maxCount3 = seqDB[input3][key]
                                        maxKey3 = key
                                # if maxCount1 >= maxCount2 and maxCount1 >= maxCount3: #萬子の捨て牌が最も高い頻度だった時
                                #     if input1 == str(re.sub(r"\D", "", str(tehai3_m))) and maxKey1 == str(re.sub(r"\D", "", str(tehai3_m2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                # if maxCount2 >= maxCount1 and maxCount2 >= maxCount3: #筒子の捨て牌が最も高い頻度だった時
                                #     if input2 == str(re.sub(r"\D", "", str(tehai3_p))) and maxKey2 == str(re.sub(r"\D", "", str(tehai3_p2))): #最も高い頻度の系列と今回の系列が一致した時
                                #         match_count += 1
                                if maxCount3 >= maxCount1 and maxCount3 >= maxCount2: #索子の捨て牌が最も高い頻度だった時
                                    if input3 == str(re.sub(r"\D", "", str(tehai3_s))) and maxKey3 == str(re.sub(r"\D", "", str(tehai3_s2))): #最も高い頻度の系列と今回の系列が一致した時
                                        match_count += 1            

                            tehai3_s = tehai3_s2.copy()                                       

                elif paihu[0:2] == "<N": #鳴きの場合
                    act = re.search('<N\swho=\"\d\"\sm=\"[0-9]{1,6}\"\s/>',paihu)
                    act = act.group()
                    paihu = paihu.replace(act,"",1)
                    while True:
                        if paihu[0:3] == "<UN":
                            act = re.search('<UN\sn\d=\".{1,100}\"\s/>',paihu)
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        if paihu[0:2] == "<B":
                            act = re.search('<BYE\swho=\"\d\"\s/>',paihu)
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        if paihu[0:2] == "<T" or paihu[0:2] == "<U" or paihu[0:2] == "<V" or paihu[0:2] == "<W" or paihu[0:2] == "<D" or paihu[0:2] == "<E" or paihu[0:2] == "<F" or paihu[0:2] == "<G":
                            if act := re.search('<[TUVWDEFG][0-9]{1,3}/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                elif act := re.search('<DORA\shai=\"[0-9]{1,3}\"\s/>',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                        elif paihu[0:2] == "<R": #リーチ、流局の場合
                            if act := re.search('<REACH\swho=\"\d\"\sstep=\"\d\"/>',paihu): 
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                            if act := re.search('<REACH\swho=\"\d\"\sten=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sstep=\"\d\"/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                            if act := re.search('<RYUUKYOKU\s',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                if act := re.search('type=\".{0,30}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('ba=\"\d,\d\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)       
                                if act := re.search('sc=\"[^a-zA-Z]{0,100}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai0=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai1=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai2=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('hai3=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                                if act := re.search('/>',paihu):
                                    if act.start() == 0:
                                        act = act.group()
                                        paihu = paihu.replace(act,"",1)
                        elif paihu[0:2] == "<N": #鳴きの場合
                            act = re.search('<N\swho=\"\d\"\sm=\"[0-9]{1,6}\"\s/>',paihu)
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        elif paihu[0:2] == "<A": #上がりの場合
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                        else:
                            break
                #     act = re.search('<N\swho=\"\d\"\sm=\"[0-9]{1,6}\"\s/>',paihu)
                #     act = act.group()
                #     number = re.findall(r"\d+", act)
                #     naki_N = []
                #     if int(number[0]) == 0:
                #         N = int(number[1])
                #         while N!=0:
                #             a = N % 2
                #             N = N // 2
                #             naki_N.append(a)
                #         naki_K = naki_N[2]
                #         naki_K2 = naki_N[3]
                #         naki_K3 = naki_N[4]
                #         naki_K4 = naki_N[5]
                #         (naki_K)
                #         naki_N2 = naki_N
                #         naki_N.reverse()
                #         naki = "".join(str(i) for i in naki_N)
                #         print(naki)
                #         if naki_K == 1:
                #             naki_N3 = naki_N2[10:]
                #             naki_N3.reverse()
                #             naki = "".join(str(i) for i in naki_N3)
                #             print(naki)
                #             naki = int(naki,2)
                #             nakihai = math.floor(naki/3) + naki%3
                #             print(tehai_m)
                #             print(tehai_p)
                #             print(tehai_s)
                #             print(naki)
                #         elif naki_K == 0:
                #             if naki_K2 == 1:
                #                 print(a)
                #             elif naki_K3 == 1:
                #                 print(a)
                #         elif naki_K == 0 and naki_K2 == 0 and naki_K3 == 0 and naki_K4 == 0:
                #             print(a)

                elif paihu[0:2] == "<R": #リーチ、流局の場合
                    if act := re.search('<REACH\swho=\"\d\"\sstep=\"\d\"/>',paihu): 
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                    if act := re.search('<REACH\swho=\"\d\"\sten=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sstep=\"\d\"/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                    if act := re.search('<RYUUKYOKU\s',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                        if act := re.search('type=\".{0,30}\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                        if act := re.search('ba=\"\d,\d\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)       
                        if act := re.search('sc=\"[^a-zA-Z]{0,100}\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                        if act := re.search('hai0=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                        if act := re.search('hai1=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                        if act := re.search('hai2=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                        if act := re.search('hai3=\"[0-9]{1,3}[^a-zA-Z]{0,50}\"\s',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                        if act := re.search('/>',paihu):
                            if act.start() == 0:
                                act = act.group()
                                paihu = paihu.replace(act,"",1)
                elif paihu[0:2] == "<A": #上がりの場合
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"[^a-zA-Z]{0,15}\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                else:
                    break
print("match_count")
print(match_count)
print("count")
print(count)
print(c3)













# # 前系列'1234'について, 頻度最大となる後系列を選ぶ
# input = '9'
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