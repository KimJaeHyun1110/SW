'''
작성일 : 11월 1일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 7장 튜플
'''
#리스트생성
color_list=['red','green','blue','orange']
#튜플생성
color=('red','green','blue','orange')
#튜플 출력
print(f"color : {color}")
#color에 black추가하기
#color.append('black') append가 없기에 에러발생
#인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다
print('color 튜플 : ',color)
print('color 튜플 중 2,3,4번은?',color[1:4])
print('color 튜플 중 1,2,3번은?',color[:3])
print('color 튜플 중 3~번은?',color[2:])
print('color 튜플 중 1,3,5번은?',color[::2])
print('color 튜플 거꾸로 출력',color[::-1])
#튜플 끼리의 결합 => +연산자. 반복=> *연산자
colors=color+color
print(f"colors : {colors}")
print("color튜플을 10번 반복 :",color*10)