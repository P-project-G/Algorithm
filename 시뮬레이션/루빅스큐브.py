import time
import random
start = time.time()

def prt():
    for i in U:
        print("\t\t\t ",end="")
        print(*i)
    print()
    print(*L[0],"\t\t",*F[0],"\t\t",*R[0],"\t\t",*B[0])
    print(*L[1], "\t\t", *F[1], "\t\t", *R[1], "\t\t", *B[1])
    print(*L[2], "\t\t", *F[2], "\t\t", *R[2], "\t\t", *B[2])
    print()
    for i in D:
        print("\t\t\t ",end="")
        print(*i)
def rot(t):
    #F회전
    if t=="F":
       temp1,temp2,temp3= U[2][0],U[2][1],U[2][2]
       U[2][0], U[2][1], U[2][2]=L[2][2], L[1][2], L[0][2]
       L[0][2], L[1][2], L[2][2]=D[0][0], D[0][1], D[0][2]
       D[0][0], D[0][1], D[0][2]=R[2][0], R[1][0], R[0][0]
       R[0][0], R[1][0], R[2][0]=temp1,temp2,temp3

       temp1 = F[0][0]
       F[0][0],F[2][0],F[2][2],F[0][2]=F[2][0],F[2][2],F[0][2],temp1
       temp2 = F[0][1]
       F[0][1],F[1][0],F[2][1],F[1][2] = F[1][0],F[2][1],F[1][2],temp2
    elif t=="F'":
        temp1,temp2,temp3= U[2][0],U[2][1],U[2][2]
        U[2][0], U[2][1], U[2][2]=R[0][0], R[1][0], R[2][0]
        R[0][0], R[1][0], R[2][0]=D[0][2], D[0][1], D[0][0]
        D[0][2], D[0][1], D[0][0]=L[2][2], L[1][2], L[0][2]
        L[0][2], L[1][2], L[2][2]=temp3,temp2,temp1

        temp1 = F[0][0]
        F[0][0],F[0][2],F[2][2],F[2][0] = F[0][2],F[2][2],F[2][0],temp1
        temp1 = F[0][1]
        F[0][1],F[1][2],F[2][1],F[1][0] = F[1][2],F[2][1],F[1][0],temp1

    elif t=="B":
        temp1,temp2,temp3 = U[0][0],U[0][1],U[0][2]
        U[0][0],U[0][1],U[0][2] = R[0][2],R[1][2],R[2][2]
        R[0][2],R[1][2],R[2][2] = D[2][2],D[2][1],D[2][0]
        D[2][2],D[2][1],D[2][0] = L[2][0],L[1][0],L[0][0]
        L[0][0],L[1][0],L[2][0]=temp3,temp2,temp1

        temp1=B[2][0]
        B[2][0],B[2][2],B[0][2],B[0][0]=B[2][2],B[0][2],B[0][0],temp1
        temp1=B[2][1]
        B[2][1],B[1][2],B[0][1],B[1][0]=B[1][2],B[0][1],B[1][0],temp1
    elif t=="B'":
        temp1,temp2,temp3 = U[0][0],U[0][1],U[0][2]
        U[0][0],U[0][1],U[0][2]= L[2][0],L[1][0],L[0][0]
        L[2][0],L[1][0],L[0][0] = D[2][2],D[2][1],D[2][0]
        D[2][2],D[2][1],D[2][0] = R[0][2],R[1][2],R[2][2]
        R[0][2],R[1][2],R[2][2] = temp1,temp2,temp3

        temp1=B[2][0]
        B[2][0],B[0][0],B[0][2],B[2][2]=B[0][0],B[0][2],B[2][2],temp1
        temp1=B[2][1]
        B[2][1],B[1][0],B[0][1],B[1][2]=B[1][0],B[0][1],B[1][2],temp1

    elif t == "R":
        temp1,temp2,temp3 = F[0][2],F[1][2],F[2][2]

        F[0][2],F[1][2],F[2][2]  = D[0][2],D[1][2],D[2][2]
        D[2][2],D[1][2],D[0][2]  = B[0][0],B[1][0],B[2][0]
        B[0][0],B[1][0],B[2][0] = U[2][2],U[1][2],U[0][2]
        U[0][2],U[1][2],U[2][2] = temp1,temp2,temp3

        temp1=R[0][0]
        R[0][0],R[2][0],R[2][2],R[0][2] = R[2][0],R[2][2],R[0][2],temp1
        temp1=R[0][1]
        R[0][1],R[1][0],R[2][1],R[1][2] = R[1][0],R[2][1],R[1][2],temp1
    elif t == "R'":
        temp1,temp2,temp3 = F[0][2],F[1][2],F[2][2]

        F[0][2],F[1][2],F[2][2] = U[0][2],U[1][2],U[2][2]
        U[0][2],U[1][2],U[2][2] = B[2][0],B[1][0],B[0][0]
        B[0][0],B[1][0],B[2][0] = D[2][2],D[1][2],D[0][2]
        D[0][2],D[1][2],D[2][2] = temp1,temp2,temp3

        temp1=R[0][0]
        R[0][0],R[0][2],R[2][2],R[2][0] = R[0][2],R[2][2],R[2][0],temp1
        temp1=R[0][1]
        R[0][1],R[1][2],R[2][1],R[1][0] = R[1][2],R[2][1],R[1][0],temp1

    elif t == "L":
        temp1,temp2,temp3 = F[0][0],F[1][0],F[2][0]
        F[0][0],F[1][0],F[2][0] = U[0][0],U[1][0],U[2][0]
        U[0][0],U[1][0],U[2][0] = B[2][2],B[1][2],B[0][2]
        B[2][2],B[1][2],B[0][2] = D[0][0],D[1][0],D[2][0]
        D[0][0],D[1][0],D[2][0] = temp1,temp2,temp3

        temp = L[0][0]
        L[0][0],L[2][0],L[2][2],L[0][2] = L[2][0],L[2][2],L[0][2],temp
        temp = L[0][1]
        L[0][1],L[1][0],L[2][1],L[1][2] = L[1][0],L[2][1],L[1][2],temp
    elif t == "L'":
        temp1,temp2,temp3 = F[0][0],F[1][0],F[2][0]
        F[0][0],F[1][0],F[2][0] = D[0][0],D[1][0],D[2][0]
        D[0][0],D[1][0],D[2][0]  = B[2][2],B[1][2],B[0][2]
        B[2][2],B[1][2],B[0][2] = U[0][0],U[1][0],U[2][0]
        U[0][0],U[1][0],U[2][0]=temp1,temp2,temp3

        temp = L[0][0]
        L[0][0],L[0][2],L[2][2],L[2][0] = L[0][2],L[2][2],L[2][0],temp
        temp = L[0][1]
        L[0][1],L[1][2],L[2][1],L[1][0] = L[1][2],L[2][1],L[1][0],temp

    elif t == "U":
        temp = F[0]
        F[0],R[0],B[0],L[0]  = R[0],B[0],L[0],temp

        temp = U[0][0]
        U[0][0],U[2][0],U[2][2],U[0][2] = U[2][0],U[2][2],U[0][2],temp
        temp = U[0][1]
        U[0][1],U[1][0],U[2][1],U[1][2] = U[1][0],U[2][1],U[1][2],temp
    elif t == "U'":
        temp = F[0]
        F[0],L[0],B[0],R[0] = L[0],B[0],R[0],temp

        temp = U[0][0]
        U[0][0],U[0][2],U[2][2],U[2][0] = U[0][2],U[2][2],U[2][0],temp
        temp = U[0][1]
        U[0][1],U[1][2],U[2][1],U[1][0] = U[1][2],U[2][1],U[1][0],temp

    elif t == "D":
        temp=F[2]
        F[2],L[2],B[2],R[2]= L[2],B[2],R[2],temp

        temp = D[0][0]
        D[0][0],D[2][0],D[2][2],D[0][2] = D[2][0],D[2][2],D[0][2],temp
        temp = D[0][1]
        D[0][1],D[1][0],D[2][1],D[1][2] = D[1][0],D[2][1],D[1][2],temp
    elif t == "D'":
        temp = F[2]
        F[2],R[2],B[2],L[2] = R[2],B[2],L[2],temp

        temp = D[0][0]
        D[0][0],D[0][2],D[2][2],D[2][0] = D[0][2],D[2][2],D[2][0],temp
        temp = D[0][1]
        D[0][1],D[1][2],D[2][1],D[1][0] = D[1][2],D[2][1],D[1][0],temp

#종료
def q():
    print('bye~')
    end = time.time()
    start_end = time.ctime(end - start)
    print('경과시간:', str(start_end)[14:19])
    print("조작갯수:", cnt)
    print('이용해주셔서 감사합니다. 뚜뚜뚜.')
    exit()

F=[ ['G']*3 for _ in range (3) ]
R=[ ['R']*3 for _ in range (3) ]
U=[ ['W']*3 for _ in range (3) ]
B=[ ['B']*3 for _ in range (3) ]
L=[ ['O']*3 for _ in range (3) ]
D=[ ['Y']*3 for _ in range (3) ]
inp=0
cnt=0
while inp!='Q':
    cmd=list(map(str,input("CUBE>")))


    #cmd(명령어)안의 "'" 결합 후 제거
    while "'" in cmd:
        if "'" in cmd:
            cmd[cmd.index("'")-1]+="'"
            cmd.pop(cmd.index("'"))
    #cmd(명령어)안의 "2" 결합 후 제거
    while "2"in cmd:
        if "2" in cmd:
            cmd[cmd.index("2")-1]+="2"
            cmd.pop(cmd.index("2"))
#명령어 구현 시작
    for i in range(len(cmd)):
        inp=cmd.pop(0)

#명령어 'Q'입력 시 끝
        if inp=="Q":
            q()

#명령어 구현
        print(inp)

        # scramble 기능
        if inp == 's':
            #조작개수 초기화
            cnt=0

            #컬러 리스트를 shuffle통해 섞어줌.
            color = ["O", "G", "R", "B", "W", "Y"]
            random.shuffle(color)

            c = color.pop()
            F = [[c] * 3 for _ in range(3)]

            c = color.pop()
            R = [[c] * 3 for _ in range(3)]

            c = color.pop()
            U = [[c] * 3 for _ in range(3)]

            c = color.pop()
            D = [[c] * 3 for _ in range(3)]

            c = color.pop()
            L = [[c] * 3 for _ in range(3)]

            c = color.pop()
            B = [[c] * 3 for _ in range(3)]

            # 모든 기능 중 랜덤으로 24번 회전시켜줌
            r = ["F", "F'", "B", "B'", "R", "R'", "L", "L'", "U", "U'", "D", "D'"]
            for _ in range(24):
                a = random.choice(r)
                rot(a)
            start = time.time()  # 섞었으므로, start 갱신
            print(start)
            prt()

        if inp == 'F':
            rot('F')
            prt()
        if inp == 'F2':
            rot('F')
            rot('F')
            cnt+=1
            prt()

        if inp == "F'":
            rot("F'")
            prt()
        if inp == "F'2":
            rot("F'")
            rot("F'")
            cnt+=1
            prt()

        if inp == "B":
            rot("B")
            prt()
        if inp == 'B2':
            rot('B')
            rot('B')
            cnt+=1
            prt()

        if inp == "B'":
            rot("B'")
            prt()
        if inp == "B'2":
            rot("B'")
            rot("B'")
            cnt+=1
            prt()

        if inp == 'U':
            rot('U')
            prt()
        if inp == 'U2':
            rot('U')
            rot('U')
            cnt+=1
            prt()

        if inp == "U'":
            rot("U'")
            prt()
        if inp == "U'2":
            rot("U'")
            rot("U'")
            cnt+=1
            prt()

        if inp == 'D':
            rot('D')
            prt()
        if inp == 'D2':
            rot('D')
            rot('D')
            cnt+=1
            prt()

        if inp == "D'":
            rot("D'")
            prt()
        if inp == "D'2":
            rot("D'")
            rot("D'")
            cnt+=1
            prt()

        if inp == 'R':
            rot('R')
            prt()
        if inp == 'R2':
            rot('R')
            rot('R')
            cnt+=1
            prt()

        if inp == "R'":
            rot("R'")
            prt()
        if inp == "R'2":
            rot("R'")
            rot("R'")
            cnt+=1
            prt()

        if inp == 'L':
            rot('L')
            prt()
        if inp == 'L2':
            rot('L')
            rot('L')
            cnt+=1
            prt()

        if inp == "L'":
            rot("L'")
            prt()
        if inp == "L'2":
            rot("L'")
            rot("L'")
            cnt+=1
            prt()

#모든 면이 맞았는 지 판명코드
        answer=True
        for k in [F,B,R,L,U,D]:
            for i in range(3):
                for j in range(3):
                    if k[i][j] != k[1][1]:
                        answer=False
                        break
        if answer==True:
            print("축하합니다! 모든 면을 다 맞추셨습니다.")
            q()

        cnt+=1