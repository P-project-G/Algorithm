from copy import deepcopy
from collections import deque
n = int(input())
s = []
max_value = 0
def dfs(dist, maps, cnt):
    global max_value
    copy_maps = deepcopy(maps)
    if dist == 0:
        for i in range(n):
            temp = deque()
            for j in range(n):
                if copy_maps[j][i] != 0:
                    temp.append(copy_maps[j][i])
            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num + 1] *= 2
                    num += 2
                else:
                    num += 1
            num = 0
            while num < n:
                if temp:
                    a = temp.popleft()
                    if a != 0:
                        copy_maps[num][i] = a
                        num += 1
                else:
                    copy_maps[num][i] = 0
                    num += 1
    elif dist == 1:
        for i in range(n):
            temp = deque()
            for j in range(n - 1, -1, -1):
                if copy_maps[j][i] != 0:
                    temp.append(copy_maps[j][i])
            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num + 1] *= 2
                    num += 2
                else:
                    num += 1
            num = n - 1
            while num > -1:
                if temp:
                    a = temp.popleft()
                    if a != 0:
                        copy_maps[num][i] = a
                        num -= 1
                else:
                    copy_maps[num][i] = 0
                    num -= 1
    elif dist == 2:
        for i in range(n):
            temp = deque()
            for j in range(n - 1, -1, -1):
                if copy_maps[i][j] != 0:
                    temp.append(copy_maps[i][j])
            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num + 1] *= 2
                    num += 2
                else:
                    num += 1
            num = n - 1
            while num > -1:
                if temp:
                    a = temp.popleft()
                    if a != 0:
                        copy_maps[i][num] = a
                        num -= 1
                else:
                    copy_maps[i][num] = 0
                    num -= 1
    elif dist == 3:
        for i in range(n):
            temp = deque()
            for j in range(n):
                if copy_maps[i][j] != 0:
                    temp.append(copy_maps[i][j])
            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num + 1] *= 2
                    num += 2
                else:
                    num += 1
            num = 0
            while num < n:
                if temp:
                    a = temp.popleft()
                    if a != 0:
                        copy_maps[i][num] = a
                        num += 1
                else:
                    copy_maps[i][num] = 0
                    num += 1
    if cnt == 5:
        for i in range(n):
            max_value = max(max_value, max(copy_maps[i]))
        return
    dfs(0, copy_maps, cnt + 1)
    dfs(1, copy_maps, cnt + 1)
    dfs(2, copy_maps, cnt + 1)
    dfs(3, copy_maps, cnt + 1)
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(4):
    dfs(i, s, 1)
print(max_value)