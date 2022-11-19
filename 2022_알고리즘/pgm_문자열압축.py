def solution(s):
    answer = 99999
    for cut in range(1, len(s) // 2 + 2):
        res = ""
        temp = s[:cut]
        equalCnt = 1
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == temp:
                equalCnt += 1
            else:
                if equalCnt == 1:
                    res += temp
                else:
                    res += str(equalCnt) + temp
                temp = s[i:i + cut]
                equalCnt = 1

        if equalCnt == 1:
            res += temp
        else:
            res += str(equalCnt) + temp

        answer = min(answer, len(res))

    return answer