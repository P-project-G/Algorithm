import heapq
def solution(scoville, K):
    answer=0
    scoville.sort()
    while True:
        if scoville[0]>=K:
            break
        heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville))*2)
        answer+=1
        if len(scoville)==1 and scoville[0]<K:
            return -1
    return answer

if __name__=='__main__':
    scoville=[1,2,3,9,10,12]
    K=7
    print(solution(scoville,K))