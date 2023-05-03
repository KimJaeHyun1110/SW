'''
작성일 : 5월 3일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 사용자로부터 숫자를 입력받아 그 숫자에 해당하는 팩토리얼 출력
'''
# while 버전
print("while버전")
#1. 사용자로 부터 정수를 입력받는다 
num=int(input('팩토리얼 입력: '))
#2. total변수를 1으로 초기화 및 선언 해준다.
total=1
#3. num이 0보다 클때까지 반복 이나 출력을 위해 1로 수정
print("{}! = ".format(num),end='')
while num>1:
    #4. total에 total 곱하기 num의 결과를 저장한다.
    total=total*num
    print(num,"× ",end='')
    #5. num을 1 감소시켜준다.
    num-=1
#6. 친절하게 출력해준다
print("1 = {} 입니다.".format(total))

# for 버전
print("\nfor버전")
#1. 사용자로 부터 정수를 입력받는다 
num=int(input('팩토리얼 입력: '))
#2. total변수를 1으로 초기화 및 선언 해준다.
total=1
#3. num이 0보다 클때까지 반복 이나 출력을 위해 1로 수정
print("{}! = ".format(num),end='')
for num in range(num,1,-1):
    #4. total에 total 곱하기 num의 결과를 저장한다.
    total=total*num
    print(num,"× ",end='')
#6. 친절하게 출력해준다
print("1 = {} 입니다.".format(total))