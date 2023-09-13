'''
작성일 : 9월 13일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 직각 삼각형의 빗변의 길이를 구하시오.
'''

bottom=float(input('직각삼각형의 밑변의 길이를 입력하시오: '))
height=float(input('직각삼각형의 높이를 입력하시오: '))
hypotenuse=(bottom**2+height**2)**0.5
print("빗면은 {:.2f}입니다.".format(hypotenuse))