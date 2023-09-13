'''
작성일 : 9월 13일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 터틀 모듈
'''

import turtle as t  #터틀 모듈을 사용하기 위해 준비
                    #turtle 클래스 객체를 t로 생성. (별명)

t.shape("turtle")#커서모양 거북이로
t.speed(4)#선그리는속도

#선 그리기
#t.forward(200)#200픽셀 이동

#삼각형 그리기
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
#원그리기
for i in range(144):
    t.forward(5)
    t.left(2.5)
for i in range(72):
    t.forward(10)
    t.left(5)
for i in range(36):
    t.forward(20)
    t.left(10)
for i in range(18):
    t.forward(40)
    t.left(20)
for i in range(9):
    t.forward(80)
    t.left(40)
#별그리기
for i in range(5):
    t.forward(200)
    t.left(144)



t.mainloop()#그림판 사라지지 않게 위해 사용