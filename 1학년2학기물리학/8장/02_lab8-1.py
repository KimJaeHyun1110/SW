'''
작성일 : 11월 1일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 딕셔너리
        lab 8-1 편의점 재고 관리 프로그램
'''
items={"커피음료":7,"펜":3,"종이컵":2,"우유":1,"콜라":4,"책":5}

#물건의 목록을 출력한다
print("제품 목록 : ",end='')
for key in items.keys():
    print(f"{key}, ",end='')
print()

#물건의 이름을 입력 받아 재고를 출력한다
print()
name=input("물건의 이름을 입력하시오:")
print('재고:',items[name])
