#Q1. 다음 코드의 결과값은?
a="Life is too short =, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

#>>>돌리기 전 예상 : shirt 출력

#Q2. 1부터 1000까지의 자연수 중 3의 배수의 합 구하기
result=0
i=1
while i<=1000:
    if i%3==0:
        result += i
    i += 1
print(result)

print(' ')

result=0
i=0
while i<=1000:
    i=i+1
    if i%3==0:
        result += i
print(result)

#>>> i+=1 은 i=i+1과 같다.

print(' ')

#Q3. 그림과 같이 코드 구현
i=0
while True:
    i += 1
    if i>5: break
    print('*'*i)

print(' ')

#Q4. 1부터 100까지 숫자 출력
for i in range(1,101):
    print(i)

print(' ')

#Q5. A학급의 평균점수 구하기
classA=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in classA:
    total=total+score
average=total/len(classA)
print(average)

classA=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in classA:
    total+=score
average=total/len(classA)
print(average)

print(' ')

#Q6. 홍수에만 2를 곱하는 코드 구현 
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    if n%2==1:
        result.append(n*2)
print(result)

# 위 코드를 리스트 내포를 사용하여 구현
numbers=[1,2,3,4,5]
resultt= [n*2 for n in numbers if n%2==1]
print(resultt)






