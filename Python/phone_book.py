'''
    전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
    어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록
    solution 함수를 작성해주세요.
'''

def solution(phone_book):
    for i in phone_book:
        cnt=0
        for j in range (len(phone_book)):
            if i.startswith(phone_book[j]):
                cnt+=1
                if cnt>1:
                    return False
    return True

if __name__ == '__main__' :
    phone_book=["119","1195421","9115"]
    print(solution(phone_book))