#문자 입력받아 공백 기준 자르기
# li1=input('문자 입력').split()


#문자 입력받아 전체 자르기
# li2=list(input('문자입력'))

#숫자하나씩 입력받기
# li3=[]

# li3.append(int(input('숫자입력')))
# li3.append(int(input('숫자입력')))
# li3.append(int(input('숫자입력')))

#숫자 여러개 입력받기
# li4=list(map(int,input('숫자입력').split()))
# a=input('숫자입력').split()
# b=map(int,a)
# c=list(b)

#합, 평균, 최소값, 최대값, 중간값 구하기
# num=list(map(int,input('숫자입력').split()))
# num.sort() #오름차순으로 값을 정렬

# print('합:',sum(num))
# print('평균:',sum(num)/len(num))
# print('최소값:',num[0])
# print('최대값:',num[len(num)-1])
# print('중간값:',num[len(num)//2])

#리스트와 제어문

#for문으로 리스트값 추가
# li=[]

# for i in range(5):
#     li.append(int(input('숫자입력:')))

#for문으로 리스트 값 출력
# for i in range(len(li)):
#     print(li[i])
    
# for i in li:
#     print(i)
    
#if문 추가
# for i in range(len(li)):
#     if i%2==0:
#         print(li[i]) #짝수 인덱스 출력
        
# for i in li:
#     if i%2==0:
#         print(i) #짝수값 출력
        
        
#리스트 분리하기
# li=list(input('문자입력:'))
# up=[]
# low=[]

# for i in li:
#     if i.isupper():
#         up.append(i)
#     elif i.islower():
#         low.append(i)
        
# print(up)
# print(low)

#함수
'''
함수란?
프로그램을 짤 때 효율을 높이기 위하여
특정기능르 미리 만들어 두고 이름을 붙여 사용
'''

#함수정의하기 인자값/리턴값
# def aa():
#     print('hi~')
    
# def bb(x):
#     for i in range(x):
#         print('hello~')
    
# def cc():
#     n=int(input('n:'))
#     print(n*2)
#     return n*2

# def dd(x,y):
#     print(x*y)
#     return x*y

#함수 호출하기
# re1=aa()
# re2=bb(3)
# re3=cc()
# re4=dd(4,5)


#내장 모듈 활용
# import math
# re1=math.ceil(2.1)      #올림
# re2=math.floor(2.1)     #내림
# re3=math.factorial(10)  #팩토리얼
# re4=math.sqrt(4)        #루트
# math.pi             #원주율

# print(re1,re2,re3,re4,math.pi)

import random
re1=random.randint(1,5)     #범위 내의 정수 랜덤값 생성
re2=random.random()         #0<=?? <1 랜던값 생성

li=['a','b','c','d','e']
re3=random.choice(li)       #리스트 값 중 하나 랜덤뽑기
re4=random.sample(li,3)     #리스트에서 랜덤 n 개 뽑기
re5=random.shuffle(li)      #리스트 순서 랜덤 섞기

print(li)