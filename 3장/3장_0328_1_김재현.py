'''
작성일 : 3월 28일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 변수 사용법과 자료형 알아보기
       print() 함수 사용법 익히기.
'''
# 변수 num1에 10을 배정하시오.
num1=10
# 변수 num2에 20을 배정하시오.
num2=20 #첫칸띄어쓰기 하지말것
# 변수 pi에 3.14를 배정하시오.
pi=3.14
#변수에 자기 이름을 저장하시오.
name="김재현"
#num1,num2에 저장된 값을 더하여 total에 저장하시오.
total=num1+num2
#각변수에저장된값을출력한다.
print(num1,num2,pi,name,total,num1==10,name=="김재현")
print("pi:{}, num1:{}, num2:{}, total:{}, name:{} num1==num2?:{}".format(pi,num1,num2,total,name,num1==num2))
#나의 이름은 김재현입니다.
print("나의 이름은 {}입니다.".format(name))
print("나의 이름은 ",name,"입니다.",sep='')
#10+20+30
print("{}+{}={}".format(num1,num2,total))
print(num1,'+',num2,'=',total,sep='')
#변수의 자료형 알아보기 위해서 사용하는 함수
#type()
print("num1의 자료형 :",type(num1))
print("pi의 자료형 :",type(pi))
print("name의 자료형 :",type(name))
