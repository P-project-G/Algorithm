'''
programmers hash #3 위장
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때
서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
'''

from collections import Counter

def solution(clothes):
    answer=1
    cnt=list(Counter(list(dict(clothes).values())).values())
    for i in range (len(cnt)):
        answer*=(cnt[i]+1)
    return answer-1
if __name__ == '__main__':
    clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "face"], ["green_turban", "headgear"]]
    print(solution(clothes))