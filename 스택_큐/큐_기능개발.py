"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에
뒤에 있는기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.

배포는 하루에 한 번만 할 수 있으며,
하루의 끝에 이루어진다고 가정합니다.
예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]

[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
"""
from collections import deque
def solution(progresses, speeds):
    day = []
    ans = []
    for i,j in zip(progresses,speeds): # i = progrresses를 돌고, j = speeds를 돌아라.
        if (100-i)%j != 0: # 100-i를 j로 나눴을 때 나머지가 0 이 아니면,
            day.append( (100-i) // j + 1)
        else: # 100-i를 j로 나눴을 때 나머지가 0 이면,
            day.append( (100-i) // j)
    print(day)
    dayq = deque(day) # day를 deque화, dayq

    while dayq: # dayq가 존재한다면 계속,
        a = dayq[0]
        cnt = 0
        for i in dayq:
            if a >= i:
                cnt += 1
            else:
                break

        for i in range(cnt): # cnt만큼 dayq에서 pop
            dayq.popleft()

        ans.append(cnt) # cnt를 ans에 추가

    return ans

print(solution([95, 90, 99, 99, 80, 99],[1,1,1,1,1,1]))