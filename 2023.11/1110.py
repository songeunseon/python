#약수와 배수 판별
#숫자 a,b를 입력받아 b가 a의 약수인지 확인하기 (a>=b)
#a=8 b=2--> 네
#a=8 b=3--> 아니요

# a=int(input('a'))
# b=int(input('b'))

# if a%b==0:
#     print('약수입니다')
# else:
#     print('약수가 아닙니다')

#숫자 a,b를 입력받아 b가 a의 배수인지 확인하기 (a<=b)
#a=8 b=24--> 네
#a=8 b=25--> 아니요

# a=int(input('a'))
# b=int(input('b'))

# if b%a==0:
#     print('배수입니다')
# else:
#     print('배수가 아닙니다')

#약수 구하기
#숫자 n을 입력받아 n의 모든 약수 구하기

# n=int(input('n:'))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)



#배수 구하기
#숫자n을 입력받아 n의 모든 배수 구하기(단, 100이하)

# n=int(input('n:'))

# for i in range(1,101):
#     if i%n==0:
#         print(i)


#문자 체크
#긴 문장 (text)과 한 문자(t)를 입력 받아
#t가 text안에 포함되어 있는지 확인
text=input('text:')
t=input('t:')

check=False

for i in text:
    if i==t:
        check=True

print(check)

#숫자 체크
#5개의 숫자를 입력받아 리스트를 만들고
#n을 입력받아 리스트 값에 n이 있는지 확인
