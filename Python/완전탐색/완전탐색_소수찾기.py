"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다.
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	return
17	3
011	2

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
"""


from itertools import permutations
def solution(numbers):
    answer = []
    num_list = list(map(str,numbers))
    cnt=0

    for i in range (1,len(numbers)+1):
        temp=(set(list(map(int,(map("".join,permutations(num_list,i)))))))
        mx_num=max(temp)
        for j in temp:
            cnt=0
            if j == 1 or j == 0:
                continue
            for k in range (2,int(j**0.5)+1):
                if j%k == 0:
                    cnt+=1
                    break

            if cnt==0:
                answer.append(j)

    return len(set(answer))

#numbers="17"
numbers="011"
#numbers="1231"
#numbers="7843"
#numbers="9999999"
print(solution(numbers))