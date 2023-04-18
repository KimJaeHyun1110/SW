'''
작성일 : 4월 18일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 두 과목을 입력받아 학업 성취 우수도를 출력해주는 프로그램
'''

# 1. 두 과목의 숫자를 각각 sub1,sub2에 입력받는다
sub1=int(input("첫번째 점수를 입력해 주세요 : "))
sub2=int(input("두번째 점수를 입력해 주세요 : "))

# 2-1. sub1이 75이상이고 sub2도 75이상이면 우수도 알고리즘을 실행한다
if sub1>=75 and sub2>=75:
    
    #3. sub1+sub2의 결과를 total에 저장한다.
    total=sub1+sub2

    # 4. 만약 총점이 180 이상이면 "최우수학생"을 출력한다
    if total>=180:
        print("총점 {}점 으로 최우수학생 입니다.".format(total))

    # 5. 아니고 만약 총점이 160 이상이면 "우수학생"을 출력한다
    elif total>=160:
        print("총점 {}점 으로 우수학생 입니다.".format(total)) 
    
    # 6. 아니라면 "보통학생"을 출력한다
    else:
        print("총점 {}점 으로 보통학생 입니다.".format(total))

# 2-2. 아니면 "분발합시다." 라고 출력한다.
else:
    print("분발합시다.")