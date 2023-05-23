'''
작성일 : 5월 3일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 사용자로부터 숫자를 입력받아 그 숫자에 1~10사이의 배수를 더한 후 출력하는 프로그램
'''
# while 버전
print("while버전")
#1. 사용자로 부터 정수를 입력받는다 
innum=int(input('검사할 수 입력: '))
#2. total을 0으로 선언
total=0
#3. num을 0으로 선언
num=0
#4. num이 10보다 작을때 까지 반복
while num<10:
    #5. num에 1을 더해준다
    num+=1
    #6-1. 만약 num을 innum으로 나눈 나머지가 0이 아니라면
    if num%innum!=0:
        #6-2. continue 시켜준다
        continue
    #7. total에 num을 더해준다
    total+=num;
#8. 출력해준다.
print("1 부터 10까지 {}의 배수의 합은 {}입니다.".format(innum,total))

print("for버전")
#1. 사용자로 부터 정수를 입력받는다 
innum=int(input('검사할 수 입력: '))
#2. total을 0으로 선언
total=0
#3. num을 0으로 선언
num=0
#4. num이 10보다 작을때 까지 반복
for num in range(1,11):
    #6-1. 만약 num을 innum으로 나눈 나머지가 0이 아니라면
    if num%innum!=0:
        #6-2. continue 시켜준다
        continue
    #7. total에 num을 더해준다
    total+=num;
#8. 출력해준다.
print("1 부터 10까지 {}의 배수의 합은 {}입니다.".format(innum,total))