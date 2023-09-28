from collections import Counter
def solution(participant, completion):
    participant=Counter(participant)
    completion=Counter(completion)
    answer = list((participant-completion).keys())
    return answer[0]

if __name__ == '__main__':
    participant=["leo","kiki","eden","kiki"]
    completion=["eden","kiki","leo"]
    print(solution(participant,completion))
