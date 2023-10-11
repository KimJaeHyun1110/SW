'''
작성일 : 10월 11일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 6장 함수
        여러개의 값을 넘겨주고 여러개의 값을 돌려받기
        두 수를 전달 받아 사칙연산의 결과값을 돌려주는 함수
        [알고리즘]
        (함수)
        3. 두 수를 전달받는다
        4. 절달 받은 수로 사칙연산을 진행한다
        5. 사칙연산의 결과 5개를 그냥 리턴한다
        (메인)
        1. 사용자로 부터 두 수를 입력받는다
        2. 입력받은 두 수를 함수에 전달한다
        6. 받은 결과값을 출력한다
'''

def cals(n1,n2):
    sum=n1+n2
    minus=n1-n2
    mul=n1*n2
    div=n1/n2
    rest=n1%n2
    return sum,minus,mul,div,rest

n1=int(input('첫번째 정수를 입력 해 주세요 : '))
n2=int(input('두번째 정수를 입력 해 주세요 : '))
sum,minus,mul,div,rest=cals(n1,n2)
print(f"{n1}+{n2}={sum}")
print(f"{n1}-{n2}={minus}")
print(f"{n1}*{n2}={mul}")
print(f"{n1}/{n2}={div}")
print(f"{n1}%{n2}={rest}")