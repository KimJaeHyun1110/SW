'''
작성일 : 9월 27일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 
        터틀 그래픽으로 여러개의 원을 그려보자
'''
import turtle as t

#원 하나 그리기
#t.circle(100)

for count in range(10):
    t.circle(100)
    t.left(360/10)

#t.mainloop()#터틀 종료1
t.done()#터틀 종료2