'''
작성일 : 5월 30일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#open()함수로 파일 쓰기 - write()메소드
f=open("C:\\Users\\User\\Documents\\test.txt","w")#파일 오픈

#파일에 쓸 내용
for i in range(1, 11):
    f.write("{}번째 메세지 입니다. \n".format(i))

f.close()#파일 종료