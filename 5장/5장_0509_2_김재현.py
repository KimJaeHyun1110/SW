'''
작성일 : 5월 9일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 사용자로부터 5과목 점수를 입력받아 총점과 평균을 출력하는 프로그램
'''
# while 버전
print("while버전")
#1. total,count를 0으로 초기화 및 선언
total=0
count=0
#2. count가 5보다 작을때 까지 반복
while count<5:
    #3. 사용자로 부터 정수를 입력받는다 
    print(count+1,"번째 정수 입력 : ",end='')
    num=int(input(''))
    #4-1. 만약 num이 0~100 사이의 숫자가 아니라면
    if not 0<=num<=100:
        #4-2. 맞다면 continue시켜준다
        print("잘못된 숫자를 입력 하셨습니다.")
        continue
    #5. total에 num을 더해준다
    total+=num;
    #5. count에 1을 더해준다
    count+=1;
#6-1. 총점과 평균을 출력
print("총점 {}점 \n평균 {:.2f}점".format(total,total/5))
