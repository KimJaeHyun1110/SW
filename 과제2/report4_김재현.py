'''
작성일 : 5월 31일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 레포트4번 7장 3번
'''
#1. 프로그램을 짜기위한 랜덤 불러로기 및 사용할 리스트와 딕셔너리 선언
import random
rlist=[]
list1=[]
list2=[]
list3=[]
dict1={}

#2. i는 0부터 9까지 반복한다
for i in range(10):
    #3. rlist에 1부터 100사이의 랜덤한 결과를 추가한다
    rlist.append(random.randint(1, 100))
#4. 추가된 리스트를 출력한다
print("생성된 리스트 :",rlist)

#5. rlist한테 더이상 불러올 값이 없을때 까지 값을 하나씩 불러와서 i에게 넣어주는것을 반복
for i in rlist:
    #6. i가 0보다 크고 10보다 작은가
    if 0<i<10:
        #7. 참이라면 list1에 i값을 추가한다
        list1.append(i)
#8. 딕셔너리에 1을 키값으로 list1를 저장한다
dict1[1]=list1

#9. rlist한테 더이상 불러올 값이 없을때 까지 값을 하나씩 불러와서 i에게 넣어주는것을 반복
for i in rlist:
    #10. i가 0보다 크고 10보다 작은가
    if 9<i<100:
        #11. 참이라면 list2에 i값을 추가한다
        list2.append(i)
#12. 딕셔너리에 1을 키값으로 list2를 저장한다
dict1[2]=list2

#13. rlist한테 더이상 불러올 값이 없을때 까지 값을 하나씩 불러와서 i에게 넣어주는것을 반복
for i in rlist:
    #14. i가 0보다 크고 10보다 작은가
    if 99<i<1000:
        #15. 참이라면 list3에 i값을 추가한다
        list3.append(i)
#16. 딕셔너리에 1을 키값으로 list3를 저장한다
dict1[3]=list3

#17. 딕셔너리를 출력한다
print("생성된 딕셔너리 :",dict1)