'''
작성일 : 5월 16일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 사용자로 부터 월을 입력받아 그 월이 봄여름가을겨울중 어디에 해당하는지 출력
'''
# 첫번째 방법
#1. 필요변수 선언
num=1
#2-1. num이 0이 아닐때 까지 반복
while True:
    print("\n\n\n\n====================\n가장 좋아하는 월은? (종료 : 0)\n====================")
    #2-2. num에 정수를 입력한다
    num=int(input('입력해 주세요 : '))
    #2-3-1. num이 0보다 작거나 12보다 큰가
    if 0>num or 12<num:
        #2-3-2. 참이라면 다시 입력 요구후 컨티뉴
        print("잘못된 숫자를 입력하셨습니다 다시 입력해 주세요")
        continue
    #2-3-3-1. 거짓이면 만약 num이 0인가?
    elif num==0:
        #2-3-3-2. 참이라면 브레이크
        break
    print("****** {}월 ******\n{}월은 ".format(num,num),end='')
    #2-4-1. num이 3~5인가
    if 3<=num<=5:
        #2-4-2. 참이라면 봄 출럭
        print("봄에 해당합니다.")
    #2-4-3-1. 거짓이라면 만약 num이 6~8인가
    elif 6<=num<=8:
        #2-4-3-2. 참이라면 여름출력
        print("여름에 해당합니다")
    #2-4-3-3-1. 거짓이라면 만약 num이 9~11인가
    elif 9<=num<=11:
        #2-4-3-3-2. 참이라면 가을출력
        print("가을에 해당합니다")
    #2-4-3-3-3. 거짓이라면 겨울 출력
    else:
        print("겨울에 해당합니다")
print("종료 하였습니다 이용해주셔서 감사합니다.")

#두번재 방법
#1. 필요변수 선언
num=1
#2-1. num이 0이 아닐때 까지 반복
while num!=0:
    print("\n\n\n\n====================\n가장 좋아하는 월은? (종료 : 0)\n====================")
    #2-2. num에 정수를 입력한다
    num=int(input('입력해 주세요 : '))
    #2-3-1. num이 0보다 작거나 12보다 큰가
    if 0<num<13:
        print("****** {}월 ******\n{}월은 ".format(num,num),end='')
        #2-4-1. num이 3~5인가
        if 3<=num<=5:
            #2-4-2. 참이라면 봄 출럭
            print("봄에 해당합니다.")
        #2-4-3-1. 거짓이라면 만약 num이 6~8인가
        elif 6<=num<=8:
            #2-4-3-2. 참이라면 여름출력
            print("여름에 해당합니다")
        #2-4-3-3-1. 거짓이라면 만약 num이 9~11인가
        elif 9<=num<=11:
            #2-4-3-3-2. 참이라면 가을출력
            print("가을에 해당합니다")
        #2-4-3-3-3. 거짓이라면 겨울 출력
        else:
            print("겨울에 해당합니다")
    else:
        print("잘못된 숫자를 입력하셨습니다 다시 입력해 주세요")
print("종료 하였습니다 이용해주셔서 감사합니다.")