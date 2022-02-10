#딕셔너리 자료형
dic = {'name':'haeun', 'age':25}
print(dic['name'])

#딕셔너리 자료형에 키 추가하기
dic['height']=150
print(dic)

a={'딸':'김하은','아빠':'김현수','엄마':'이석정','아들':'김태균'}
print(a.keys())
print(a.values())
print(a.items())
print(' '*50)

for v in a.items():
    print(v)
print(' '*50)

for n in a.values():
    print(n)
print(' '*50)

for m in a.keys():
    print(m)
print(' '*50)

for m,n in a.items():
    print("key is :" +m)
    print("value is :" +n)
print(' '*50)


print(a.get('이모'))
print(a.get('이모','기입x')) #키가 없는 경우 '기입x'로 리턴하라.

print('이모' in a)
print('딸' in a)

print(' '*50)

#집합 자료형
s1=set([1,2,3])
s2={1,2,3}
print(type(s1))
print(type(s2))

print(' '*50)

#리스트에서 집합으로 변환
l=[1,2,2,3,3,3,4,5]
newlist=list(set(l))
print(newlist)

#튜플에서 집합으로 변환
t=(1,2,2,3,4,5,5)
newtuple=tuple(set(t))
print(newtuple)