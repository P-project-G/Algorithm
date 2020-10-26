def solution(s,idx):
    answer=[]
    key,val=[],[]

    stack=[]
    for id,letter in enumerate(s):
        if letter == '{':
            stack.append(id)

        elif letter == '}':
            if stack:
                rev_idx=stack.pop()
                key.append(rev_idx)
                key.append(id)
                val.append(id)
                val.append(rev_idx)

            else:
                stack.append(id)

    key_value=[key,val]
    dic=dict(zip(*key_value))

    for i in idx:
        answer.append(dic[i])
    return answer

s="{cpp{java}}{python}"
idx=[0,4,9,10,11,18]

#s="ab{}cd{efg{}h}{ij}"
#idx=[3,6,11,3,14,11]
print(solution(s,idx))