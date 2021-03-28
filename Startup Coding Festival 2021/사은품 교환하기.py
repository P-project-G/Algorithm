# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


t = int(input())  # 테스트케이스 수
for _ in range(t):
    # N : 시즌한정음료 쿠폰의 수
    # M : 일반음료 쿠폰의 수
    N, M = map(int, input().split())
    cnt = 0  # 구매한 음료의 수

    Nmok = N // 5
    Nmod = N % 5
    Mmok = M // 7
    Mmod = M % 7

    if Nmok > Mmok:
        cnt += Mmok
        N = (Nmok - Mmok) * 5 + Nmod
        M = Mmod
    elif Nmok <= Mmok:
        cnt += Nmok
        N = Nmod
        M = (Mmok - Nmok) * 7 + Mmod

    if N < 5:
        print(cnt)

    else:
        if N >= 5 and M > 0 and N + M >= 12:
            N -= 12 - M
            M = 0
            cnt += 1
        if N >= 12:
            cnt += N // 12

        print(cnt)


"""
4
12 0
10 14
4 20
5 2147483648
"""