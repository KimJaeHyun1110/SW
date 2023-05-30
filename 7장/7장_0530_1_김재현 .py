'''
작성일 : 5월 30일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 7장 세트와 딕셔너리
       02. 딕셔너리
키와 값을 한 요소로 묶어 표현한 자료구조
키는 중복을 허용하지 않음
세트처럼 순서가 없는 자료형
각 요소에서 키와 값은 ":"으로 구분
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
#딕셔너리 생성
dict1={1:'one',2:'two',3:'three'}
print("딕셔너리 dict1 내용", dict1)

#리스트를 딕셔너리로 변환
list1=[[1,'하나'],[2,'둘'],[3,'셋'],]
dict2=dict(list1)
print("딕셔너리 dict2 내용", dict2)
print("리스트 list1 내용", list1)

#키를 지정하여 값 검색
print("딕셔너리 dict2의 키 3의 값:",dict2.get(3))

#딕셔너리의 모든 요소 삭제
dict2.clear()
print("딕셔너리 dict2 내용", dict2)

#keys()메소드를 이용하여 사전의 모든 키 출력
print("key : ", dict1.keys())
#반복문 사용하여 키 출력 딕셔너리에 있는 키 값이 끝날때 까지 num에 담는다
for num in dict1.keys():
    print(num,end=', ')
print()

#vlaues()메소드를 이용하여 사전의 모든 값 출력
print("values : ",dict1.values())
#반복문 사용하여 벨류 값 출력 딕셔너리에 있는 벨류 값이 끝날때 까지 num에 담는다
for num in dict1.values():
    print(num,end=', ')
print()

#items()메소드를 이용하여 사전의 모든 키와 값 출력 키와 값 둘다 불러오기에 변수는 2개 선언 필요
for num,alphanum in dict1.items():
    print(num,"은 영어로",alphanum,end=', ')
print()

