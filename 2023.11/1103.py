#for문
# for i in range(10):
#     print(i)

#1서 n까지 출력
# n=int(input('n:'))
# for i in range(1,n+1):
#     print(i)

#a서 b까지 출력
# a,b=map(int,input('a,b:').split())
# for i in range(a,b+1):
#     print(i)

#n서 0까지 출력
# n=int(input('n:'))
# for i in range(n,-1,-1):
#     print(i)

#기타제어문
'''
continue
-해당 단계만 건너뛰고 다음 단계로 간다
break
-제어문을 중단하고 빠져나간다
pass
-아무작업도 하지않는다
-비워두면 오류나니 패스를 넣어 오류방지
//
제어문과 함께 다양하게 활용되는 명령문
'''

#continue
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
#break
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
#pass
# for i in range(1,11):
#     if i==5: 
#         pass
#     print(i)

#제어문 중첩

#if +if
# age=int(input('나이입력:'))
# if age<=7:
#     print('유아입니다')
# elif age<=19:
#     print('청소년입니다')
#     if age<=13:
#         print('초등학생')
#     elif age<=16:
#         print('중학생')
#     else:
#         print('고등학생')
# else:
#     print('성인입니다')

#for +if
# n=int(input('n:'))
# for i in range(1,n+1):
#     if i%3==0:
#         print('X')
#     else:
#         print(i)

#while +if
# num1=0
# num2=int(input('n:'))
# while True:
#     num1=num1+1
#     print(num1)
#     if num1==num2:
#         break

#for +for
# for i in range(1,7):
#     for j in range(1,7):
#         print(i,j)



#list
#리스트만들기
# li=[]
# li=list()

# #리스트 인덱스
# li=['a','b','c']

# li[0]
# li[1]
# li[2]

# li[2]='d'

# #리스트 활용
# li=['a','b','c','d','e']
# li.index('c')       #위치찾기

# li.append('f')      #추가하기1
# li.insert(0,'aa')      #추가하기2

# li.remove('aa')     #삭제하기1
# del li[2]           #삭제하기2

# 'b' in li           #확인하기

# len(li)             #전체개수

# li.count('a')       #개수세기

# num=[1,2,3,4,5,6,7,8,9,10]

# sum(num)            #합구하기
# min(num)            #최소값
# max(num)            #최대값

# num.reverse()       #역순만들기

# num.sort()              #오름차순정렬
# num.sort(reverse=True)  #내림차순정렬


#tuple

#튜플만들기
# tu=()
# tu=tuple()

# #튜플인덱스
# tu=('a','b','c')
# tu[0]
# tu[1]
# tu[2]

# tu[2]='d'

# #튜플 활용
# tu=('a','b','c','a')

# tu.index('c')       #위치찾기
# 'b' in tu           #확인하기
# len(tu)             #전체개수
# tu.count('a')       #개수세기

# num=(5,7,9)
# n1,n2,n3=num            #변수할당하기
# #값과 변수의 개수가 같아야 함


# a='hello'
# b='world'
# (a,b)=(b,a)             #값교환하기
# print(a,b) 


# li=['a','b','c','d','e','f']
# tuple(li)               #리스트->튜플
# print(tuple(li)) 

# tu=('a','b','c')
# list(tu)                #튜플->리스트
# print(list(tu))

# tu=('a','b','c')
# print(tu)
# print(tu[0])

#set 세트

#세트만들기
# se=set()
# se={} #사용불가능

#세트특징(순서,중복 없음)
# a={2,4,6,8}
# b={2,4,2,1,2,3}

# a[0]

#세트활용
# a.add(5)            #추가하기
# a.remove(5)         #삭제하기
# 1 in a              #확인하기
# len(a)              #전체개수
# sum(num)            #합구하기
# min(num)            #최소값찾기
# max(num)            #최대값찾기

# list(a)             #리스트만들기
# tuple(a)            #튜플만들기

# a={1,2,3}
# b={2,3,4}

# a&b                 #교집합
# a|b                 #합집합
# a-b                 #차집합
# a^b                 #대칭 차집합

# print(a^b)


#사전 dict
'''
딕셔너리 특징
사전형(딕셔너리)
dic={키:값,키:값,키:값}
-딕셔너리의 기본형태
-리스트,튜플,세트와 달리 키(key)와 값으로 이루어짐
'''

#딕셔너리 만들기
dic={}
dic=dict()

#딕셔너리 특징
dic={'kor':80,'eng':90,'mat':77}
dic['kor']
dic['kor']=85
dic['sci']=92
dic[0]
#키가 있으면 변경, 없으면 추가가 된다


#딕셔너리 활용
del dic['mat']          #삭제하기
dic.clear()             #전체삭제
'eng' in dic            #확인하기(키 기준)
len(dic)                #전체 개수

dic.keys()              #모든 키 얻기
dic.values()            #모든 값 얻기
dic.items()             #모든 순서쌍 얻기

tuple(dic)
list(dic)
set(dic)


#짝이 맞아야 가능합니당
li=['ab','cd','ef']
dict(li)

li=[['a',1],['b',2],['c',3]]
dict(li)

