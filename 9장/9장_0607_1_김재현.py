'''
작성일 : 6월 07일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 9장 함수와모듈
'''

#두 정수를 입력 받아 큰 수를 출력하시오.
#큰 수를 판별하여 결과를 돌려주는 함수를 작성하시오.

#알고리즘
#*함수
#3. 전달 받은 두 수를
#1) 둘 중 큰 수를 판단한다.
#만약에 첫번째수가 두번째수보다 크면
#a. 첫번째 수를 돌려준다.
#2) 아니면 (두번째수가 첫번째수보다 크다)
#a. 두번째 수를 돌려준다.

#*메인
#1. 두 정수 입력 받기
#2. 두 정수를 가지고 함수 호출하기
#4. 돌려 받은 결과 출력하기

def max_num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

num1=int(input("첫번째 숫자 입력 : "))
num2=int(input("두번째 숫자 입력 : "))
print("두 숫자 중 큰 수 : ",max_num(num1, num2))
