'''
작성일 : 9월 27일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 5장 반복문
'''

#본인 이름 5개 출력
print(":: 내 이름 5개 출력하기 ::")
for i in range(5):
    print(i,"김재현")

print(":: 내 이름 5개 출력하기(리스트). ::")
for i in [1,2,3,4,5]:
    print(i,"김재현")

print(":: 리스트로 구구단의 19단 출력 ::")
for num in [1,2,3,4,5,6,7,8,9]:
    print(f"19 x {num} = {19*num}")

print(":: 문자열 내용 출력. ::")
for i in "HELLO":
    print("i=",i)

#도전문제 5.3
print("::: BTS 멤버 명단 출력. :::")
bts=['뷔','제이홉','알엠','정국','진','지민','슈가']
for name in bts:
    print(name)