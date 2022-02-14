#Q1. 홍길동의 평균 점수 구하기
korean=80
english=75
math=55
print((korean+english+math)/3)

#Q2. 홀짝 판별
print(13%2)

#Q3. 주민등록번호 881120-1068234 에서 연월일과 숫자 부분으로 나누어 출력하기
pin="881120-1068234"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)

#Q4. 위의 주민등록번호를 보고 성별 맞추기
print(pin[7])

#Q5. a#b#c#d# 로 출력하기
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#Q6. 리스트 배열 [5,4,3,2,1]로 만들기
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#Q7. Life is too short 문자열 출력
a=['Life','is','too','short']
result=" ".join(a[:])
print(result)

#Q8. 튜플에 4를 추가하기
a=(1,2,3)
a=a+(4,)
print(a)
# >>> (4)가 아닌 (4,)임을 주의하자.

#Q9. 오류가 발생하는 경우
a=dict()
a
# a['name']='python'
# a[('a',)]='python'
# a[[1]]='python'  >>> 오류 : key는 변하는 값이 올 수 없다. (리스트는 변하는 자료)
# a[250]='python'

#Q10. 딕셔너리 a에서 'B'에 해당되는 값을 출력
a={'A':90,'B':80,'C':70}
result=a.get('B')
print(a)
print(result)

#Q11. 중복 제거
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#Q12. b는 어떻게 출력될까
a=b=[1,2,3]
a[1]=4
print(b)

a=[1,2,3]
b=a
a[1]=4
print(b)

# >>> 모두 [1,4,3] 출력.