"""
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
"""

def solution(bridge_length, weight, truck_weights):
    object=len(truck_weights)
    pass_truck=[]
    arrive_truck=[]
    time=0
    time_sheet=[]

    while len(arrive_truck)!=object:
        time+=1

        if truck_weights and truck_weights[0]+sum(pass_truck)<=weight:
            pass_truck.append(truck_weights.pop(0))
            time_sheet.append(time)

        if pass_truck and (time-time_sheet[0]+1)%bridge_length==0:
            time_sheet.pop(0)
            arrive_truck.append(pass_truck.pop(0))
    answer=time+1

    return answer

if __name__=='__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    bridge_length = 100
    weight = 100
    truck_weights = [10]

print(solution(bridge_length,weight,truck_weights))