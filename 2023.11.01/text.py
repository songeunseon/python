print('hi')
a=5
b=10
print(a+b)
#불필요한코드

'''
여러줄의
주석을
처리하는
방법
'''
print('불필요한 코드') 

n=10
if n%2==0:
    print('even')
    print('짝수')
else:
    print('odd')
    print('홀수')

#변수
a=10
b=5
print(a) #변수를 호출
print('a') #a라는 문자 호출
print(b)
b=7 #b값의 변경 var같은 느낌일세
print(a+b)

'''영어, _ 만이 첫글자에 올수있다
a와 A는 다르다
파이썬의 단어들은 변수이름으로 사용할수없다'''

#내장함수사용법
'''함수이름(인자값,인자값,인자값) -->리턴값
// 리턴값이 있다면 추가적으로 활용가능 '''
print('hi','hello')

#표준입출력
name=input('이름을 입력해주세요')
print('안녕하세요',name)