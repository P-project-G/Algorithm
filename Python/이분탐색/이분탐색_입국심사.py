import sys
input = sys.stdin.readline

def solution(n, times):
    start = 0;
    end = times[len(times) - 1] * n;
    answer = sys.maxsize;
    while (start < end):
        sum = 0;
        mid = (start + end) // 2;

        for t in times:
            sum += mid // t;

        if sum < n:
            start = mid+1;
        else:
            end = mid;
    return end

n = 6;
times = [7,10];
print(solution(n,times));