from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = [[] for _ in range(11)]
    orderRank = [0 for _ in range(11)]

    # 코스메뉴 dict
    dic = defaultdict(int)

    for order in orders:
        # 알파벳 사전순 정렬
        ord = sorted(order)
        for i in range(1, len(order)):
            # 모든 조합 생성해서 코스메뉴 dict에 추가
            for com in combinations(ord, i + 1):
                temp = "".join(com)
                if dic[temp]:
                    dic[temp] += 1
                else:
                    dic[temp] = 1

    for d in dic:
        # 2사람 이상이 주문한 코스메뉴
        if dic[d] > 1:
            if (orderRank[len(d)] < dic[d]):
                orderRank[len(d)] = dic[d]
                answer[len(d)] = [d]
            elif (orderRank[len(d)] == dic[d]):
                answer[len(d)].append(d)
    ans = []
    for c in course:
        ans.extend(answer[c])

    return sorted(ans)