from collections import defaultdict
T = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b :
        parent[b] = a
        friendsNum[a] += friendsNum[b]

for _ in range (T):
    parent , friendsNum = {}, {}

    F = int(input())

    for _ in range (F):
        frOne, frTwo = input().split()

        if frOne not in parent:
            parent[frOne] = frOne
            friendsNum[frOne] = 1

        if frTwo not in parent:
            parent[frTwo] = frTwo
            friendsNum[frTwo] = 1

        union(frOne, frTwo)

        print(friendsNum[find(frOne)])


"""

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	256 MB	22640	5504	3288	24.909%

문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

예제 입력 1 
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty

예제 출력 1 
2
3
4
2
2
4
"""