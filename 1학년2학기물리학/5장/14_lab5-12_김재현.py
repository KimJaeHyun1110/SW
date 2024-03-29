'''
작성일 : 10월 4일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 
        2개의 수로 더하기 결과를 맞추는 게임
        2개의 수는 1~100사이 랜덤으로 출제됨
        사용자가 0을 입력하면 프로그램은 종료
        즉, 사용자가 0을 입력하기 전 까지는 무한 반복하여 문제 풀기
        정답을 맞추면 "참 잘했어요!" 출력
        틀리면 정답을 알려주고, "정답은 00 입니다. 틀렸습니다" 출력
        게임이 종료되면 "프로그램 종료!" 출력
        문제분석: 랜덤수 생성 import random
'''
#1. 랜덤 함수를 사용하기 위해 불러와준다
import random as r
#2. 무한반복
while True:
    #2-1. 1부터 100사이의 숫자를 각각 따로 저장해준다
    n1=r.randint(1,100)
    n2=r.randint(1,100)
    #2-2. 사용자로 부터 질문을 출력하고 정수를 입력받아 i에 저장한다
    i=int(input(f'{n1}+{n2}= '))
    #2-3-1. 만약 i가 0인가?
    if i==0:
        #2-3-1-1. 0이라면 반복문을 빠저 나간다
        break
    #2-3-2. 아니고 만약 n1+n2와 i의 값이 같은가?
    elif n1+n2==i:
        #2-3-2-1. 참 잘했어요 출력
        print("참 잘했어요!")
    #2-3-3. 아니면 정답을 출력하고 오답이라 알려준다.
    else:
        print("정답은",n1+n2,"입니다. 틀렸습니다")
#3. 프로그램이 종료되었다 알려준다
print("프로그램 종료!")