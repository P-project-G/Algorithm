# 카드사 [2019년, 2018년] 신용판매, 현금대출 합계 (카드사 점유율 계산)
shinhan=["신한",1501966,1423041]
lotte=["롯데",723650,712779]
samsung=["삼성",1221157,1235959]
bc=["비씨",1293142,1219199]
kb=["국민",1130111,1031470]
hyundae=["현대",1057115,980321]
hana=["하나",547615,532758]
woori=["우리",605108,548556]

all = [shinhan, lotte, samsung, bc, kb, hyundae, hana, woori]

cur_last_profit = [ [name,str((a-b)/10000)+"조"] for name,a,b in all]
print("작년대비, 증가율 순위") # 현재실적 - 전년도실적
cur_last_profit.sort(key=lambda x: x[1],reverse=True)
for i in range (len(cur_last_profit)):
    print(str(i+1)+"등", *cur_last_profit[i])

print()

print("2019년 영업실적 순위") # 현재실적
cur = [ [name,a/10000] for name,a,b in all ]
cur.sort(key=lambda x: x[1], reverse=True)
for i in range (len(cur)):
    print(str(i+1)+"등", *cur[i],end="")
    print("조")

print()

print("시장 점유율 순위") # 현재실적 / 전체실적 * 100
occupancy=[ a/10000 for name,a,b in all ]
occupancy_ratio = [ [name, round((a/10000)/sum(occupancy) * 100,3)] for name,a,b in all ]
occupancy_ratio.sort(key=lambda x: x[1], reverse=True)
for i,a in enumerate(occupancy_ratio):
    print(str(i+1)+"등",*a,end="")
    print("%")