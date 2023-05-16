'''
작성일 : 5월 16일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 10개의 정수를 입력받아 합을 구하는 프로그램 단, 짝수번째에 입력되는 숫자는 양수를 음수로, 음수를 양수로 바꾸어야한다.
'''
#for버전
print("for버전")
#1. 필요 변수를 선언한다
count=0
total=0
#2-1. count가 10보다 작을때까지 반복한다
for count in range(10):
    #2-2. 정수를 입력 받는다.
    num=int(input(str(count+1)+"번째 정수를 입력하세요."))
    #2-3-1. 만약 count+1을 2로 나눈 나머지가 0인가?
    if (count+1)%2==0:
        #2-3-2. num에 -1 을 곱해준다
        num*=-1
    #2-4. total에 num을 더해준다
    total+=num
#3. 친절하게 출력한다.
print("변수의 총 합은",total,"입니다.")

#while 버전
print("\n\n\nwhile버전")
#1. 필요 변수를 선언한다
count=0
total=0
#2-1. count가 10보다 작을때까지 반복한다
while count<10:
    #2-2. 정수를 입력 받는다.
    num=int(input(str(count+1)+"번째 정수를 입력하세요."))
    #2-3-1. 만약 count+1을 2로 나눈 나머지가 0인가?
    if (count+1)%2==0:
        #2-3-2. num에 -1 을 곱해준다
        num*=-1
    #2-4. total에 num을 더해준다
    total+=num
    #2-5. count를 1증가시켜준다
    count+=1
#3. 친절하게 출력한다.
print("변수의 총 합은",total,"입니다.")


#교수님코드
count=1
sum=0
while True:
    num=int(input(str(count)+"번째 정수를 입력하세요."))
    if count%2==0:
        num = -num
    sum+=num
    count+=1

    if count>10:
        break
print("10개 정수의 합 : {}".format(sum))