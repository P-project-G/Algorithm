def solution(n, lost, reserve):
    set_lost=list(set(lost)-set(reserve))
    set_reserve=list(set(reserve)-set(lost))
    print(set_lost,set_reserve)
    answer=n-len(set_lost)
    for i in range (len(set_reserve)):
        if set_reserve[i]-1 in set_lost:
            set_lost.remove(set_reserve[i]-1)
            answer+=1
        elif set_reserve[i]+1 in set_lost:
            set_lost.remove(set_reserve[i]+1)
            answer+=1
    return answer

if __name__ == '__main__':
    n=5
    lost=[1,2,4]
    reserve=[1,3,5]

    print(solution(n,lost,reserve))