'''
작성일 : 9월 20일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 4장 조건문
        교통 카드의 종류로 '청소년', '성인' 카드가 있다고 하자.
        사용자에게 카드의 종류를 입력받아 청소년이면 '청소년입니다.'
        '성인'이면 '성인입니다.'를 출력하자.
'''

#1. 카드의 종류를 문자열로 입력받는다
card=input('카드의 종류를 입력해주세요(성인, 청소년) : ')

#2. 입력받은 문자열이 성인인가?
if card=="성인":
    #2-1. 성인이라고 출력
    print("성인입니다.")
#3. 아니면 입력받은 문자열이 청소년인가
elif card=="청소년":
    #3-1. 청소년이라고 출력
    print("청소년입니다.")
#4. 아니면 잘못된 입력이라 출력
else:
    print("잘못된 입력입니다.")
