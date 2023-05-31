'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#writelines()메소드
list1=['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n']
list2=[1,2,3,4,5]

#readline() 메소드 - 무한 반복문으로 읽기
print("==for문을 이용하여 읽기==")
with open("Linetest.txt","r") as f :
    for line in f:#f의 내용이 없을때 까지 반복하면서 line 변수에 입력해주세요
        print(line,end='')