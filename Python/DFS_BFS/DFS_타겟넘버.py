def DFS(idx,numbers,target):
    if idx == len(numbers)-1:
        if target==0:
            return 1
        else:
            return 0
    else:
        return DFS(idx+1,numbers,target-numbers[idx+1]) + DFS(idx+1,numbers,target+numbers[idx+1])




if __name__ == '__main__' :
    numbers=[1,1,1,1,1]
    target=3
    print(DFS(-1,numbers,target))