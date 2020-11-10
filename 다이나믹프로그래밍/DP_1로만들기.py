"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	125039	41844	26140	32.229%

문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""
x = int(input())
array = [0 for _ in range(x+1)]
array[0]=0
array[1]=0

for i in range(2,x+1):

    if (i%3 == 0 and i%2 == 0):
      array[i] = min(array[i//3], array[i//2], array[i-1]) + 1
      continue

    elif (i%3 == 0 and i%2 != 0):
      array[i] = min(array[i//3], array[i-1]) + 1

      continue
    elif (i%3 != 0 and i%2 == 0):
      array[i] = min(array[i//2], array[i-1]) + 1
      continue
    else:
      array[i] = array[i-1] + 1

print(array[x])