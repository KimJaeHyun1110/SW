'''
작성일 : 5월 2일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 두 수를 입력받아 두 수 사이의 합을 구하는 프로그램
'''
#1. 숫자입력받기
input_num1=int(input('첫번쨰 정수를 입력해 주세요: '))
input_num2=int(input('두번째 정수를 입력해 주세요: '))

# 변수값교환
if input_num1>input_num2:
    num=input_num1
    input_num1=input_num2
    input_num2=num

#2. sum=0
sum=0

#3. 수는 입력받은 수 부터
num=input_num1

#4. 수는 입력받은 수 까지 반복하면서
while num<=input_num2:
    # 1) 합계 계산
    sum+=num
    # 2) 수는 1씩 증가
    num=num+1

#5. 합계 출력
print("{}부터 {}까지의 숫자를 모두 더하면 {}입니다.".format(input_num1,input_num2,sum))