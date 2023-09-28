def distance(hand,num):
    phone = {'1':[0,0], '2':[0,1], '3':[0,2],
             '4':[1,0], '5':[1,1], '6':[1,2],
             '7':[2,0], '8':[2,1], '9':[2,2],
             '*':[3,0], '0':[3,1], '#':[3,2]}
    hand_arr = phone[hand]
    num_arr = phone[num]
    return abs(hand_arr[0] - num_arr[0]) + abs(hand_arr[1] - num_arr[1])


def solution(numbers, hand):
    answer=""
    left,right = '*', '#'

    for i in numbers:

        if i in [1,4,7]:
            left=str(i)
            answer += 'L'

        if i in [3,6,9]:
            right=str(i)
            answer += 'R'

        if i in [2,5,8,0]:
            left_num = distance(left,str(i)) # 왼쪽손으로부터 거리
            right_num = distance(right,str(i)) # 오른쪽손으로부터 거리
            if left_num > right_num:
                right=str(i)
                answer += 'R'
            elif left_num < right_num:
                left=str(i)
                answer += 'L'
            else:
                if hand=='left':
                    left=str(i)
                    answer += 'L'
                else:
                    right=str(i)
                    answer += 'R'

    return answer

numbers=[1,3,4,5,8,2,1,4,5,9,5]
hand="right"

#numbers=[7,0,8,2,8,3,1,5,7,6,2]
#hand="left"

#numbers=[1,2,3,4,5,6,7,8,9,0]
#hand="right"

print(solution(numbers,hand))


"""
문제링크
https://programmers.co.kr/learn/courses/30/lessons/67256
"""