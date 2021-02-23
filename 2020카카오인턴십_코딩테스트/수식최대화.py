from itertools import permutations

def calculator(express,operator,d):
    if d==2:
        return str(eval(express))

    if operator[d]=='+':
        result = eval('+'.join([calculator(i,operator,d+1) for i in express.split('+')]))

    if operator[d]=='-':
        result = eval('-'.join([calculator(i,operator,d+1) for i in express.split('-')]))

    if operator[d]=='*':
        result = eval('*'.join([calculator(i,operator,d+1) for i in express.split('*')]))


    return str(result)

def solution(expression):
    answer = 0
    operator = ['+','-','*']
    all_operator = list(permutations(operator,3))

    for operator in all_operator:
        candidate=int(calculator(expression,operator,0))
        answer = max(answer,abs(candidate))

    return answer

expression = "100-200*300-500+20"
print(solution(expression))

#역순계산

"""
문제링크
https://programmers.co.kr/learn/courses/30/lessons/67257
"""