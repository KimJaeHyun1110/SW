'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#print() 함수로 파일에 저장. 매개변수 file의 값으로 파일 객체에 저장.
#1번방법
f=open("ptext.txt","w")
#print 문이 원래 출력할 내용을 file=f로 지정하여 저장시킴
print("컴퓨터공학부",file=f)
print("202395010",file=f)
print("김재현",file=f)
f.close()
#2번방법
'''
with open("ptext.txt","w") as f:
    print("컴퓨터공학부",file=f)
    print("202395010",file=f)
    print("김재현",file=f)
'''