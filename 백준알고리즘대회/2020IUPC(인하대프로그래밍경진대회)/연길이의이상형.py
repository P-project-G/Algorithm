mbti = input()
reverse_mbti = {"E":"I", "S":"N", "T":"F", "J":"P", "I":"E", "N":"S", "F":"T", "P":"J"}

for i in mbti:
    print(reverse_mbti[i],end="")