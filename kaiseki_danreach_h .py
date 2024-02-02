import os
import re
import pandas as pd
import copy
import glob
import sys

dir_path = './paihu2'
dir_path2 = './houou_danreach_csv'
files = os.listdir(dir_path)
files2 = os.listdir(dir_path2)
reach = 0
oya = 0
oya_num = 0
count0 = int(len(files2))
if int(len(files2)) > 199:
    sys.exit()
csv = './houou_danreach_csv/' + 'houou' + str(count0) + 'c.csv'
df = pd.DataFrame([],columns = ['tsumo','mae','ato','sutehai','kazu'],index = ['1'])
df
df.to_csv(csv)
count = 0
count2 = 0
c2 = 500 * count0
c = 0
tsumohai = "NONE"
sutehai = "NONE"
m = ["1m","2m","3m","4m","5m","6m","7m","8m","9m"]
p = ["1p","2p","3p","4p","5p","6p","7p","8p","9p"]
s = ["1s","2s","3s","4s","5s","6s","7s","8s","9s"]
j = ['東','南','西','北','白','發','中']
#ファイルの数だけ繰り返す
for file in files:
    file_path = os.path.join(dir_path, file)
    if c == 3:
        print(count2)
        sys.exit()
    if c2 > count2:
        count2 += 1
        continue
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
            print()
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
            if delete2 := re.search(r'<INIT\sseed=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sten=\"[0-9]{1,4},[0-9]{1,4},[0-9]{1,4},[0-9]{1,4}\"\soya=\"\d\"\shai0=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai1=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai2=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"\shai3=\"[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}\"/>' ,paihu):
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
                reach = 0
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
                    elif hai_num == 27:
                        tehai_j.append('東')
                    elif hai_num == 28:
                        tehai_j.append('南')
                    elif hai_num == 29:
                        tehai_j.append('西')
                    elif hai_num == 30:
                        tehai_j.append('北')
                    elif hai_num == 31:
                        tehai_j.append('白')
                    elif hai_num == 32:
                        tehai_j.append('發')
                    elif hai_num == 33:
                        tehai_j.append('中')
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
                    elif hai_num == 27:
                        tehai1_j.append('東')
                    elif hai_num == 28:
                        tehai1_j.append('南')
                    elif hai_num == 29:
                        tehai1_j.append('西')
                    elif hai_num == 30:
                        tehai1_j.append('北')
                    elif hai_num == 31:
                        tehai1_j.append('白')
                    elif hai_num == 32:
                        tehai1_j.append('發')
                    elif hai_num == 33:
                        tehai1_j.append('中') 

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
                    elif hai_num == 27:
                        tehai2_j.append('東')
                    elif hai_num == 28:
                        tehai2_j.append('南')
                    elif hai_num == 29:
                        tehai2_j.append('西')
                    elif hai_num == 30:
                        tehai2_j.append('北')
                    elif hai_num == 31:
                        tehai2_j.append('白')
                    elif hai_num == 32:
                        tehai2_j.append('發')
                    elif hai_num == 33:
                        tehai2_j.append('中')

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
                    elif hai_num == 27:
                        tehai3_j.append('東')
                    elif hai_num == 28:
                        tehai3_j.append('南')
                    elif hai_num == 29:
                        tehai3_j.append('西')
                    elif hai_num == 30:
                        tehai3_j.append('北')
                    elif hai_num == 31:
                        tehai3_j.append('白')
                    elif hai_num == 32:
                        tehai3_j.append('發')
                    elif hai_num == 33:
                        tehai3_j.append('中')

                oya = re.search('oya=\"\d\"',paihu)
                oya = oya.group()
                oya = oya.replace('hai3=','')
                oya_nums = re.findall(r"\d+", oya)
                for n in oya_nums :
                    oya_num = int(n) 
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
                            
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                        else:
                            break

                if paihu[0:2] == "<T" or paihu[0:2] == "<U" or paihu[0:2] == "<V" or paihu[0:2] == "<W" or paihu[0:2] == "<D" or paihu[0:2] == "<E" or paihu[0:2] == "<F" or paihu[0:2] == "<G":
                    act = re.search('<[TUVWDEFG][0-9]{1,3}/>',paihu)
                    act = act.group()
                    paihu = paihu.replace(act,"",1)
                    #自摸、打牌情報取得
                    act_num = re.sub(r"[^0-9]", "", act)
                    act_eng = re.sub(r"[^a-zA-Z]", "", act)
                    #プレイヤ０のときは処理
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
                        elif hai2 == 27:
                            tehai_j.append('東')
                            tsumohai = '東'
                        elif hai2 == 28:
                            tehai_j.append('南')
                            tsumohai = '南'
                        elif hai2 == 29:
                            tehai_j.append('西')
                            tsumohai = '西'
                        elif hai2 == 30:
                            tehai_j.append('北')
                            tsumohai = '北'
                        elif hai2 == 31:
                            tehai_j.append('白')
                            tsumohai = '白'
                        elif hai2 == 32:
                            tehai_j.append('發')
                            tsumohai = '發'
                        elif hai2 == 33:
                            tehai_j.append('中')
                            tsumohai = '中'
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
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_m,tehai_m2,str(hai2) + 'm','1']
                                df.to_csv(csv)
                            tehai_m = tehai_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai_p2.remove(str(hai2) + 'p')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_p,tehai_p2,str(hai2) + 'p','1']
                                df.to_csv(csv)
                            tehai_p = tehai_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai_s2.remove(str(hai2) + 's')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_s,tehai_s2,str(hai2) + 's','1']
                                df.to_csv(csv)
                            tehai_s = tehai_s2.copy()
                        elif hai2 == 27:
                            tehai_j2.remove('東')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'東','1']
                                df.to_csv(csv)
                            tehai_j = tehai_j2.copy()
                        elif hai2 == 28:
                            tehai_j2.remove('南')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'南','1']
                                df.to_csv(csv)
                            tehai_j = tehai_j2.copy()
                        elif hai2 == 29:
                            tehai_j2.remove('西')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'西','1']
                                df.to_csv(csv)
                            tehai_j = tehai_j2.copy()
                        elif hai2 == 30:
                            tehai_j2.remove('北')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'北','1']
                                df.to_csv(csv)
                            tehai_j = tehai_j2.copy()
                        elif hai2 == 31:
                            tehai_j2.remove('白')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'白','1']
                                df.to_csv(csv)
                            tehai_j = tehai_j2.copy()
                        elif hai2 == 32:
                            tehai_j2.remove('發')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'發','1']
                                df.to_csv(csv)
                            tehai_j = tehai_j2.copy()
                        elif hai2 == 33:
                            tehai_j2.remove('中')
                            if reach == 1 and oya_num != 0 and dan0 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai_j,tehai_j2,'中','1']
                                df.to_csv(csv)  
                            tehai_j = tehai_j2.copy() 
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
                        elif hai2 == 27:
                            tehai1_j.append('東')
                            tsumohai = '東'
                        elif hai2 == 28:
                            tehai1_j.append('南')
                            tsumohai = '南'
                        elif hai2 == 29:
                            tehai1_j.append('西')
                            tsumohai = '西'
                        elif hai2 == 30:
                            tehai1_j.append('北')
                            tsumohai = '北'
                        elif hai2 == 31:
                            tehai1_j.append('白')
                            tsumohai = '白'
                        elif hai2 == 32:
                            tehai1_j.append('發')
                            tsumohai = '發'
                        elif hai2 == 33:
                            tehai1_j.append('中')
                            tsumohai = '中'
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
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1             
                                df.loc[str(count)] = [tsumohai,tehai1_m,tehai1_m2,str(hai2) + 'm','1']
                                df.to_csv(csv)
                            tehai1_m = tehai1_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai1_p2.remove(str(hai2) + 'p')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                  
                                df.loc[str(count)] = [tsumohai,tehai1_p,tehai1_p2,str(hai2) + 'p','1']
                                df.to_csv(csv)
                            tehai1_p = tehai1_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai1_s2.remove(str(hai2) + 's')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1               
                                df.loc[str(count)] = [tsumohai,tehai1_s,tehai1_s2,str(hai2) + 's','1']
                                df.to_csv(csv)
                            tehai1_s = tehai1_s2.copy()
                        elif hai2 == 27:
                            tehai1_j2.remove('東')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'東','1']
                                df.to_csv(csv)
                            tehai1_j = tehai1_j2.copy()
                        elif hai2 == 28:
                            tehai1_j2.remove('南')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'南','1']
                                df.to_csv(csv)
                            tehai1_j = tehai1_j2.copy()
                        elif hai2 == 29:
                            tehai1_j2.remove('西')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'西','1']
                                df.to_csv(csv)
                            tehai1_j = tehai1_j2.copy()
                        elif hai2 == 30:
                            tehai1_j2.remove('北')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'北','1']
                                df.to_csv(csv)
                            tehai1_j = tehai1_j2.copy()
                        elif hai2 == 31:
                            tehai1_j2.remove('白')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'白','1']
                                df.to_csv(csv)
                            tehai1_j = tehai1_j2.copy()
                        elif hai2 == 32:
                            tehai1_j2.remove('發')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'發','1']
                                df.to_csv(csv)
                            tehai1_j = tehai1_j2.copy()
                        elif hai2 == 33:
                            tehai1_j2.remove('中')
                            if reach == 1 and oya_num != 1 and dan1 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai1_j,tehai1_j2,'中','1']
                                df.to_csv(csv)  
                            tehai1_j = tehai1_j2.copy()
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
                        elif hai2 == 27:
                            tehai2_j.append('東')
                            tsumohai = '東'
                        elif hai2 == 28:
                            tehai2_j.append('南')
                            tsumohai = '南'
                        elif hai2 == 29:
                            tehai2_j.append('西')
                            tsumohai = '西'
                        elif hai2 == 30:
                            tehai2_j.append('北')
                            tsumohai = '北'
                        elif hai2 == 31:
                            tehai2_j.append('白')
                            tsumohai = '白'
                        elif hai2 == 32:
                            tehai2_j.append('發')
                            tsumohai = '發'
                        elif hai2 == 33:
                            tehai2_j.append('中')
                            tsumohai = '中'
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
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1               
                                df.loc[str(count)] = [tsumohai,tehai2_m,tehai2_m2,str(hai2) + 'm','1']
                                df.to_csv(csv)
                            tehai2_m = tehai2_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai2_p2.remove(str(hai2) + 'p')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                 
                                df.loc[str(count)] = [tsumohai,tehai2_p,tehai2_p2,str(hai2) + 'p','1']
                                df.to_csv(csv)
                            tehai2_p = tehai2_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai2_s2.remove(str(hai2) + 's')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                  
                                df.loc[str(count)] = [tsumohai,tehai2_s,tehai2_s2,str(hai2) + 's','1']
                                df.to_csv(csv)
                            tehai2_s = tehai2_s2.copy()
                        elif hai2 == 27:
                            tehai2_j2.remove('東')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'東','1']
                                df.to_csv(csv)
                            tehai2_j = tehai2_j2.copy()
                        elif hai2 == 28:
                            tehai2_j2.remove('南')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'南','1']
                                df.to_csv(csv)
                            tehai2_j = tehai2_j2.copy()
                        elif hai2 == 29:
                            tehai2_j2.remove('西')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'西','1']
                                df.to_csv(csv)
                            tehai2_j = tehai2_j2.copy()
                        elif hai2 == 30:
                            tehai2_j2.remove('北')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'北','1']
                                df.to_csv(csv)
                            tehai2_j = tehai2_j2.copy()
                        elif hai2 == 31:
                            tehai2_j2.remove('白')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'白','1']
                                df.to_csv(csv)
                            tehai2_j = tehai2_j2.copy()
                        elif hai2 == 32:
                            tehai2_j2.remove('發')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'發','1']
                                df.to_csv(csv)
                            tehai2_j = tehai2_j2.copy()
                        elif hai2 == 33:
                            tehai2_j2.remove('中')
                            if reach == 1 and oya_num != 2 and dan2 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai2_j,tehai2_j2,'中','1']
                                df.to_csv(csv) 
                            tehai2_j = tehai2_j2.copy()
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
                        elif hai2 == 27:
                            tehai3_j.append('東')
                            tsumohai = '東'
                        elif hai2 == 28:
                            tehai3_j.append('南')
                            tsumohai = '南'
                        elif hai2 == 29:
                            tehai3_j.append('西')
                            tsumohai = '西'
                        elif hai2 == 30:
                            tehai3_j.append('北')
                            tsumohai = '北'
                        elif hai2 == 31:
                            tehai3_j.append('白')
                            tsumohai = '白'
                        elif hai2 == 32:
                            tehai3_j.append('發')
                            tsumohai = '發'
                        elif hai2 == 33:
                            tehai3_j.append('中')
                            tsumohai = '中'
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
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1             
                                df.loc[str(count)] = [tsumohai,tehai3_m,tehai3_m2,str(hai2) + 'm','1']
                                df.to_csv(csv)
                            tehai3_m = tehai3_m2.copy()
                        elif hai2 < 18:
                            hai2 -= 8
                            tehai3_p2.remove(str(hai2) + 'p')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                  
                                df.loc[str(count)] = [tsumohai,tehai3_p,tehai3_p2,str(hai2) + 'p','1']
                                df.to_csv(csv)
                            tehai3_p = tehai3_p2.copy()
                        elif hai2 < 27:
                            hai2 -= 17
                            tehai3_s2.remove(str(hai2) + 's')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_s,tehai3_s2,str(hai2) + 's','1']
                                df.to_csv(csv)
                            tehai3_s = tehai3_s2.copy()
                        elif hai2 == 27:
                            tehai3_j2.remove('東')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'東','1']
                                df.to_csv(csv)
                            tehai3_j = tehai3_j2.copy()
                        elif hai2 == 28:
                            tehai3_j2.remove('南')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'南','1']
                                df.to_csv(csv)
                            tehai3_j = tehai3_j2.copy()
                        elif hai2 == 29:
                            tehai3_j2.remove('西')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'西','1']
                                df.to_csv(csv)
                            tehai3_j = tehai3_j2.copy()
                        elif hai2 == 30:
                            tehai3_j2.remove('北')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'北','1']
                                df.to_csv(csv)
                            tehai3_j = tehai3_j2.copy()
                        elif hai2 == 31:
                            tehai3_j2.remove('白')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'白','1']
                                df.to_csv(csv)
                            tehai3_j = tehai3_j2.copy()
                        elif hai2 == 32:
                            tehai3_j2.remove('發')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'發','1']
                                df.to_csv(csv)
                            tehai3_j = tehai3_j2.copy()
                        elif hai2 == 33:
                            tehai3_j2.remove('中')
                            if reach == 1 and oya_num != 3 and dan3 == 1:
                                count += 1                   
                                df.loc[str(count)] = [tsumohai,tehai3_j,tehai3_j2,'中','1']
                                df.to_csv(csv) 
                            tehai3_j = tehai3_j2.copy()                    
                        #書き込み

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
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:    
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                                if act.start() == 0:
                                    act = act.group()
                                    paihu = paihu.replace(act,"",1)
                                    break
                            if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\spaoWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
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
                            act2 = re.search('who=\"\d\"',act)
                            act2 = act2.group()
                            act_nums = re.findall(r"\d+", act2)
                            for n in act_nums :
                                if oya_num == int(n):
                                    reach = 1
                            paihu = paihu.replace(act,"",1)
                    if act := re.search('<REACH\swho=\"\d\"\sten=\"[0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\"\sstep=\"\d\"/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            act2 = re.search('who=\"\d\"',act)
                            act2 = act2.group()
                            act_nums = re.findall(r"\d+", act2)
                            for n in act_nums :
                                if oya_num == int(n):
                                    reach = 1
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
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syaku=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\sdoraHaiUra=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:    
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\sm=\"[^a-zA-Z]{0,50}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                    if act := re.search('<AGARI\sba=\"\d,\d\"\shai=\"[^a-zA-Z]{0,60}\"\smachi=\"[0-9]{1,3}\"\sten=\"[^a-zA-Z]{0,30}\"\syakuman=\"[^a-zA-Z]{0,60}\"\sdoraHai=\"[^a-zA-Z]{0,30}\"\swho=\"\d\"\sfromWho=\"\d\"\ssc=\"[^a-zA-Z]{0,100}\"\sowari=\"[^a-zA-Z]{0,100}\"\s/>',paihu):
                        if act.start() == 0:
                            act = act.group()
                            paihu = paihu.replace(act,"",1)
                            break
                else:
                    break


