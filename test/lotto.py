import random

lotto_num=[] #빈 로또 번호 리스트 생성

def getRandomNumber():
    number=random.randint(1,45)
    return number
count=0 #횟수를 지정한 변수
#무한반복
while True:
    if count > 5:
        break
    random_number=getRandomNumber() #로또번호하나를 뽑는다
    if random_number not in lotto_num: #로또번호 리스트안에 뽑은 로또번호가 없으면
        lotto_num.append(random_number) #로또 번호 리스트에 뽑은 로또번호를 추가해라
        count=count+1

print(lotto_num)
# for i in range(6):