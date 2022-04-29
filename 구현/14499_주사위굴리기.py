#    0
# 1  2  3
#    4
#    5
def goOK(direction):
    global curPos

    dr, dc = move[direction-1]

    if (curPos[0] + dr >= n or curPos[0] + dr < 0 or curPos[1] + dc >= m or curPos[1] + dc < 0):
        return False
    else:
        return True

def changeNum(direction):
    global curPos
    dr, dc = move[direction-1]

    if diceMap[curPos[0] + dr][curPos[1] + dc] == 0:
        diceMap[curPos[0] + dr][curPos[1] + dc] = dice[5]
    else:
        dice[5] = diceMap[curPos[0] + dr][curPos[1] + dc]
        diceMap[curPos[0] + dr][curPos[1] + dc] = 0

    curPos = [curPos[0] + dr, curPos[1] + dc]

def goSouth(dice):
    temp = dice[0]
    dice[0] = dice[5]
    dice[5] = dice[4]
    dice[4] = dice[2]
    dice[2] = temp
    changeNum(4)
    return dice

def goNorth(dice):
    temp = dice[5]
    dice[5] = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[4]
    dice[4] = temp
    changeNum(3)
    return dice

def goWest(dice):
    temp = dice[2]
    dice[2] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp
    changeNum(2)
    return dice

def goEast(dice):
    temp = dice[2]
    dice[2] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[3]
    dice[3] = temp
    changeNum(1)
    return dice


# 1 East
# 2 West
# 3 North
# 4 South
move = [[0,1], [0,-1], [-1,0], [1,0]]

n,m,x,y,k = map(int,input().split())
diceMap = []
for r in range (n):
    diceMap.append(list(map(int,input().split())))

command = list(map(int,input().split()))

dice = [0,0,0,0,0,0]
curPos = [x,y]
ans = []

for cmd in command:

    # 이동할 수 있으면 커맨드 실행
    if goOK(cmd):
        if cmd==1:
            dice = goEast(dice)
        elif cmd==2:
            dice = goWest(dice)
        elif cmd==3:
            dice = goNorth(dice)
        else:
            dice = goSouth(dice)
        ans.append(dice[2])

for a in ans:
    print(a)
