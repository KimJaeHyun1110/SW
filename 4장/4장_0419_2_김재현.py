'''
작성일 : 4월 19일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 숫자 두개와 연산자를 입력받아 연산자에 해당하는 사칙연산을 수행하고 출력하는 프로그램
'''
# 1. 정수를 입력 받아서 num1에 저장한다.
num1=int(input("숫자1을 입력해 주세요 : "))

# 2. 연산자를 입력 받아서 cal에 저장한다.
cal=input("연산자를 입력해 주세요 : ")

# 3. 정수를 입력 받아서 num2에 저장한다.
num2=int(input("숫자2를 입력해 주세요 : "))

# 4. 만약 cal이 '+' 이라면 num1+num2의 결과를 출력한다
if cal=='+':
    print("{} + {} = {}입니다.".format(num1,num2,(num1+num2)))

# 5. 아니고만약 cal이 '-' 이라면 num1-num2의 결과를 출력한다
elif cal=='-' :
        print("{} - {} = {}입니다.".format(num1,num2,(num1-num2)))

# 6. 아니고만약 cal이 '*' 이라면 num1*num2의 결과를 출력한다
elif cal=='*' :
        print("{} * {} = {}입니다.".format(num1,num2,(num1*num2)))

# 7. 아니고만약 cal이 '/' 이라면 num1/num2의 결과를 출력한다
elif cal=='/' :
        print("{} / {} = {}입니다.".format(num1,num2,(num1/num2)))

# 8. 아니면 "해당 연산자가 없습니다." 라고 출력한다.
else:
    print("해당 연산자가 없습니다.")


