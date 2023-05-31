'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#3과목의 평균 점수를 계산하여 출력
print("==학생 정보 읽어오기2==")
with open("student.txt","r") as f:
    while True:
        std=f.readline()
        if std=='':
            break

        studentList=std.split()#빈칸을 기준으로 리스트 객체로 반환
        name=studentList[0]#첫번째 항목을 name에 저장
        sum=0#합계 저장용 변수선언
        for i in range(1,4):
            sum=sum+int(studentList[i])#1,2,3번지의 문자를 숫자로 변환하여 합계계산

        print("{}학생의 점수는 국:{}, 영:{}, 수{}, 총합{}, 평균{:.0f} 입니다".format(name,studentList[1],studentList[2],studentList[3],sum,sum/3))
        

