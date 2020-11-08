"파일에 있는 각각의 단어의 수 구하기"
import collections
fr=open('test.txt', 'r')
temp=list(map(lambda x: x.split(), fr))
dic=collections.defaultdict(int)
for i,j in temp:
    dic[i]+=1
    dic[j]+=1
for i,j in sorted(dic.items(),key=lambda x:x[1],reverse=True):
    print(i,j)

