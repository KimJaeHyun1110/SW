'''
작성일 : 9월 20일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 과제 1 - 113페이지 4.3
        나이를 입력받아 나이가 20살 이상이면 Adult 10살 이상 20살 미만히면 Youth
        10살 미만이면 Kid를 출력하는 프로그램을 ifelse문으로 사용하여 작성하시오
'''
#1. 나이를 정수로 입력 받는다
age=int(input('나이를 입력하시오 : '))

#2. 만약 나이가 20세 이상이면 Adult출력
if age>=20 :
    print("Adult")
#3. 아니고 만약 나이가 20세 미만 10세 이상이면 Youth출력
elif 20>age>=10:
    print("Youth")
#4. 아니라면 10세 미만이라는 뜻 이기에 Kid출력
else:
    print("Kid")