'''
작성일 : 5월 30일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#writelines()메소드
list1=['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n']
list2=[1,2,3,4,5]

#with open()함수로 파일 읽기
with open("Linetest.txt","w") as f:#파일 오픈(쓰기)
    f.writelines(list1) #줄 단위 텍스트 파일 쓰기
    #f.writelines(list2) #오류 발생. 리스트 내용이 정수일 경우 오류 발생.

#with문을 사용하여 파일 객체를 생성하는 경우 f.close()를 쓸필요없다.