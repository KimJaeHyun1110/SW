'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
print("==학생 정보 읽어오기1==")
with open("student.txt","r") as f:
    while True:
        std=f.readline()
        print(std, end='')
        if std=='':
            break

print("==학생 정보 읽어오기2==")
with open("student.txt","r") as f:
    while True:
        std=f.readline()
        studentList=std.split()#빈칸을 기준으로 리스트 객체로 반환
        print(studentList)
        if std=='':
            break

