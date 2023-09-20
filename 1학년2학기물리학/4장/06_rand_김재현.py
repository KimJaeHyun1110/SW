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

#3. 사용자에게 물자열로 가위 바위 보 중 하나를 입력받는다.
sel=input("가위, 바위, 보 중 하나를 입력해 주세요 : ")

#4. 0~2사이의 랜덤한 수를 randselect에 입력합니다
rsel=random.randrange(3)
print("컴퓨터 : ",end='')
if rsel==0:
    print("가위")
if rsel==1:
    print("바위")
if rsel==2:
    print("보")
#4. 이기는 조건에 해당하면 이겼습니다를 출력합니다 예시로 sel이 가위이고 rsel이 2(보)이면 이깁니다
if (sel=="가위" and rsel==2)or(sel=="바위" and rsel==0)or(sel=="보" and rsel==1) :
    print("이겼습니다")
#6. 비기는 조건에 해당하면 비겼습니다를 출력합니다 예시로 sel이 가위이고 rsel이 0(가위)이면 이깁니다.
elif (sel=="가위" and rsel==0)or(sel=="바위" and rsel==1)or(sel=="보" and rsel==2) :
    print("비겼습니다")
#7. 아니라면 졌습니다를 출력합니다.
else :
    print("졌습니다")