# 문제링크
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=javascript

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
storage = [] # 인형을 담고있는 리스트
result = 0 # 정답

# i는 행, j는 열
while moves:
    crane = moves.pop(0)
    for i in range (len(board)):
        if board[i][crane-1] == 0:
            continue
        elif board[i][crane-1] != 0:
            storage.append(board[i][crane-1])
            board[i][crane-1] = 0
            break

    if len(storage) >= 2:
        if storage[-1] == storage[len(storage)-2]:
            storage.pop()
            storage.pop()
            result += 2
print(result)