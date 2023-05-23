'''
작성일 : 5월 23일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 6장 시퀸스 자료형
       05. 다중리스트
'''
#다중리스트
num=[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]

#리스트 내의 각각 리스트의 합계를 계산하여 출력
for i in range(len(num)):
    total=0
    for j in range(len(num[i])):#0번지의 길이까지 반복
        total+=num[i][j]
    print(total)

#실습예제 6-5
# 1~100사이의 랜덤 수를 발생시ㅕ 리스트에 저장하고
# 합계, 최대값, 최소값을 출력하시오
# 오름차순으로 정렬도 하시오.
import random
num=[]
for i in range(10):
    num.append(random.randint(1, 100))

print("생성된리스트 : ",num)
print("가장 큰값 : ",max(num))
print("가장 작은값 : ",min(num))
print("합계 : ",sum(num))
num.sort()#정렬후 출력하기
print("오름차순 정렬 : ",num)