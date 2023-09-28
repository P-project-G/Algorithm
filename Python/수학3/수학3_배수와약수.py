while True:
    i,j=list(map(int,(input().split())))
    if i==0 and j==0:
        break

    if j%i==0:
        print("factor")
        continue
    if i%j==0:
        print("multiple")
        continue

    if i%j !=0 and j%i != 0 :
        print("neither")