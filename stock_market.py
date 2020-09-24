"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
"""

def solution(prices):
    answer = []
    for i in range (len(prices)):
        t=0
        for j in range (i,len(prices)):
            t+=1
            if prices[i]>prices[j]:
                break
        answer.append(t-1)
    return answer

if __name__ == '__main__':
    prices=[1,2,3,2,3]
    print(solution(prices))