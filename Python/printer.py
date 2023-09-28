"""
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도
   존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고
중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다.
위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴
배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의
어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지
return 하도록 solution 함수를 작성해주세요.
"""
def solution(priorities, location):
    location=[priorities[location],location]
    result=[]
    for i in range (len(priorities)):
        priorities[i]=[priorities[i],i]

    while True:
        temp=priorities.pop(0)
        if not priorities:
            result.append(temp)
            break

        if temp[0]<max(priorities,key=lambda x:x[0])[0]:
            priorities.append(temp)
        else:
            result.append(temp)

    answer=result.index(location)
    return answer+1

if __name__=='__main__':
    priorities=[1,1,9,1,1,1]
    location=0
    print(solution(priorities,location))