"""
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다.
디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다.
가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

프로그래머스
문제링크
https://programmers.co.kr/learn/courses/30/lessons/42627
"""

import heapq
def solution(jobs):
    length = len(jobs)
    answer, endtime, time, cnt, queue = 0, -1, 0, 0, []

    while cnt < length:
        for i in jobs:
            if endtime < i[0] <= time:
                answer += (time - i[0])
                heapq.heappush(queue, i[1])

        if queue:
            answer += len(queue) * queue[0]
            endtime = time
            time += heapq.heappop(queue)
            cnt += 1

        else:
            time += 1

    return int(answer / length)

if __name__ == '__main__':
    jobs=[[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))