'''
작성일 : 9월 27일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 4장 조건문
        점수를 입력받아 학점을 출력하시오.
        90~100 A
        80~89 B
        70~79 C
        60~69 D
        0~59 F
'''
age=int(input('점수를 입력 해 주세요 :' ))
# 판단.
# 이 코드는 논리 오류가 발생한다.
print("첫 번째 성적처리")
if age>=90:
    print("A학점 입니다.")
elif age>=80:
    print("B학점 입니다.")
elif age>=70:
    print("C학점 입니다.")
elif age>=60:
    print("D학점 입니다.")
else:
    print("F학점 입니다.")
print()#개행
#정확한 범위를 지정하자. -성적의 범위를 벗어나면 잘못된 점수
print("두 번째 성적처리")
if 100>=age>=90:
    print("A학점 입니다.")
elif 90>age>=80:
    print("B학점 입니다.")
elif 80>age>=70:
    print("C학점 입니다.")
elif 70>age>=60:
    print("D학점 입니다.")
elif 60>age>=0:
    print("F학점 입니다.")
else:
    print("점수를 잘못 입력하셨습니다.")
print()#개행
#점수는 무조선 0~100점 사이입니다. -아니면 잘못된 입력입니다.
print("세 번째 성적처리")
if 100>=age>=0:
    if age>=90:
        print("A학점 입니다.")
    elif age>=80:
        print("B학점 입니다.")
    elif age>=70:
        print("C학점 입니다.")
    elif age>=60:
        print("D학점 입니다.")
    else:
        print("F학점 입니다.")
else:
    print("점수를 잘못 입력하셨습니다.")
print()#개행
