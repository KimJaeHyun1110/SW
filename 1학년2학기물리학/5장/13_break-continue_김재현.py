'''
작성일 : 10월 4일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문 
        반복을 제어하는 BREAK,CONTINUE
        교재 137 페이지

        Test word : programming
        예상출력
        break1,2 : pr
        continue : prgrmmng 
'''
word = input("단어를 입력하세요")
print("::break1::")
for i in word:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        break
    else:
        print(i,end='')
print()
print("::break2::")
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:#모음을 만나면 반복을 중한단다.
        break
    else:
        print(i,end='')
print()
print("::continue::")
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        continue    
    print(i,end='')
print()