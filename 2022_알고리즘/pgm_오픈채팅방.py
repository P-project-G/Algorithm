def solution(record):
    answer = []

    chatUserDic = {}
    for rec in record:
        r = rec.split()

        # 등장 or 변경
        if len(r) == 3:
            cmd, uId, nknm = r[0], r[1], r[2]
            if cmd == "Enter":
                chatUserDic[uId] = nknm
                answer.append([uId, "Enter"])
            if cmd == "Change":
                chatUserDic[uId] = nknm
        # 떠남
        else:
            cmd, uId = r[0], r[1]
            answer.append([uId, "Leave"])

    ans = []
    for a in answer:
        if a[1] == "Enter":
            ans.append(chatUserDic[a[0]] + "님이 들어왔습니다.")
        else:
            ans.append(chatUserDic[a[0]] + "님이 나갔습니다.")

    return ans