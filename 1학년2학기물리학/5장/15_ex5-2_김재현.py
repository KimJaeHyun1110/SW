'''
작성일 : 10월 4일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 
        두수를 입력받아
        1. 두수 사이의 합계 출력하기
        2. 두수 사이의 짝수의 합계 출력하기

        심화문제 5.2, 141쪽
        for 또는 while 중 원하는 것 사용.
        오늘의 마지막 문제
'''

#1. 합계를 저장할 변수 두개를 만든다
n1=0
n2=0

#2. 사용자로 부터 숫자 두개를 입력받아 저장한다
start=int(input('시작 정수를 입력하세요: '))
stop=int(input('끝 정수를 입력하세요: '))
#2-1. 만약 start가 stop보다 크면 서로 바꿔준다
if start>stop:
    temp=stop
    stop=start
    start=temp

#3. 정수의 합 앞 부붙을 출력해준다
print("{}부터 {}까지의 정수의 ".format(start,stop),end='')
#4. start부터 stop까지 반복한다
for start in range(stop+1):
    #4-1. n1에 start를 더한다
    n1+=start
    #4-2. 만약 start를 2로 나눈 나머지가 0이라면 n2에 start를 더한다
    if start%2==0:
        n2+=start
#5. 모든 합을 출력한다.
print(f"모든 합은 {n1} 이고 짝수의 합은 {n2} 입니다")