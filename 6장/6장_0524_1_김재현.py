'''
작성일 : 5월 24일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 6장 시퀸스 자료형
'''
#튜플생성
tuple1=() #빈 튜플
tuple2=('a',) #원소가 하나여도 쉼표는 필수!!
tuple3=('a','b','c') #2개이상은 마지막 쉼표 필요X

color=('white','gray','black','red','green','blue','skyblue')
print("color 내용 : ",color)
print("color의 길이 : ", len(color))
print("white 개수 : ",color.count('white'))
print("green의 위치 : ",color.index('green'))

#실습예제6-7
#2개의 튜플을 하나의 리스트로 만들기
fruit=('사과','배','딸기','수박','망고')
price=(2000,4500,8000,12000,5500)

#결과 : [사과, 2000, 배, 4500 ....]
fp_list=[] #2개의 튜플 내용이 저장 될 리스트 생성
fp_tuple=()
for i in range(len(fruit)):
    fp_list.append(fruit[i])
    fp_list.append(price[i])

print("과일 목록 : ",fruit)
print("가격 목록 : ",price)
print("과일의 가격 리스트 : ",fp_list)
