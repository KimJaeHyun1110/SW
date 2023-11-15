'''
작성일 : 11월 15일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 9장
'''
s="happyday"
print(s[0])
print(s[6:10])#6~9
print(s[:-2])#0~뒤에서 2번째 앞 까지
s='Welcome to python'
print(s.split('.'))

s='2023.11.15'
print(s.split('.'))

s='Hello, world!'
print(s.split(','))

s='Hello, world!'
print(s.split(','))

#공백제거 strip()
s='welcome, to, python, and, bla , bla     '
print(s.strip())
print([x.strip() for x in s.split(',')])

print(list('hello world!'))

#문자열 연결 : join()
print(','.join(['apple','grape','banana'])) #,를 붙여서 연결하라.
print('-'.join('010.1234.5678'.split('.'))) #.으로 구분된 번호를 -로 고친다.

#.을-로바꾸기
print('010.1234.5678'.replace('.','-')) #.으로 구분된 번호를 -로 고친다.

s='helloworld'
print(s)
#s에 저장된 문자열을 리스트로 문자열 분리시켜 slist에 저장
slist=list(s)
print(slist)
#분리된 문자를 다시 합치기
print(''.join(slist))

#줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string='Today as well, \n\t Have a Happy Day.'
print(a_string)

#문자열 자르기 word_list에 저장.
word_list=a_string.split()
print(word_list)

#다시 합치기
refined_string=" ".join(word_list)
print(refined_string)

#대소문자 변환과 문자열 삭제
s='Hello, World!'
print(s)
print(s.lower())
print(s.upper())

#공백 제서 strip()
s='     Hello, World!        '
print(s.strip())#왼쪽,오른쪽 모든 공백 제거
print(s.lstrip())
print(s.rstrip())

s='#######Hello, World!#######'
print(s)
print(s.lstrip('#'))

#문자열 찾기
s='www.silla.ac.kr'
print(s.find('.kr'))
print(s.find('x'))#-1(문자열이 없다)

#.이 몇개인가
print(s.count('.'))