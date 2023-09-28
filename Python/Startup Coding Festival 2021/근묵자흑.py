# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
numarr = list(map(int, input().split()))
keyidx = numarr.index(min(numarr))

# keyidx를 기준으로 왼쪽, 오른쪽으로 나눔
arr1 = numarr[:keyidx]
arr2 = numarr[keyidx + 1:]
tmp = []

# 더 짧은 쪽 선택하기 위해
if len(arr1) > len(arr2):
    tmp = arr2
    arr2 = arr1
    arr1 = tmp

while len(arr1) - K != -1:
    if len(arr1) >= K:
        arr2.append(arr1.pop())
    else:
        arr1.append(arr2.pop())
#이 과정이 끝나고나면, 왼쪽은 무조건 keyidx를 기준으로 한번에 끝낼 수 있게됨.
#따라서 1 + (arr2의 길이를 K-1개로 나눈 몫)이 정답.
#만약, arr2의 길이가 K-1개로 나누어 떨어지지 않으면  +1을 한번 더 해주면 정답.

if N == K:
    print(1)
else:
    if len(arr2) % (K - 1) == 0:
        print(1 + len(arr2) // (K - 1))
    else:
        print(2 + len(arr2) // (K - 1))
