'''
작성일 : 6월 07일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 9장 함수와모듈
'''
import random#랜덤함수 불러오기

def make_question():# 질문제작 함수 생성
    num1=random.randint(1, 40)# 1부터 40까지의 정수를 랜덤으로 생성후 num1에 저장
    num2=random.randint(1, 20)# 1부터 20까지의 정수를 랜덤으로 생성후 num2에 저장
    op=random.randint(1, 3)# 1부터 3까지의 정수를 랜덤으로 생성후 op에 저장
    que=str(num1)#생성된 정수 num1을 문자열로 바꿔 que에 저장

    if op==1:#생성된 op가 1이면
        que=que+'+'#문자열 변수 que에 문자 '+'추가
    if op==2:#생성된 op가 2이면
        que=que+'-'#문자열 변수 que에 문자 '-'추가
    if op==3:#생성된 op가 3이면
        que=que+'*'#문자열 변수 que에 문자 '*'추가
    
    que=que+str(num2)#생성된 정수 num2을 문자열로 바꿔 que에 추가
    return que#완성된 사칙연산문자열 que를 반환

R_ans=0#정답수
W_ans=0#오답수

for i in range(5):# i가 0부터 5보다 작을대 까지 반복
    que=make_question()#질문 제작함수를 호출하여 반환값을 que에 저장
    print(que,end='')#que에 저장된 내용을 출력 단, print후 자동개행은 안하도록 end=''로 지정
    result=int(input('='))#'='이라는 문자를 출력후 입력값을 정수로 바꿔 result에 저장
    if eval(que)==result:#문자열 사칙연산 함수에 que를 인수로 준후 반환값이 result랑 같은가? 
        print("정답입니다")#같다면 정답입니다 출력후 개행
        R_ans+=1#R_ans에 자기자신+1을 한후 저장
    else :#아니라면?
        print("오답입니다")#틀렸다면 오답입이다 출력루 개행
        W_ans+=1#R_ans에 자기자신+1을 한후 저장

print("정답 : ",R_ans,"오답 : ",W_ans)# 정답 갯수와 오답 갯수 출력

if R_ans==5:#정답 갯수가 5개인가
    print('당신은 천재 입니다.')
