#한줄에 하나씩 숫자 입력받기
# a=int(input("a 입력:"))
# b=int(input("b 입력:"))
# c=int(input("c 입력:"))

# print(a,b,c,a+b+c)



#한줄에 여러개의 숫자 입력받기
# a,b,c=map(int,input('a b c 값 입력').split())

# print(a,b,c,a+b+c)

#문자1.split(문자2):문자2를 기준으로 문자1을 자른다.
# text=input('날짜 입력 yyyy.mm.dd')
# y,m,d=text.split('.')

# print(text,y,m,d)


#map(함수,집합 형태-iterable객체):
# a,b,c=map(int,['1','2','3'])

# print(a,b,c,a+b+c)

#하나씩적용
#a,b,c=map(int,input('a b c값 입력').split())
# text=input('a b c값 입력')
# text=text.split()
# a,b,c=map(int,text)

# print(a,b,c,a+b+c)


#숫자출력하기
# x=3
# y=5
# print(x,y,x+y)

#숫자와 문자 함께 출력하기 (1)콤마 & 형변환
# print(x,'과', y,'의 합은', x+y,'이다')
# print(str(x)+'과'+ str(y)+'의 합은'+str(x+y)+'이다')

#숫자와 문자 함께 출력하기 (2) end=''
# print(x,end='')
# print('과 ',end='')
# print(y,end='')
# print('의 합은 ',end='')
# print(x+y,end='')
# print('이다')

#숫자와 문자 함께 출력하기 (3) format()
# print('{}과 {}의 합은 {}이다'.format(x,y,x+y))

#연산자 우선순위
#산술연산자>관계연산자>논리연산자
#산술연산자- 지수>곱하기,나누기,몫,나머지>더하기,빼기
#관계연산자- 작다>작거나같다>크다>크거나같다>같다>같지않다
#논리연산자- not > and > or 
#ex) 2*5>2+5 and not 3*3>10 -> true

#반올림 : round(a), round(a,b)
# print(round(3.33))
# print(round(3.66))
# print(round(3.66,1)) #소수첫번째자리까지 반올림해라
# #절대값 : abs(a)
# print(abs(3))
# print(abs(-3))
# #제곱 : pow(a,b) a=밑 b=지수
# print(pow(3,2))
# print(3**2)
# #나눗셈 : divmod(a,b)
# x,y=divmod(7,2) #x=몫 y=나머지
# print(x)
# print(y)
# #최대값 : max(a,b,c,d,...)
# print(max(7,5,1,3))
# #최소값 : min(a,b,c,d,...)
# print(min(7,5,1,3))
# #합 : sum(집합 형태: Iterable)
# print(sum([7,5,1,3]))

# #문자열 다루기
# #1.문자열인덱스
# text='abc'
# print(text[0])
# print(text[1])
# print(text[2])
# print()
# print(text[-3])
# print(text[-2])
# print(text[-1])

#2.문자열 슬라이스
# text='abcde fgh ijk'
# text[2:5]
# print(text[2:5])
# print(text[1:8])
# print(text[-5:-1])


# print(text[5:]) #인덱스 5번부터 맨끝까지
# print(text[:5]) #처음부터 인덱스 5번전까지
# print(text[:]) #처음부터 끝까지
# print(text[0:8:2]) #맨끝에는 간격
# print(text[1:8:2]) #맨끝에는 간격
# print(text[8:0:-1]) #음수를 적을경우 거꾸로 
# print(text[::-1])
# print(text[::3])

#문자열 메쏘드
#1.출력지정:format(a,b,c,...)
# text='abcde{}{}'
# print(text.format('ABC',123))

#2.대체하기 : replace(a,b) a=바꾸고싶은대상 b=바꾸고싶은값
# text='abcde ABC ABC'
# print(text.replace('A','K'))

#3.자르기 : split(a)
# text='abcde A/B/C A.B.C'
# a,b,c=text.split('/')
# print(a)
# print(b)
# print(c)

#4. 합치기 : a.join() 리스트다룰때 많이 사용
# text='abcde'
# print('/'.join(text))

#5. 개수 확인하기 : count(a)
# text='abcde ABC ABC'
# print(text.count('a'))
# print(text.count('A'))
# print(text.count('1'))

#6. 제거하기 : strip(a) / lstrip(a) / rstrip(a)
# text=' abcde '
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

#7.인덱스 찾기 : find(a) / rfind(a)/ index(a)/ rindex(a)
# text='ABC ABC'
# print(text.find('A'))
# print(text.rfind('A'))
# print(text.index('A'))
# print(text.rindex('A'))

#8.확인하기 : isalpha()/isdigit()/isalnum()/isupper()/islower()
#결과값은 true 또는 false로 나온다
# text1= 'ABCabc123'
# text2= '123'
# text3= 'ABC'
# text4= 'abc'

# print(text1.isalpha())
# print(text1.isdigit())
# print(text1.isalnum())
# print(text1.isupper())
# print(text1.islower())

# print(text2.isalpha())
# print(text2.isdigit())
# print(text2.isalnum())
# print(text2.isupper())
# print(text2.islower())

# print(text3.isalpha())
# print(text3.isdigit())
# print(text3.isalnum())
# print(text3.isupper())
# print(text3.islower())

# print(text4.isalpha())
# print(text4.isdigit())
# print(text4.isalnum())
# print(text4.isupper())
# print(text4.islower())

#9.대/소문자 만들기 :upper() /lower()
# text='ABCabc'
# print(text.upper())
# print(text.lower())

#10. 0채우기 : zfill()
# y='2023'
# m='11'
# d='2'
# print(y.zfill(4))
# print(m.zfill(2))
# print(d.zfill(2))


#if문
'''
특정조건을 만족할때와 만족하지 않을때를 나누어 코드를 실행하는 조건문
조건이 참일때=실행
조건이 거짓일때=실행하지않음
if 조건: (한칸띄어쓰기)
    실행코드 (한 블록 들여쓰기)
'''
#if
# num=int(input('숫자하나 입력:'))

# if num>0 :
#     print('{}은(는) 양수입니다'.format(num))

#if~else
# num=int(input('숫자하나 입력:'))

# if num%2==0 :
#     print('{}은(는) 짝수입니다'.format(num))
# else :
#     print('{}은(는) 홀수입니다'.format(num))

#if ~elif
# age=int(input('나이입력'))

# if age<=7:
#     print('유아입니다')
# elif age<=19:
#     print('청소년입니다')
# elif age>=20:
#     print('성인입니다')
    

#if ~elif ~else
# text=input('알파벳 입력:')

# if text.isupper():
#     print('대문자')
# elif text.islower():
#     print('소문자')
# else :
#     print('대/소문자 구분 불가능')

#while문
'''
특정 조건을 만족할때 코드를 반복 실행하는 조건문
조건이 참일때 = 반복실행
조건이 거짓일때 = 반복 종료
while 조건:(한칸띄어쓰기)
    실행코드 (한블록들여쓰기)
'''
#while문
# print('a가 0보다 같거나 크면 실행, 작으면 정지')

# a=int(input('a:'))
# while a>=0:
#     print('실행')
#     a=int(input('a:'))

#무한루프
# a=10

# while a>0:
#     print('실행')
#     a=a-1

#n번 반복하기
# n=int(input('n:'))

# while n:
#     print(n)
#     n=n-1


#~까지 반복하기
#(1)1~10까지 숫자 반복하기
# n=1
# while n<=10:
#     print(n)
#     n=n+1

#(2)yes를 입력하면 반복하기
# text='yes'

# while text=='yes':
#     text=input('yes 입력시 반복')
# print('종료')

# #(3)e 또는 E가 입력될때 까지 반복하기
# text=input('e또는 E입력시 종료')

# while text!='e' and text!='E':
#     text=input('e또는 E입력시 종료')
# print('종료')

#for문
'''
특정 범위만큼 코드를 반복 실행하는 조건문
열거형 데이터를 하나씩 변수 값에 대입하며 실행
for 변수 in 열거형: (한칸띄어쓰기 사이사이)
    실행코드 (한블록 들여쓰기)
'''
#range()함수
'''
숫자의 범위와 증감 값을 정하면 규칙적인 수들의 집합으로 만들어주는 함수
range(a) -> 0~a-1
range(a,b) -> a~b-1
range(a,b,c) -> a~b-1,c씩 증가
@a,b,c는 모두 정수(int)만 가능

range(11)
-0부터 10(11-1)까지 1씩 증가
-> 0,1,2,3,4,5,6,7,8,9,10

range(1,11)
-1부터 10(11-1)까지 1씩 증가
-> 1,2,3,4,5,6,7,8,9,10

range(1,11,2)
-1부터 10(11-1)까지 2씩 증가
-> 1,3,5,7,9
'''

#range()연습

for i in range(1,11,3):
    print(i)


    fjdkfj;sldkjf