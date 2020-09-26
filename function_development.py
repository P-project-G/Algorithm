def solution(progresses, speeds):
    answer = []
    result=[]
    for i,j in zip(progresses,speeds):
        cnt=0
        while i<100:
            i+=j
            cnt+=1
        result.append(cnt)

    cnt=0
    for i in range (len(result)):
        if cnt>1:
            cnt-=1
            continue
        cnt=0
        for j in range (i,len(result)):
            if result[i]<result[j]:
                cnt+=1
                answer.append(cnt-1)
                break
            if result[i]>=result[j]:
                for k in range (j,len(result)):
                    if result[j]>=result[k]:
                        cnt+=1
                    else:
                        break
                answer.append(cnt)
                break
    return answer

#progresses=[93,30,55]
#speeds=[1,30,5]
#progresses=[95,90,99,99,80,99]
#speeds=[1,1,1,1,1,1]
progresses=[40,93,30,55,60,65]
speeds=[60,1,30,5,10,7]
print(solution(progresses,speeds))