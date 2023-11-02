# print('hi')
# a=5
# b=10
# print(a+b)
#불필요한코드

'''
여러줄의
주석을
처리하는
방법
'''
# print('불필요한 코드') 

# n=10
# if n%2==0:
#     print('even')
#     print('짝수')
# else:
#     print('odd')
#     print('홀수')

#변수
# a=10
# b=5
# print(a) #변수를 호출
# print('a') #a라는 문자 호출
# print(b)
# b=7 #b값의 변경 var같은 느낌일세
# print(a+b)

'''영어, _ 만이 첫글자에 올수있다
a와 A는 다르다
파이썬의 단어들은 변수이름으로 사용할수없다'''

#내장함수사용법
'''함수이름(인자값,인자값,인자값) -->리턴값
// 리턴값이 있다면 추가적으로 활용가능 '''
print('hi','hello')

#표준입출력
# name=input('이름을 입력해주세요')
# print('안녕하세요',name)
'''
자료형은 파이썬에서 데이터를 다룰때 데이터의 종류를 의미
변수를 만들때 사용자가 자료형을 결졍하지 않아도 파이썬 내부에서 자동으로 자료형을 판단하여 적용
자료형확인은 type()함수로 알수있다.
필요에 따라 자료형을 변경할수있다
각 자료형의 특징을 잘 이해하면 효율적인 코드를 짤 수있다.
'''
#숫자형
'''
종류
1. 정수형 int 
2. 실수형 float 
3. 복소수 complex 등등
- 연산이 가능하다
-숫자를 다루는 내장함수들 사용가능 ex)round(), range(), pow() 등

a+b > a 더하기 b
a-b > a 빼기 b
a*b > a 곱하기 b
a/b > a 나누기 b
---자주쓰는것 ▼----
a//b > a를 b로 나눈 몫
a%b > a를 b로 나눈 나머지
a**b > a의 b 제곱
'''
# a=10
# b=5 #int로 판단(정수)
# c=2.0 #float로 판단(실수)
# d=0.5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #형태가 float로 나온다
# print(a//b) 
# print(a%b)
# print(a**b)


#숫자중 하나라도 실수가 포함이되면 형태가 float로 출력된다
# print(b+c)
# print(b-c)
# print(b*c)
# print(b/c) 
# print(b//c) 
# print(b%c)
# print(b**c)

# print(d+c)
# print(d-c)
# print(d*c)
# print(d/c) 
# print(d//c) 
# print(d%c)
# print(d**c)

#논리형
'''
종류
1. bool
    ->true(참)/false(거짓) 
-참과 거짓을 나타내는 자료형
-주로 비교&논리 연산자로 만들어진다
-조건문에 많이 활용된다

비교연산자
< 작다
<= 작거나같다
> 크다
>= 크거나같다
== 같다
!= 같지않다

논리연산자
x or y - x나 y 둘 중 하나만 참이면 참이다
x and y - x,y 모두 참이어야 참
not x - x가 참이면 거짓
        x가 거짓이면 참
''' 
# x=10
# y=-10

# print(x>0)
# print(y>0)
# print()
# print(x>y)
# print(x<y)
# print()
# print(x==10)
# print(x==y)
# print(x!=y)
# print()
# print(x>0 or y>0)
# print(x>0 and y>0)
# print()
# print(x>0)
# print(not x>0)

#문자열형
'''
종류
1. str -> 다른 언어와 달리 문자와 문자열을 따로 구분하지않는다
-'' 또는 "" 에 감싸져 있다.
-연산이 불가능하다. (예외:문자+문자, 문자*정수)
-문자열을 다루는 다양한 메소드들이 존재한다.
ex) split(), join(), upper(), lower(), replace() 등
'''
# a=5
# b='5'
# c=5.0

# print(a+a) #int+int
# print()
# print(b+b)
# print(a*b) #int*str 문자가 곱하기된 숫자만큼 나열된다
# print()
# '''
# print(a+b) #int+str 
# print(b*c) #str*float 
# '''
# print('안녕하세요')
# print("안녕하세요")
#print("안녕하세요')

#군집자료형
'''
-여러 데이터를 모든 집합 형태 자료형
종류
1. 리스트 list -데이터를 순차적으로 저장 ->열거형
2. 튜플 tuple -값을 변경할수 없는 열거형 집합
3. 세트 set -순서가 없고 중복이 허용되지않는 집합
4. 사전 dictionary -키와 값의 쌍으로 구성된 집합
'''

#자료형 변환
'''
-파이썬은 사용자가 자료형을 결정하지않기 때문에 편리하기도 하지만
데이터가 사용자의 의도와 다른 자료형이 될 수도있다
이때는 각 데이터들의 자료형을 원하는 것으로 변경해야한다.
ex) input()사용, 정수와 실수의 사용등
-자료형 변환(typecasting)방법: 원하는 자료형 함수에 값을 넣는다.
ex)str(10), int('10'), int(12.5), list('hello') 등
'''
#input()으로 숫자 입력받기
# a=int(input('숫자를 입력하세요'))
# print(a+a)

'''
#실수<->정수
num=5.0
range(int(num))
'''
a=input('숫자 하나 입력')
b=int(a)
c=float(a)

print(type(a))
print(type(b))
print(type(c))