'''
작성일 : 5월 30일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#open()함수로 파일 읽기 - read()메소드
f=open("test.txt","r")#파일 오픈(읽기)

text=f.read()
print(text)

f.close()#파일 종료