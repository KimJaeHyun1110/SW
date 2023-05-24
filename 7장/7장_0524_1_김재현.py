'''
작성일 : 5월 24일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 7장 세트와 딕셔너리
       01. 세트
       
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
set1={'one','two','three'}
print("세트 set1 내용 : ",set1)

set2={1,2,3,4,5,4,3,2,1}
print("세트 set2 내용 : ",set2)

set3={1,2,3,(1,2,3),4}
print("세트 set3 내용 : ",set3)

set4={1,2,3,(1,2,3),4,(2,2,2)}
print("세트 set4 내용 : ",set4)

#set5={1,2,3,[1,2,3],4}
#print("세트 set5 내용 : ",set5)#리스트는 세트에 포함 할 수 없다.
#따라서 문자열, 튜플을 세트 자료형으로 사용 가능하지만 리스트는 안된다.

#세트 메소드
#add(),remove(),discard(),pop(),copy(),clear()

#추가
set6={1,2,3,4,5,6}
set6.add(6)
print("세트 set6 내용 : ",set6)

#set6에 1~10까지 내용을 추가하시오.
for i in range(1,11):
    set6.add(i)

print("세트 set6 내용 : ",set6)

#삭제 remove(),discard(),pop()
set6.discard(1)#내용중 1을 삭제
set6.remove(3)#내용중 3을 삭제
print("세트 set6 내용(1,3 삭제) : ",set6)

set6.discard(11)
#set6.discard(11) #내용중 없는 11을 삭제시 오류 발생
print("세트 set6 내용(11 삭제) : ",set6)

set6.pop() #첫번째 요소 삭제
print("세트 set6 내용 : ",set6)

#복사
set7={11,22,33,44,55}
set8=set7.copy()
print("세트 set7 내용 : ",set7)
print("세트 set8 내용 : ",set8)

#지우기(모두삭제)
set7.clear()
print("세트 set7 내용 : ",set7)

#세트 연산 메소드
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("세트 set1 내용 : ",set1)
print("세트 set2 내용 : ",set2)
print("set1과 set2의 합집합",set1|set2)
print("set1과 set2의 교집합",set1&set2)
print("set1과 set2의 차집합",set1-set2)