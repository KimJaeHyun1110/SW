'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#ptext.txt파일을 copytext.txt파일로 복사
source=input("원본 파일 입력 : ")
target=input("복사본 파일 입력 : ")

with open(source,"r") as f:
    texts=f.read()#파일의 모든 내용을 읽어 변수에 저장

with open(target,"w") as f:
    f.write(texts)#texts의 내용을 target파일에 쓰기(출력)

print("{} 파일이 생성 되었습니다.".format(target))