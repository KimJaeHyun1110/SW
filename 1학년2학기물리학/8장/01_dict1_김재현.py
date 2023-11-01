'''
작성일 : 11월 1일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 딕셔너리
'''
#빈딕셔너리생성
phone_book1={}

#딕셔너리에 값 저장 1 key, value [key]=value
phone_book1['김재현']='010-1234-5678'
print('phone_book1 :',phone_book1)#{'김재현':'010-1234-5678'}

#딕셔너리에 값 저장 2 {key:value}
phone_book2={'홍길동':'010-7899-4545','김재현':'010-1234-5678'}
print('phone_book2 :',phone_book2)#

#딕셔너리에 값 저장 3
phone_book3={}
phone_book3['김재현']='010-1234-5678'
phone_book3['이재현']='010-2234-5678'
phone_book3['박재현']='010-3234-5678'
phone_book3['최재현']='010-4234-5678'
phone_book3['정재현']='010-5234-5678'
print('phone_book3 :',phone_book3)#


print()
print("::전화번호 phone_book3::")
#모든 key 출력
print(phone_book3.keys())
#모든 value 출력
print(phone_book3.values())
#모든 key,value 출력
print(phone_book3.items())

print()
print("::전화번호 phone_book3 items()출력::")
for name,phone_num in phone_book3.items():
    print(name,':',phone_num)

print()
for key in phone_book3.keys():
    print(key,':',phone_book3[key])

print()

print("딕셔너리 작성 시 : (콜론)을 기준으로 key:value 작성")
person_dict={'name':'김재현','age':23,'calss':'1학년'}

print('name :',person_dict['name'])
print('age :',person_dict['age'])

print()
#phone_book3를 sorted로 정렬
print(sorted(phone_book3))

print("키를 기준으로 정렬")
sort_phone_book3=sorted(phone_book3.items(),key=lambda x:x[0])
print(sort_phone_book3)
print("값을 기준으로 정렬")
sort_phone_book3=sorted(phone_book3.items(),key=lambda x:x[1])
print(sort_phone_book3)

print 
print(":::항목삭제:::")
del phone_book3['김재현']
print(phone_book3)

print("::전체삭제::")
phone_book3.clear()
print(phone_book3)