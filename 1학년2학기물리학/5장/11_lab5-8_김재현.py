'''
작성일 : 10월 4일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 
        while문으로 별 그리기를 해보자
'''
import turtle as t

t.shape("turtle")
i=0
while i<5:
    t.forward(50)
    t.right(144)
    i+=1


#t.mainloop()#터틀 종료1
t.done()#터틀 종료2