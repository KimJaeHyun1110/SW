'''
작성일 : 9월 27일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 
        반복문으로 펙도리얼 구하기
        오늘의 마지막 문제
'''
num=1
i=int(input('정수를 입력하시오: '))
for j in range(1,i+1):
    num*=j
print("{}!은 {} 이다.".format(i,num))
