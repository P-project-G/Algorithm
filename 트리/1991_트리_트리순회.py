n = int(input())
tree = {}

def preorder(node):
    if node == '.':
        return
    print(node,end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node,end="")
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node,end="")

for _ in range (n):
    root,l,r = input().split()
    tree[root] = (l,r)
preorder('A')
print()
inorder('A')
print()
postorder('A')

"""
그림문제
링크
https://www.acmicpc.net/problem/1991

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	22970	14279	10883	63.610%

문제
이진 트리를 입력받아
전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한
결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력 1 
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

예제 출력 1 
ABDCEFG
DBAECFG
DBEGFCA
"""