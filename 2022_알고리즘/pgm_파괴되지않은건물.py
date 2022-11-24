def solution(board, skill):
    answer = 0

    skBuild = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for s in skill:
        skBuild[s[1]][s[2]] += -s[5] if s[0] == 1 else s[5]
        skBuild[s[1]][s[4] + 1] += s[5] if s[0] == 1 else -s[5]
        skBuild[s[3] + 1][s[4] + 1] += -s[5] if s[0] == 1 else s[5]
        skBuild[s[3] + 1][s[2]] += s[5] if s[0] == 1 else -s[5]

    for r in range(len(skBuild) - 1):
        for c in range(len(skBuild[0]) - 1):
            skBuild[r][c + 1] += skBuild[r][c]

    for c in range(len(skBuild[0]) - 1):
        for r in range(len(skBuild) - 1):
            skBuild[r + 1][c] += skBuild[r][c]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += skBuild[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer