'''
작성일 : 5월 31일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 레포트5번 8장 1번
'''
#1. 랜덤을 위한 랜덤 불러오기
import random

#2. num.txt를 쓰기모드로 오픈하여 f에 입력
with open("num.txt", 'w') as f:
    #3. i가 0부터 5보다 작을때 까지 반복
    for i in range(5):
        #4. j가 0부터 5보다 작을때 까지 반복
        for j in range(5):
            #5. 1부터 100사이의 랜덤한 숫자를 뒤에 띄어쓰기를 하여 저장
            f.write("{} ".format(random.randint(1, 100)))
        #6. 한줄 끝나면 개행 저장
        f.write('\n')
#7. 필요한 변수와 리스트 선언
i=1
avg=[]
#8. num.txt를 읽기모드로 오픈하여 f에 입력
with open("num.txt","r") as f:
    #9. 무한반복
    while True:
        #10. 한줄씩 읽어서 text에 저장
        text=f.readline()
        #11. 만약 text가 '' 비어있는가
        if text=='':
            #11-1. 참이라면 반복문 종료
            break
        #12. 빈칸을 기준으로 리스트 객체로 반환하여 textList에 저장
        textList=text.split()
        #13. 합계 저장용 및 j값 저장용 변수선언
        sum=0
        j=0
        #14. j가 0부터 textList의 길이만큼 반복한다
        for j in range(0,len(textList)):
            #15. sum에게 textList[j]의 값을 숫자로 바꾼후 sum을 더한 값을 저장한다
            sum=sum+int(textList[j])
        #16. 리스트 avg에게 format을 이용하여 지정된 문자열을 저장한다.
        avg.append("{}번째 학생의 평균 : {}\n".format(i,sum/(j+1)))
        #17. 몇번째 학생인지 알기위해 i를 1더해준다
        i+=1

#18. avg.txt를 쓰기모드로 오픈하여 f에 입력
with open("avg.txt", "w") as f:
    #19. 리스트 avg의 내용을 한줄씩 파일에 저장
    f.writelines(avg)
        
