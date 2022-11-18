def convert(num, base):
    temp = "0123456789ABCDEF"

    div,mod = divmod(num, base)

    if div == 0:
        return temp[mod]
    else:
        return convert(div, base) + temp[mod]

def solution(n, t, m, p):
    answer = ''

    num = [convert(i, n) for i in range(m * t)]
    num = "".join(num)

    # t가 10개면
    # 참가하는 인원이 3명
    # 2진수라면, 2번째라면
    # 0 1 10 11 100 101 110 111
    # 0, 1v, 1, 0, 1v, 1, 1, 0v, 0, 1, 0v, 1, 1, 1v, 0, 1, 1v, 1

    cnt = 0
    numIdx = 0
    # print(num)
    while True:
        if cnt == t:
            break
        answer += num[p - 1]
        p = p + m
        cnt += 1

    return answer