import time

N,K = map(int,input().split())

start = time.time()
cnt = 0

#"""
while N != 1:
    if N%K == 0:
        N = N/K
        cnt += 1
    else:
        tmp = N%K
        if tmp >= N:
            cnt += tmp-1
            N = N-tmp+1
        else:
            N = N-tmp
            cnt += tmp
print(cnt)
#"""
# time: 0.0010004043579101562

"""
while N != 1:
    if N%K == 0:
        N = N/K
        cnt += 1
    else:
        N -= 1
        cnt += 1
print('cnt',cnt)
"""
# time: 1.12358

print("time:",time.time()-start)

"""
시간초과 코드
10000000000000 9999995777277
"""