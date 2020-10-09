"""
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

def solution(depth,N,M):
    Nlist=[i for i in range(1,N+1)]

    if depth==M:
        print(out)
        return

    for i in range(N):
        if check[i]:
            continue
        out.append(Nlist[i])
        check[i]=True

        solution(depth+1,N,M)

        out.pop()
        check[i]=False



if __name__=='__main__':
    N,M=map(int,input().split())
    out=[]
    check=[False]*N
    solution(0,N,M)
