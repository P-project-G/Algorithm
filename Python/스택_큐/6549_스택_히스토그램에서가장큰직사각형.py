import sys
input = sys.stdin.readline

while True:
    histogram = list(map(int,input().split()))
    if histogram == [0]:
        break
    length = histogram.pop(0)
    mx = 0
    stack = []

    for i in range (length):
        while stack and histogram[stack[-1]] > histogram[i]:
            idx = stack.pop()

            if stack:
                width = i - stack[-1] -1
            else:
                width = i

            if mx < width*histogram[idx]:
                mx = width*histogram[idx]
        stack.append(i)

    while stack:
        idx = stack.pop()

        if stack:
            width = length - stack[-1] - 1
        else:
            width = length

        if mx < width * histogram[idx]:
            mx = width * histogram[idx]

    print(mx)