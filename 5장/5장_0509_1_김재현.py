'''
작성일 : 5월 9일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 사용자로부터 숫자를 입력받아 그 숫자가 소수인지 아닌지 판단하는 프로그램
'''
# while 버전
print("while버전")
#1. 사용자로 부터 정수를 입력받는다 
num=int(input('검사할 수 입력: '))
#2. count을 2로 선언
count=2
#3. count가 num보다 작을때 까지 반복
while count<num:
    #4-1. 만약 num을 count으로 나눈 나머지가 0이라면
    if num%count==0:
        #4-2. break 시켜준다
        break
    #5. count에 1을 더해준다
    count+=1;
#6-1. 만약 num이랑 count가 같은가
if num==count:
    #6-2. 같다면 소수 입니다 출력
    print("정수 {}은(는) 소수 입니다.".format(num))
else:
    #6-3. 아니라면 소수가 아닙니다 출력
    print("정수 {}은(는) 소수가 아닙니다.".format(num))

# for 버전
print("for버전")
#1. 사용자로 부터 정수를 입력받는다 
num=int(input('검사할 수 입력: '))
#2. count을 2로 선언
count=2
#3. count가 num보다 작을때 까지 반복
for count in range(2,num+1):
    #4-1. 만약 num을 count으로 나눈 나머지가 0이라면
    if num%count==0:
        #4-2. break 시켜준다
        break
#5-1. 만약 num이랑 count가 같은가
if num==count:
    #5-2. 같다면 소수 입니다 출력
    print("정수 {}은(는) 소수 입니다.".format(num))
else:
    #5-3. 아니라면 소수가 아닙니다 출력
    print("정수 {}은(는) 소수가 아닙니다.".format(num))