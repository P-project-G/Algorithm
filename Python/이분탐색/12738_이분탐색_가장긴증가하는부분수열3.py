n = int(input())
arr = list(map(int,input().split()))
LIS = [arr[0]]

for i in arr:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        low = 0
        high = len(LIS)-1
        while low < high:
            mid = (low+high)//2
            if LIS[mid] < i:
                low = mid+1
            elif LIS[high] > i:
                high = mid
            else:
                low = high = mid
                break
        LIS[high] = i
print(len(LIS))

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	512 MB	4804	2855	2300	64.210%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
"""
