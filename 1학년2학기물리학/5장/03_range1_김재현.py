'''
작성일 : 9월 27일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 range()함수
'''

for i in range(3):
    print(i, end='. ')
    print("안녕하세요.")
    print(" 김재현 입니다.")

#range(시작값, 숫자 앞까지, 증가값(감소값))
#C언어->for(초기값;조건식;증감식)
for i in range(1,6):
    print(i,end="")
print()

for i in range(10,0,-1):
    print(i,end="")
