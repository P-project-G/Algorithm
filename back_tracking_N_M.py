"""
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

"""
from itertools import permutations
N,M=list(map(int,input().split()))
answer=[i+1 for i in range (N)]
result=list(permutations(answer,M))
result=sorted(result,key=lambda x: (x[0]))
for i in result:
    print(" ".join(map(str,i)))