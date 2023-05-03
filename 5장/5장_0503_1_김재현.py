'''
작성일 : 5월 3일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 사용자로부터 구구단 단을 입력받아 해당단 출력
'''
#for버전
print("for버전")
#1. 사용자로부터 정수를 입력받아 innum에 저장한다
innum=int(input('단 입력: '))
#2. 곱하는 수를 1부터 9까지 반복하면서
print("::: {}단 :::".format(innum))
for num in range(1,10):
    #3. 구구단을 출력한다.
    print("{}×{}={}".format(innum,num,innum*num))

#while 버전
print("\n\n\nwhile버전")
#1. 곱하는 수인 num을 선언후 1로 초기화 해준다 
num=1
print("::: {}단 :::".format(innum))
#2. 곱하는 수를 1부터 9까지 반복하면서
while num<10:
    #3. 구구단을 출력한다.
    print("{}×{}={}".format(innum,num,innum*num))
    #4. num을 1 증가시켜준다.
    num+=1