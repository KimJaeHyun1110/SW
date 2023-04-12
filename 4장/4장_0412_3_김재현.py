'''
작성일 : 4월 12일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 한 과목의 점수를 입력 받아 점수에 따라 학점을 부여하여 출력하는 프로그램
'''

# 1. 한 과목의 점수를 정수로 입력받아 score에 저장한다.
score=int(input("점수를 입력해 주세요 : "))

# 2. 점수가 90이상이면 "A학점 입니다."를 출력합니다
if score>=90:
    print("{}점은 A학점 입니다.".format(score))

# 3. 아니고 만약 점수가 80이상이며 90미만이면 "B학점 입니다."를 출력합니다   
elif score>=80 and score<90:
    print("{}점은 B학점 입니다.".format(score))

# 4. 아니고 만약 점수가 70이상이며 80미만이면 "C학점 입니다."를 출력합니다   
elif score>=70 and score<80:
    print("{}점은 C학점 입니다.".format(score))

# 5. 아니고 만약 점수가 60이상이며 70미만이면 "D학점 입니다."를 출력합니다   
elif score>=60 and score<70:
    print("{}점은 D학점 입니다.".format(score))

# 6. 아니라면 "F학점 입니다."를 출력합니다   
else:
    print("{}점은 F학점 입니다.".format(score))