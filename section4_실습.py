#Q1. 홀수/짝수 구별 함수
def is_odd(number):
    if number%2==0:
        return True
    else:
        return False

print(is_odd(1))
print(is_odd(2))

print(' ')

#Q2. 평균 계산 함수
def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return print(result/len(args))

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)

print(' ')

#Q3. 두 개 숫자를 입력받아 더하여 돌려주는 함수

#input1 = input("첫번째 숫자를 입력하세요.:")
#input2 = input("두번째 숫자를 입력하세요.:")

#total=int(input1)+int(input2)
#print("두 수의 합은 %d입니다."%total)
#>>>문자형을 숫자형을 바꿔줘야한다.

print(' ')

#Q4. 결과가 다른 하나는?
#>>> 3번으로 예상됨. 문자열에서 띄어쓰기는 콤마로 한다.
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

print(' ')

#Q5. 기존 코드에서 오류 찾아 고치기
#f1 = open("C:/hacoding/homework4.txt","w")
#f1.write("Life is too short.")
#f1.close()
#f2 = open("C:/hacoding/homework4.txt","r")
#print(f2.read())
#f2.close()

print(' ')

#Q6. 파일을 불러와 기존 내용을 유지한 채로 새로운 내용 입력하기
#user_input = input("저장할 내용을 입력하세요.:")
#f=open("C:/hacoding/homework4.txt","a")
#f.write("\n")
#f.write(user_input)
#f.close()

#f=open("C:/hacoding/homework4.txt","r")
#print(f.read())
#f.close()

print(' ')

#Q7. 문자열 수정 : java를 python으로 수정하기
f=open("C:/hacoding/homework4.txt","r")
body=f.read()
f.close()
print(body)

body=body.replace("java","python")

f=open("C:/hacoding/homework4.txt","w")
f.write(body)
f.close()

f=open("C:/hacoding/homework4.txt","r")
body=f.read()
f.close()
print(body)