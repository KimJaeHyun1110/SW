'''
작성일 : 4월 5일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 사용자로부터 평점을 입력 받아 평점을 출력하고,
       입력된 평점이 4.2 이상이면
       "해외 연수 기회 부여"를 출력하는 프로그램을 작성하시오.
'''
#score변수를 선언 및 실수를 입력받는다
score=float(input("평점을 입력해주세요(예시: 4.2) : "))#입력 값을 실수형으로 변환을하고 변환결과를 score에 저장한다.

#score를 출력한다
print("당신의 평점은 {}점 입니다.".format(score))

#score가 4.2이상인가?
if score>=4.2:
    #결과가 참이라면 "해외 연수 기회 부여" 출력
    print("해외연수 기회 부여")

#결과에 상관없이 "감사합니다"출력
print("감사합니다.0")