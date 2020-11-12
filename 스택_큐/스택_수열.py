"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	43312	13963	10165	32.538%

문제
스택 (stack)은 기본적인 자료구조 중 하나로,
컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아
제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out)
특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써,
하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는
반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다.
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
push연산은 +로, pop 연산은 -로 표현하도록 한다.
불가능한 경우 NO를 출력한다.
"""
import sys
input = sys.stdin.readline
n=int(input())
final_arr=[int(input()) for i in range(n)]
cal_arr=sorted(final_arr,reverse=True)
stack_arr=[0]
res_arr=[]
answer=[]
i=0
while True:
    if cal_arr==[]:
        break
    if stack_arr[-1]==final_arr[i]:
        i+=1
        res_arr.append(stack_arr.pop())
        answer.append('-')
    else:
        stack_arr.append(cal_arr.pop())
        answer.append('+')
while True:
    i=stack_arr.pop()
    if i==0:
        break
    else:
        res_arr.append(i)
        answer.append('-')

if res_arr == final_arr:
    for i in answer:
        print(i)
else:
    print("NO")


#다른 코드,
#for문안에서 입력을 받으며, cnt를 활용한 방식
#pop할때 같지 않으면 바로 false 해주는 것이 좋은 듯
"""
n = int(input())  # 정수 n 입력
stack = []  # 스택
op = []  # 연산자를 담을 배열
temp = True  # 수열이 되는지 판단
cnt = 1

for i in range(n):

    num = int(input())

    while (cnt <= num):
        stack.append(cnt)
        op.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        op.append("-")
    else:
        temp = False

# 수열이 안되면 NO를 출력, 수열이 되면 연산자 출력
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
"""