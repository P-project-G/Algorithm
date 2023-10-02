"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 *두 개씩* 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
* 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
* 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
* 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
"""

def solution(genres, plays):
    answer=[]
    kind=set(genres)
#    for k in kind:
#        s=0
#        for i,j in zip(genres,plays):
#            if i==k:
#                s+=j
#        dic[s]=k
    dic=dict.fromkeys(kind,0)
    for i,j in zip(genres,plays):
        dic[i]+=j
    dic={j:i for i,j in dic.items()}
    temp=[]
    cnt=[i for i in range(len(plays))]
    for i,j,k in zip(genres,plays,cnt):
        temp.append((i,j,k))
    temp=sorted(temp,key=lambda x:x[1],reverse=True)
    for ll in range(len(kind)):
        go=dic.pop(max(dic))
        cnt=0
        for i,j,k in temp:
            if cnt!=2:
                if i==go:
                    answer.append(k)
                    cnt+=1
    return answer


if __name__ == '__main__':
    genres=["classic","pop","classic","classic","pop"]
    plays=[500,600,150,800,2500]
    print(solution(genres,plays))