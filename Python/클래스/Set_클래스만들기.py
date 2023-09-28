class Set:
    def __init__(self,lst): # 리스트 중복 제거
        self.data=[]
        for i in lst:
            if i not in self.data:
                self.data.append(i)

    def add(self, member):
        if member not in self.data:
            self.data.append(member)

    def discard(self,member): # Set에 member 있으면 삭제
        if member in self.data:
            self.data.remove(member)

    def clear(self): # Set에 존재하는 모든 원소 삭제
        for i in range (len(self.data)):
            self.data.pop()


    def __and__(self, other):
        res = []
        for i in self.data:
            if i in other.data:
                res.append(i)
        return Set(res)

    def __or__(self, other):
        res = []
        for i in self.data:
            res.append(i)
        for i in other.data:
            res.append(i)

        return Set(res)

    def __sub__(self, other): # 차집합 연산
        res = []
        for x in self.data:
            if x not in other.data:
                res.append(x)
        return Set(res)

    def __le__(self,other):
        for i in self.data:
            if i not in other.data:
                return False
        return True

    def __ge__(self,other):
        for i in other.data:
            if i not in self.data:
                return False
        return True

    def __contains__(self, item): # in 연산
        if item in self.data:
            return True
        return False

    def __len__(self): # 길이 반환
        return len(self.data)

    def __str__(self): # 출력 설정정
       return "{"+str(self.data).strip('[]')+"}"

    def __ior__(self,other):
        for i in other.data:
            if i not in self.data:
                self.data.append(i)
        return self

    def __iand__(self,other):
        for i in self.data:
            if i not in other.data:
                self.data.remove(i)
        return self

    def __isub__(self,other):
        for i in other.data:
            if i in self.data:
                self.data.remove(i)
        return self


a=Set([1,2,3,4])
b=Set([1,2,3,4])

print(a)
print(b)
print()

a.discard(4)
b.discard(1)
print(a)
print(b)
print()

print(len(a))
print(1 in a)
print(1 in b)
print()

print(a | b)
print(a & b)
print(a - b)
print()

print(a <= b)
print(a <= a | b)
print(a >= b)
print(a >= a & b)
print()

b.clear()
print(b)
print()

a = Set([1,2,3])
b = Set([3,4])
address_a = id(a)
a |= b
print(a)
print(address_a == id(a))
print()

a = Set([1,2,3])
b = Set([3,4])
address_a = id(a)
a &= b
print(a)
print(address_a == id(a))
print()

a = Set([1,2,3])
b = Set([3,4])
address_a = id(a)
a -= b
print(a)
print(address_a == id(a))
print()