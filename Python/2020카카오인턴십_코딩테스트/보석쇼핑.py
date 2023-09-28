"""
문제링크
https://programmers.co.kr/learn/courses/30/lessons/67258
"""

from collections import defaultdict
def solution(gems):
    answer=[]
    result=[]
    set_gems = set(gems)
    start,end = 0,0
    gems_dic = defaultdict(int)
    gems_dic[gems[0]] += 1

    # O(n)으로 탐색하는 투 포인터 알고리즘 사용
    while (start < len(gems) and end < len(gems)):
        if len(gems_dic) == len(set_gems):
            result.append([start+1,end+1])
            if gems_dic[gems[start]] == 1:
                del gems_dic[gems[start]]
            else:
                gems_dic[gems[start]] -= 1
            start+=1
            continue
        else:
            end += 1
            if end == len(gems):
                break
            else:
                gems_dic[gems[end]] += 1

    answer=sorted(result,key=lambda x: x[1]-x[0])
    return answer[0]


"""
31.1 // 100 (시간 초과)
def solution(gems):
    answer = []
    result = []
    set_gems = set(gems)

    for i in range (len(gems)-1):
        result=[]
        result.append(gems[i])
        for j in range (i,len(gems)):
            if gems[j] not in result:
                result.append(gems[j])
            if len(result) == len(set_gems):
                answer.append([i+1,j+1])
                break

    answer=sorted(answer,key=lambda x: x[1]-x[0])
    return answer[0]
"""


gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems=["AA", "AB", "AC", "AA", "AC"]
gems=["XYZ", "XYZ", "XYZ"]
#gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))