'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''

with open("student.txt", "w") as f:
    for i in range(5):
        std=input("학생 정보를 입력해주세요: ")
        print(std,file=f)
