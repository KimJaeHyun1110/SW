'''
작성일 : 9월 20일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 4장 조건문
        random을 이용한 가위바위보 게임.
'''
#1. random 함수를 불러온다
import random

#2. 게임이 시작되었음을 알린다.
print("가위바위보 게임 시작")

p1=input('Player1의 이름 : ')
p2=input('Player2의 이름 : ')

n1=random.randrange(3)#p1의 랜덤수
n2=random.randrange(3)#p2의 랜덤수

#p1의 가위바위보 출력
print(p1, " : ",end='')
if n1==0:
    print("가위")
if n1==1:
    print("바위")
if n1==2:
    print("보")

#p2의 가위바위보 출력
print(p2, " : ",end='')
if n2==0:
    print("가위")
if n2==1:
    print("바위")
if n2==2:
    print("보")

#4. n1 이기는 조건에 해당하면 p1이(가) 이겼습니다를 출력합니다 예시로 n1이 0(가위)이고 n2이 2(보)이면 이깁니다
if (n1==0 and n2==2)or(n1==1 and n2==0)or(n1==2 and n2==1) :
    print(p1,"이(가) 이겼습니다")
#6. 비기는 조건에 해당하면 비겼습니다를 출력합니다 예시로 nl이 0(가위)이고 n2이 0(가위)이면 이깁니다.
elif (n1==0 and n2==0)or(n1==1 and n2==1)or(n1==2 and n2==2) :
    print("비겼습니다")
#7. 아니라면 p2이(가) 이겼습니다를 출력합니다.
else :
    print(p2,"이(가) 이겼습니다")