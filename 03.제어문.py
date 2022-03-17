# 조건문 : if
money=False
if money:
    print('택시를 타고 가라.')
else:
    print('걸어가라')

money=2000
if money >=3000:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# if문 뒤에는 불자료형이 들어가는 것임.
if True:
    print('택시를 타고 가라')
else:
    print('걸어가라')

#not True = False / not False = True
if not True:
    print('택시를 타고 가라')
else:
    print('걸어가라')

print(' '*50)

#연산자 사용법 (그리고 / 또는)
#or |은 둘 중 하나만 만족하면 True.
money=2000
card=1
if False or True:
    print('택시를 타고 가라')
else:
    print('걸어가라')

if False | True:
    print('택시를 타라')
else:
    print('걸어가라')

#and & 는 모두 만족해야 True.
if False and True:
    print('택시를 타고 가라')
else:
    print('걸어가라')

if False & True:
    print('택시를 타고 가라')
else:
    print('걸어가라')


print(' '*50)
# x in s / x not in s

if 1 in [1,2,3]:
    print('참')
else:
    print('거짓')

if 1 not in [1,2,3]:
    print('참')
else:
    print('거짓')
# >>> 1은 리스트 안에 존재하므로 not in 이 아니다.

#조건문에서 아무 일도 하지 않게 설정하기. pass >>> True인 경우 결과 X
pocket = ['paper','cell phone', 'money']
if 'money' in pocket:
    pass
else:
    print('걸어가라')

#조건이 여러개 : 다중 조건 판단 elif
# ex) 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper','cell phone']
card = True
if 'money' in pocket:
    print('택시를 타라')
elif card:
    print('택시를 타라')
else:
    print('걸어가라')
# >>> card = True 이므로 두번째에 print가 실행된 것임.

#조건부 표현식
#조건부 표현식 쓰기 전.
score = 70
if score >= 60:
    message = 'success!'
else:
    message = 'failure...'
print(message)

#조건부 표현식을 쓰게 되면, 다음과 같다. >>> 동일한 구문
# 성공일 때의 결과 먼저 써준다. 그 다음 조건식을 써준다.
score = 70
message = 'success!' if score >= 60 else 'failure...'
print(message)
# >>> else 뒤에 조건문 안써주면 구문 오류 나니 주의해야 한다.

print(' '*50)


# 반복문 : while
# >>> while문 뒤에 조건이 True인 이상 계속 진행. False가 되면 stop.
# ex) 열 번 찍어 안 넘어가는 나무 없다.
treehit = 0
while treehit < 10:
    treehit=treehit+1
    print('나무를 %d번 찍었습니다.'%treehit)
    if treehit==10:
        print('나무 넘어갑니다.')

print(' '*50)

# break : while문 stop
coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee -1
    print('남은 커피의 양은 %d 입니다.'%coffee)
    if not coffee:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break

# continue : while문 처음으로 돌아가기
a = 0
while a < 10:
    a=a+1
    if a % 2 ==0:
        continue
    print(a)

# 무한 루프 : 무한히 반복하기 >>> ctrl + c 를 눌러야 무한루프에서 나올 수 있다.
# while True:
#   print ()


print(' '*50)

# 반복문 : for
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print(' ')

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
    print(first)
    print(last)
    print(' ')

# ex) 60점이 넘으면 합격이고 그렇지 않으면 불합격
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number=number+1
    if mark >= 60:
        print('%d번 학생은 합격입니다.'%number)
    else:
        print('%d번 학생은 불합격입니다.'%number)

print(' ')

# for문 continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number=number+1
    if mark<60:
        continue
    print('%d번 학생 축하합니다. 합격입니다.'%number)

#for문 range
for i in range (1,11):
    print(i)
# >>> range(a,b) : a이상 b미만 출력

# ex) 1부터 10까지 더하여라.
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)

# ex) 구구단 구현하기.
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="")
    print(' : %d단'%i)

#>>> print 함수의 옵션 : end="" 값이 연속적으로 연결되어 나옴

#리스트 내포
# >>> 결국 추가하고 싶은 것을 맨 앞에 입력하고 조건을 순서대로 뒤에 입력
# result = [num*3 for num in a]
# result=[]
# for num in a:
# result.append(num*3)

a=[10,11,12,13,14,15]
result = [num*3 for num in a if num%2 == 0]
print(result)

result=[]
for num in a:
    if num % 2 == 0:
        result.append(num*3)
print(result)
