N=int(input())
vaild = [ input() for i in range (N) ]

stack=[]
for i in vaild:
    for vps in range (len(i)):
        if i[vps] == '(' :
            if ')' in stack[vps:]:
                stack.remove(')')
                continue
            else:
                stack.append('(')

        if i[vps] == ')' :
            if '(' in stack[:vps]:
                stack.remove('(')
                continue
            else:
                stack.append(')')
                continue

    if stack:
        print("NO")
    else:
        print("YES")
    stack=[]