'''
작성일 : 5월 30일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 7장 세트와 딕셔너리
       02. 딕셔너리

'''
#1. 딕셔너리 생성
dict1={}
i=0
'''
while True :
    num=int(input("{}번째 학생 이름 학번 입력 : ".format(i+1)))
    if num==0:
        break
    name=input("{}번째 학생 이름 이름 입력 : ".format(i+1))
    dict1
    i+=1'''
#2. 5회반복
for i in range(5) :
    #2-1. 학생정보 입력
    num=int(input("{}번째 학생 이름 학번 입력 : ".format(i+1)))
    name=input("{}번째 학생 이름 이름 입력 : ".format(i+1))
    #2-2. 입력받은 정보는 dict1에 저장 딕셔너리 값 추가
    dict1[num]=name#num이 키 name이 값
#3. 완성 알림 및 명부 출력
print("학생 명부가 완성 되었습니다.",dict1)
#4. 무한반복
while True:
    #4-1. 검색을 원하는 학번을 입력받음
    num=int(input("검색을 원하는 학생의 학번 입력 : "))
    #4-2. 입력받은숫자가 0인가
    if num==0:
        #4-2-1. 참이라면 반복문 종료
        break;
    else:
        #4-2-2. 거짓이라면 만약 검색값의 출력이 비어있는가?
        #if dict1.get(num,'')=='':
        #if dict1.get(num)==None:
        if num in dict1:#dict1안에 num의 값이 있는가?
            #4-2-2-1. 참이라면 학생 정보 출력
            print("입력한 학번에 해당하는 학생의 이름 : ",dict1.get(num))
            print("학번 : ",num,"이름 : ",dict1.get(num))
            print("학번 : ",num,"이름 : ",dict1[num])
        else:
            #4-2-2-2. 거짓이라면 잘못된 학언 입력 알림
            print("잘못된 학번을 입력하셨습니다.")
