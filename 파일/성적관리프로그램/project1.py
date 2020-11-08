import collections
fr=open('students.txt', 'r')

temp = list(map(lambda x: x.split(), fr))
stu_dic=collections.defaultdict()
for no,name,name2,mid,fin in temp:
    avg=(int(mid)+int(fin))/2
    if avg >= 90 :
        rank='A'
    elif avg >= 80 :
        rank='B'
    elif avg >= 70 :
        rank='C'
    elif avg >= 60 :
        rank='D'
    else:
        rank='F'
    stu_dic[no] = [name+" "+name2,mid,fin, avg, rank ]

stu_dic=dict(stu_dic)

#초기 출력
print('%10s\t%15s\t%13s\t%7s\t%12s\t%8s' % ("Student", "Name", "Midterm", "Final", "Average", "Grade"))
print("------------------------------------------------------------------------------")
for i in sorted(stu_dic.items(),key=lambda x: x[1][3],reverse=True):
    print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4]))

print()
# 세부사항1, 명령어 모음
print("┌-------------------------------------------------┐")
print("│                      Manual                     │")
print("├-------------------------------------------------┤")
print("│"+'%15s'%("show :")+'%30s'%("All student information output")+'%4s'%(' ')+'|')
print("│"+'%15s'%("search :")+'%30s'%("Search for specific students")+'%4s'%(' ')+'|')
print("│"+'%15s'%("changescore :")+'%30s'%("Modify score")+'%4s'%(' ')+'|')
print("│"+'%15s'%("add :")+'%30s'%("Add students")+'%4s'%(' ')+'|')
print("│"+'%15s'%("searchgrade :")+'%30s'%("Grade search")+'%4s'%(' ')+'|')
print("│"+'%15s'%("remove :")+'%30s'%("Delete a specific student")+'%4s'%(' ')+'|')
print("│"+'%15s'%("quit :")+'%30s'%("quit")+'%4s'%(' ')+'|')
print("│"+'%15s'%("tip :")+'%30s'%("Recall manual")+'%4s'%(' ')+'|')
print("│"+'%45s'%(" ")+'%4s'%(' ')+'|')
print("│"+'%45s'%("made by. Park GunHyeong")+'%4s'%(' ')+'|')
print("└-------------------------------------------------┘")
print("")
while True:
    print("#",end=" ")
    inp=input()
    if inp=='quit': #  파일을 종료할 때
        print("Save data?[yes/no]",end=" ")
        inp = input()
        if inp == 'yes':
            print("File name:",end=" ")
            file_name = input()

            # file_name을 쓰기형식으로, f에 저장
            f = open(file_name,'w')
            for i in sorted(stu_dic.items(),key=lambda x: x[1][3],reverse=True):
                # write할 때 한번에 하기 위해서 모든 아이템이 합쳐진 line을 만들어줌
                line = ('%10s\t%15s\t%10s\t%10s\t%10s\t%10s\n' % (i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4]))
                f.write(line)
            f.close()
            exit()

        else:
            exit()

    if inp=='show': # 현재 성적순 정렬 출력
        print('%10s\t%15s\t%13s\t%7s\t%12s\t%8s' % ("Student", "Name", "Midterm", "Final", "Average", "Grade"))
        print("------------------------------------------------------------------------------")
        for i in sorted(stu_dic.items(), key=lambda x: x[1][3], reverse=True):
            print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4]))

    if inp=='search': # 학번 검색후, 검색한 학번 정보 출력
        print("Student ID:", end=" ")

        # 세부사항2, 만약 학번이 아닌 것을 검색했을 때
        # int(input())을 통해 숫자만 입력받을 수 있게끔 설정.
        # 숫자가 아닌 다른 것을 입력한다면, 예외처리로 정확한 학번을 입력해달라고 출력
        try:
            id_search = int(input())
            id_search = str(id_search)
        except:
            print("Please enter class number correctly.")

        # 예외처리
        try:
            i=stu_dic[id_search]
            print('%10s\t%15s\t%13s\t%7s\t%12s\t%8s' % ("Student", "Name", "Midterm", "Final", "Average", "Grade"))
            print("------------------------------------------------------------------------------")
            print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (id_search, i[0], i[1], i[2], i[3], i[4]))
        except:
            print("NO SUCH PERSON.")

    if inp=='changescore': # 점수변경할 때
        print("Student ID:", end=" ")
        id_search = input() # 변경할 학생 검색

        # 예외처리 (검색한 학번이 존재하지 않을 때 except 수행)
        try:
            i=stu_dic[id_search]
            print("Mid/Final?", end=" ")
            choice=input() # mid, final 둘 중 하나 입력받아야함.
            #mid, final이 아닐 시 continue로 진행

            if choice == 'mid':
                print("Input new score:",end=" ")
                new_sco=int(input())
                if new_sco>100: # 0 ~ 100이 아닐 시 continue로 진행
                    continue
                else:
                    print('%10s\t%15s\t%13s\t%7s\t%12s\t%8s' % (
                    "Student", "Name", "Midterm", "Final", "Average", "Grade"))
                    print("------------------------------------------------------------------------------")
                    print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (id_search, i[0], i[1], i[2], i[3], i[4]))

                    print("Score changed.")

                    # 해당 학생의 mid점수 업데이트과정 i[0] i[1] i[2] i[3] i[4]는 순서대로 name, mid, fin, avg, rank
                    i = stu_dic[id_search]
                    i[1]=str(new_sco)
                    i[3] = (int(i[1]) + int(i[2])) / 2
                    if i[3] >= 90:
                        i[4] = 'A'
                    elif i[3] >= 80:
                        i[4] = 'B'
                    elif i[3] >= 70:
                        i[4] = 'C'
                    elif i[3] >= 60:
                        i[4] = 'D'
                    else:
                        i[4] = 'F'
                    stu_dic[id_search] = [i[0], i[1], i[2], i[3], i[4]]
                    print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (id_search, i[0], i[1], i[2], i[3], i[4]))
            elif choice == 'final':
                print("Input new score:",end=" ")
                new_sco=int(input())
                if new_sco>100:
                    continue
                else:
                    print('%10s\t%15s\t%13s\t%7s\t%12s\t%8s' % (
                    "Student", "Name", "Midterm", "Final", "Average", "Grade"))
                    print("------------------------------------------------------------------------------")
                    print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (id_search, i[0], i[1], i[2], i[3], i[4]))

                    print("Score changed.")

                    # 해당 학생의 final 점수 업데이트 과정 i[0] i[1] i[2] i[3] i[4]는 순서대로 name, mid, fin, avg, rank
                    i = stu_dic[id_search]
                    i[2]=str(new_sco)
                    i[3] = (int(i[1]) + int(i[2])) / 2
                    if i[3] >= 90:
                        i[4] = 'A'
                    elif i[3] >= 80:
                        i[4] = 'B'
                    elif i[3] >= 70:
                        i[4] = 'C'
                    elif i[3] >= 60:
                        i[4] = 'D'
                    else:
                        i[4] = 'F'
                    stu_dic[id_search] = [i[0], i[1], i[2], i[3], i[4]]
                    print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (id_search, i[0], i[1], i[2], i[3], i[4]))
            else:
                continue
        except:
            print("NO SUCH PERSON.")

    if inp=='add': # 학생 추가할 때
        print("Student ID:", end=" ")
        id_search = input() # 추가할 학번 입력
        # 이미 존재하는 학번이라면 try, 아니라면 에러발생 유도하여 except로 실행

        try:
            if stu_dic[id_search]:
                print("ALREADY EXISTS.")
        except:
            print("Name:", end=" ")
            name = input()
            print("Midterm Score:", end=" ")
            mid = input()
            print("Final Score:", end=" ")
            fin = input()

            avg = (int(mid) + int(fin)) / 2
            if avg >= 90:
                rank = 'A'
            elif avg >= 80:
                rank = 'B'
            elif avg >= 70:
                rank = 'C'
            elif avg >= 60:
                rank = 'D'
            else:
                rank = 'F'
            stu_dic[id_search] = [name, mid, fin, avg, rank]
            print("Student added.")

    if inp=='searchgrade': # 등급 검색할 때
        print("Grade to search:",end=" ")
        grade=input()

        # grade가 A,B,C,D,F에 존재하면 pass, 아니면 continue로 넘어감
        if grade in ['A','B','C','D','F']:
            pass
        else:
            continue

        #gradelst로 존재하고 있는 모든 Grade 묶어줌
        gradelst=list(map(lambda x: x[1][4], stu_dic.items()))

        # gradelst.index(grade), 만약 grade가 gradelst안에 존재한다면,
        # 인덱스가 나올 것이고 아니면 에러가 날 것임 이를 유도하여 try, except 사용
        # 존재하지 않으면, NO RESULTS를 출력
        # 존재한다면 진행
        try:
            gradelst.index(grade)
            print('%10s\t%15s\t%13s\t%7s\t%12s\t%8s' % (
                "Student", "Name", "Midterm", "Final", "Average", "Grade"))
            print("------------------------------------------------------------------------------")
            for i in stu_dic.items():
                if i[1][4] == grade:
                    print('%10s\t%15s\t%10s\t%10s\t%10s\t%10s' % (i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4]))
        except:
            print("NO RESULTS.")
            continue

    if inp == 'remove': # 특정 학생 삭제할 때
        # stu_dic가 존재하지 않는다면, List is empty 출력 후 continue
        if not stu_dic:
            print("List is empty.")
            continue

        #존재한다면, 진행
        else:
            print("Student ID:",end=" ")
            id_search = input()

            # stu_dic.pop(id_search) 만약 stu_dic에서
            # id_search라는 key값을 찾을 수 없을 때 except
            # key값이 존재한다면 pop(id_search)로 해당 키 삭제
            try:
                stu_dic.pop(id_search)
                print("Student removed.")
            except:
                print("NO SUCH PERSON.")
    if inp == 'tip':
        print("┌-------------------------------------------------┐")
        print("│                      Manual                     │")
        print("├-------------------------------------------------┤")
        print("│" + '%15s' % ("show :") + '%30s' % ("All student information output") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("search :") + '%30s' % ("Search for specific students") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("changescore :") + '%30s' % ("Modify score") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("add :") + '%30s' % ("Add students") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("searchgrade :") + '%30s' % ("Grade search") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("remove :") + '%30s' % ("Delete a specific student") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("quit :") + '%30s' % ("quit") + '%4s' % (' ') + '|')
        print("│" + '%15s' % ("tip :") + '%30s' % ("Recall manual") + '%4s' % (' ') + '|')
        print("│" + '%45s' % (" ") + '%4s' % (' ') + '|')
        print("│" + '%45s' % ("made by. Park GunHyeong") + '%4s' % (' ') + '|')
        print("└-------------------------------------------------┘")