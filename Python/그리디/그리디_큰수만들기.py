"""
어떤 숫자에서 k개의 수를 제거했을 때
얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면
[19, 12, 14, 92, 94, 24] 를 만들 수 있습니다.
이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가
solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중
가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
"""

def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

if __name__ == '__main__':
    number="1924"
    k=2

    number="1231234"
    k=3

    number="4177252841"
    k=4
#    number="1231234"
#    k=3

    number="999991991"
    k=5
#    number="999"
#    k=2

#    number="9991"
#    k=3

    print(solution(number,k))