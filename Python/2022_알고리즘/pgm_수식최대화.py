from itertools import permutations


def solution(expression):
    answer = 0

    operator = ['*', '+', '-']
    priorityOperator = list(permutations(operator, 3))

    expressionArr = []

    # 숫자, 연산자 List 생성
    temp = ""
    for ex in expression:
        if (ex in "0123456789"):
            temp += ex
        else:
            expressionArr.append(temp)
            expressionArr.append(ex)
            temp = ""
    expressionArr.append(temp)

    # 모든 경우의 연산자 우선수누이에 대해 반복
    for po in priorityOperator:

        copyExpression = [i for i in expressionArr]
        for o in po:
            stack = []
            while copyExpression:
                temp = copyExpression.pop(0)
                if (temp == o):
                    # 해당 연산자면 계산 후 stack 증가
                    if o == '*':
                        stack.append(int(stack.pop()) * int(copyExpression.pop(0)))
                    elif o == '+':
                        stack.append(int(stack.pop()) + int(copyExpression.pop(0)))
                    else:
                        stack.append(int(stack.pop()) - int(copyExpression.pop(0)))
                else:
                    stack.append(temp)
            copyExpression = stack
        answer = max(answer, abs(int(stack[0])))

    return answer