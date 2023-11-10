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
# text=input('text:')
# t=input('t:')

# check=False

# for i in text:
#     if i==t:
#         check=True

# print(check)

#숫자 체크
#5개의 숫자를 입력받아 리스트를 만들고
#n을 입력받아 리스트 값에 n이 있는지 확인

# li=list(map(int,input('li:').split()))
# n=int(input('n:'))

# check=False

# for i in li:
#     if i==n:
#         check=True

# print(check)

#약수의 개수 구하기
#n을 입력받아 n의 약수의 개수 구하기
# n=int(input('n:'))
# check=0
# for i in range(1,n+1):
#     if n%i==0:
#         check=check+1
        
# print(check)

# n=int(input('n:'))
# li=[]
# for i in range(1,n+1):
#     if n%i==0:
#         li.append(i)
        
# print(len(li),li,sum(li))

#OX개수 구하기
#text를입력받아 O의 개수,X의 개수 구하기
# text=list(input('text'))
# #알고리즘으로
# o_count=0
# x_count=0
# for i in text:
#     if i=='o':
#         o_count=o_count+1
#     elif i=='x':
#         x_count=x_count+1
# print(o_count)
# print(x_count)

#평균 이상 개수 구하기
#여러개의 숫자를 입력 받아 평균을 구하고
#평균이상의 숫자 개수 구하기
# num=list(map(int,input('num:').split()))

# avg=sum(num)/len(num)
# check=0
# for i in num:
#     if i>=avg:
#         check=check+1

# print(avg)
# print(check)

#소수 판별하기
#숫자 하나 입력 받아 소수인지 아닌지 확인하기
# n=int(input('n:'))
# check=0
# for i in range(1,n+1):
#     if n%i==0:
#         check=check+1
# if check==2:
#     print(True)
# else:
#     print(False)
    
#1,n
# n=int(input('n:'))
# check=True
# for i in range(2,n):
#     if n%i==0:
#         check=False
# print(check)

#범위 내의 소수 구하기
#a값을 입력받아 1~a사이 모든 소수값 구하기(a>0)

# a=int(input('a:'))
# li=[]
# #중첩for문 사용
# for n in range(2,a+1):
#     check=True
#     for i in range(2,n):
#         if n%i==0:
#             check=False
#     if check:
#         li.append(n)
        
# print(li)

#등차수열
#앞 항에 일정한 수를 더해 만드는 수열
#3,8,13,18,23,28,...n번째 항 구하기

# n=int(input('n:'))
# a=3 #시작값
# for i in range(n-1):
#     a=a+5 # +하는 값
    
# print(a)


#등비수열
#앞 항에 일정한 수를 곱해 만드는 수열
#3,6,12,24,48,96,...n번째 항 구하기

# n=int(input('n:'))
# a=3 #시작값
# for i in range(n-1):
#     a=a*2 # *하는 값
    
# print(a)

# n=int(input('n:'))
# a=int(input('a:'))
# r=int(input('r:'))

# for i in range(n-1):
#     a=a*r # *하는 값
    
# print(a)


#피보나치 수열
#바로 앞의 두개의 항을 더해 만드는 수
#1,1,2,3,5,8,13,...n번째 항 구하기

# n=int(input('n:'))
# a=1
# b=1
# for i in range(n-2):
#     c=a+b #2
#     a=b #1
#     b=c #2
# print(b)

#별찍기
#계단
# ***
#  ***
#   ***
# n=int(input('n:'))
# for i in range(n):
#     print(' '*i,end='')
#     print('*'*n)
    
#삼각형
# n=int(input('n:'))
# for i in range(1,n+1):
    # print('*'*i)
    
# n=int(input('n:'))
# for i in range(1,n+1):
    # print(' '*(n-i),end='')
    # print('*'*i)
    
#역삼각형
# n=int(input('n:'))
# for i in range(n):
#     print('*'*(n-i))
    
# n=int(input('n:'))
# for i in range(n):
#     print(' '*i,end='')
#     print('*'*(n-i))
    
#피라미드
# n=int(input('n:'))
# for i in range(n):
#     print(' '*(n-i-1),end='')
#     print('*'*(i*2+1))

#중첩 for문
#주사위
# a=int(input('a:'))
# b=int(input('b:'))
# n=int(input('n:'))


# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if i+j==n:
#             print(i,j)


#구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print('{}*{}={}'.format(i,j,i*j))
#     print()


#행렬만들기
# li=[[1,2,3,4],[5,6,7,8]]

# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j],end=' ')
#     print()


#띄어쓰기 없애기
# text=input('text')

# for i in text:
#     if i !=' ':
#         print(i,end='')
        
#대소문자 바꾸어 출력하기
# text=input('text')

# for i in text:
#     if i.isupper():
#         print(i.lower(),end='')
#     elif i.islower():
#         print(i.upper(),end='')
#     else:
#         print(i,end='')
        
        
#이름찾기
# name=['김철수','김영희','홍김동','이소뇽','이오랑']
# for i in name:
#     if '김' in i:
#         print(i)
        
# for i in name:
#     if i[0]=='이':
#         print(i)

#최대/최소값
#최소값
# li=list(map(int,input('숫자입력:').split()))
# m=li[0]
# for i in li:
#     if i <m:
#         m=i
# print(m)

#최대값
# li=list(map(int,input('숫자입력:').split()))

# x=li[0]
# for i in li:
#     if i>x:
#         x=i
        
# print(x)

#탐색하기
#선형탐색
# li=[1,6,4,2,3,10,8,7,5,9]
# n=int(input('1~10'))

# for i in range(len(li)):
#     if li[i]==n:
#         print(i)
#         break






#이진탐색(정렬이 되어있어야함)
# li=[1,3,5,6,8,9,13,15,17,19]
# n=int(input('1,3,5,6,8,9,13,15,17,19:'))

# s_index=0
# e_index= len(li)-1

# while s_index<=e_index:
#     m_index=(s_index+e_index)//2 #중간 인덱스 구하기
#     if n<li[m_index]:
#         e_index=m_index-1
#     elif n>li[m_index]:
#         s_index=m_index+1
#     else:
#         print(m_index)
#         break


#정렬하기
#선택정렬
# li=[8,6,4,1,2,3,5,10,9,7]
# for i in range(len(li)):
#     print(li)
#     m_index=i
#     for j in range(i,len(li)):
#         if li[j] < li[m_index]:
#             m_index=j
#     li[i],li[m_index]=li[m_index],li[i]
# print(li)

#버블정렬
li=[8,6,4,1,2,3,5,10,9,7]
for i in range(len(li)):
    print(li)
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1], li[j]
print(li)
