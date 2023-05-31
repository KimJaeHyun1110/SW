'''
작성일 : 5월 31일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 레포트6번 8장 2번
'''
#1. 필요한 리스트 선언
report=[]
total=[0,0,0]

#2. score.txt를 읽기모드로 오픈하여 f에 입력
with open("score.txt","r") as f:
    #3. 무한반복
    while True:
        #4. 한줄씩 읽어서 text에 저장
        std=f.readline()
        #5. 만약 text가 '' 비어있는가
        if std=='':
            #5-1. 참이라면 반복문 종료
            break
        
        #6. 빈칸을 기준으로 리스트 객체로 반환하여 textList에 저장
        studentList=std.split()
        #7. 첫번째 항목을 name에 저장
        name=studentList[0]
        #8. 합계 저장용 변수선언
        sum=0
        #9. i가 1부터 4까지 반복한다
        for i in range(1,4):
            #10. sum에게 studentList[i]의 값을 정수로 바꾼값에 sum을 더한후 저장한다
            sum=sum+int(studentList[i])
            #11. total[i-1]에게 studentList[i]의 값을 정수로 바꾼값에 total[i-1]을 더한후 저장한다
            total[i-1]=total[i-1]+int(studentList[i])
        #12. 리스트 report에게 format을 이용하여 지정된 문자열을 저장한다
        report.append("{} 총점:{} 평균 {}\n".format(name,sum,sum/3))

#13. 리스트 report에게 format을 이용하여 지정된 문자열을 저장한다
report.append("국어전체평균: {}\n".format(total[0]/4))
report.append("수학전체평균: {}\n".format(total[1]/4))
report.append("영어전체평균: {}\n".format(total[2]/4))

#14. report.txt를 쓰기모드로 오픈하여 f에 입력
with open("report.txt", "w") as f:
    #15. 리스트 report의 내용을 한줄씩 파일에 저장
    f.writelines(report)