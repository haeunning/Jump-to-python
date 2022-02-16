# 프로그램의 입력과 출력, 함수

# 04-1 함수
#함수 정의
def sum(a,b):
    result=a+b
    return result
#함수 호출 (함수 사용)
print(sum(1,2))

#입력값이 없는 함수
def say():
    return 'Hi'
print(say())

print('-'*50)

#결과값이 없는 함수
def sum(a,b):
    print('%d,%d의 합은 %d입니다.'%(a,b,a+b))
sum(1,2)
#>>>1,2의 합은 3입니다.
print(sum(1,2))
#>>>1,2의 합은 3입니다.
# >>> def에 할당하는 return이 없기 때문이다. = 결과값이 없는 함수
print(' ')

myList = [1,2,3]
print(myList.append(4))
# >>> None이 나온다. append는 return의 과정이 없는 함수인 것.
print(myList)
# >>> mtList에 4가 추가되었음을 확인할 수 있음.

myList = [1,2,3]
print(myList.pop())
# >>> 결과값이 3이 출력됨. pop은 떨어져나간 값이 return으로 출력되는 함수인 것.
print(myList)
# >>> myList에 마지막 인수인 3이 제거됨을 확인할 수 있음.

# 함수에 여러개의 입력값 *args
def sum_many(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(sum_many(1,2,3,4,5))

print('-'*50)

#매개변수 여러가지 입력하기 : *args는 함께 쓰일 수 있다.
# ex) add_mul 함수 계산법 두가지
# >>> choice에 할당한 값에 따라 계산방법 달라짐.
def add_mul(choice, *args):
    if choice == "add":
        result=0
        for i in args:
            result=result+i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
    return result

result=add_mul('add',1,2,3,4,5)
print(result)

result=add_mul('mul',1,2,3,4,5)
print(result)

print(' ')

#키워드 파라미터 **keyword arguments : doctionary 형태로 여러가지 값을 저장
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        if 'ant' in kwargs.keys():
            print("주인님 오셨군요! 오늘 기분이 어떠세요?")
        else:
            print("{0}은 {1}입니다.^^".format(key,value))
print_kwargs(이름='김하은')
print_kwargs(ant='haeun')

#함수의 결과값은 언제나 하나이다. 튜플형태로 출력
def sum_and_mul(a,b):
    return a+b, a*b, a-b
print(sum_and_mul(1,2))
print(sum_and_mul(1,2)[0])

def add_and_mul(a,b):
    return a+b
    return a*b
print(add_and_mul(1,2))
# >>> 첫번째 return문만 실행됨. 즉 함수는 return문은 만나는 순간 함수를 빠져나간다.
def say_nick(nick):
    if nick=="바보":
        return
    print("나의 별명은 %s입니다."%nick)
say_nick('기마웅')
say_nick('바보')

print(' ')

#매개변수에 초기값 미리 설정하기 (man의 기본값은 True)
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('김하은', 25, False)
say_myself('김하은', 25)

print(' ')

#함수 안에서 선언한 변수의 효력범위
a=1
def vartest(a):
    a=a+1
    return print(a)  # >>> return을 해주지 않으면 결과 X
vartest(1)
print(a)

print(' ')

#lamda
def add(a,b):
    return print(a+b)
add(1,2)

add_lambda= lambda a,b : print(a+b)
add_lambda(1,2)

#>>>간단한 함수식 정의는 lambda가 더 편하다.

#>>> 리스트나 튜플 안에서도 함수 정의가 가능하다.
#리스트
myList_lambda=[lambda a,b: print(a+b), lambda a,b : print(a*b)]
myList_lambda[0](2,5)
myList_lambda[1](2,5)
#튜플
myList_lambda=(lambda a,b: print(a+b), lambda a,b : print(a*b))
myList_lambda[0](2,5)
myList_lambda[1](2,5)

print(' ')
print('='*50)


# 04-2 사용자 입력과 출력
#사용자 입력 : input
name=input('이름을 입력하세요.: ')
print(name)

print(' ')

print('life''is''too short')
print('life','is','too short')

for i in range(10):
    print(i, end=' ')


print(' ')
print(' ')


# 04-3 파일 읽고 쓰기
# >>> 주의 : 파일을 한번 open 했으면 꼭 close 해주어야 한다.

#파일 쓰기
f = open('C:/hacoding/myfirst.txt','w', encoding="UTF-8")
for i in range(1,11):
    data='%d번째 줄입니다.\n'%i
    f.write(data)
f.close()

#파일 읽기
#readline : 한 줄씩 읽음
f = open('C:/hacoding/myfirst.txt','r', encoding="UTF-8")
line = f.readline()
print(line)
f.close

print('-'*50)

f=open('C:/hacoding/myfirst.txt','r',encoding="UTF-8")
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

print('-'*50)

f=open('C:/hacoding/myfirst.txt','r',encoding="UTF-8")
while True:
    line=f.readline()
    if not line: break
    print(line.strip("\n"))
f.close()

print('-'*50)

f=open('C:/hacoding/myfirst.txt','r',encoding="UTF-8")
while True:
    line=f.readline()
    if not line: break
    print(line.strip("\n"))
f.close()

print('-'*50)

#readlines : 리스트 형태로 읽음
f=open('C:/hacoding/myfirst.txt','r',encoding="UTF-8")
lines=f.readlines()
for line in lines:
    print(line.strip("\n"),end='')
f.close()

print(' ')
print('-'*50)

#read : 통채로 읽음
f=open('C:/hacoding/myfirst.txt','r',encoding="UTF-8")
data=f.read()
print(data)
f.close()

print('-'*50)

#파일 추가하기
f = open('C:/hacoding/myfirst.txt','a', encoding="UTF-8")
for i in range(11,20):
    data='%d번째 줄입니다.\n'%i
    f.write(data)
f.close()

f=open('C:/hacoding/myfirst.txt','r',encoding="UTF-8")
data=f.read()
print(data)
f.close()