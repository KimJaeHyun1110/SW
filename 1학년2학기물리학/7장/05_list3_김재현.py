'''
작성일 : 10월 18일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 7장 리스트
    리스트의 객체 생성과 참조
'''
fr1=['딸기','수박','바나나']

#실제 값을 복사하는 것이 아니라 리스트의 저장 위치가 복사된다
fr2=fr1

print("fr1 :",fr1)
print("fr2 :",fr2)

fr2[1]='망고'#fr2의[1]번지 과일을 망고로 바꾸면

print("fr1 :",fr1)#모두 1번지 내용이 망고로 바뀐다
print("fr2 :",fr2)#주소를 참조하기 때문(같은 주소)

#주소확인 => 메모리 위치 정보 알아보기 id()함수
print("fr1의 id :",id(fr1))
print("fr2의 id :",id(fr2))# 두 리스트의 id정보가 같다.

'''
리스트 내용 복제하기 list() 함수
'''
fr2=list(fr1)
print("내용 복제 후 1")
print("fr1 :",fr1)
print("fr2 :",fr2)

print("fr1의 id :",id(fr1))
print("fr2의 id :",id(fr2))# 두 리스트의 id정보가 다르다.

#내용 복제2
fr3=fr1[:]
print("내용 복제 후 2")
print("fr1 :",fr1)
print("fr3 :",fr3)

print("fr1의 id :",id(fr1))
print("fr3의 id :",id(fr3))# 두 리스트의 id정보가 다르다.

fr3[0]='수박'#0번지 내용을 수박으로 바꾼다.
print("fr3의 0번지에 수박으로 내용을 바꾼후")
print("fr1 :",fr1)
print("fr3 :",fr3)