def DFS(id, numbers, target):
    if id == len(numbers) and target == 0:
        return 1
    elif id == len(numbers):
        return 0
    else:
        return DFS(id + 1, numbers, target + numbers[id]) + DFS(id + 1, numbers, target - numbers[id])

def solution(numbers, target):
    return DFS(0, numbers, target)

numbers=[1,1,1,1,1]
target=3
print(solution(numbers,target))