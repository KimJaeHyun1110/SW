'''
작성일 : 10월 11일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 6장 함수
        
'''
def order(num,pickel,onion):
    print("햄버거{}개 - 피클{}, 양파{} ".format(num,pickel,onion))

def order2(num,pickel='기본',onion='기본'):
    print("햄버거{}개 - 피클{}, 양파{} ".format(num,pickel,onion))

order2(2)
order2(1,pickel='뺌',onion='기본')