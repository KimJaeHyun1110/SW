'''
작성일 : 9월 13일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 90페이지 문제 3.0
        평균 시속과 이동시간을 입력받아
        이동 시간은 시,분,초 단위로 출력하고
        이동한 거리를 계산하여 출력하시오.
'''
#1. 시속과 시간을 입력받는다
speed=float(input('평균 시속을 입력해 주세요(단위 km/h): '))
time=float(input('이동 시간을 입력해 주세요: '))

'''
계산방법
소숫점을 포함한 시간의 소숫점부분이 분 초 단위라 가정하면 60을 두번 곱하여 초로 변환한다
초를 60으로 나누면 60분 이상이 되며 이를 60으로 나눈 몫은 시간이며 남은 나머지가 분이된다
예시로 6000초라 하면 60을 나눔으로 100분이 되며 이를 60으로 나누면 몫은 1 나머지는 40이 되며
이는 1시간 40분임을 뜻한다 어차피 60을 나누는 과정이니 초같은 경우 모든 계산을 한 후에
60으로 나눈 나머지를 저장하면된다 예로 6025초 라면 이를 60으로 나눌시 몫은 100이고
나머지는 25가되니 나머지인 25가 초 단위인 것이다
'''

#2. 계산을 위해 시간을 초 단위로 변환해준다
s=int(time*60*60)
#3. 초를 60으로 나눈 몫에 60을 나눈 몫을  hour변수에 저장해준다.
h=(s//60)//60#혹은 int((s/60)/60)도 가능
#4. 초를 60으로 나눈 몫에 60을 나눈 나머지를 min변수에 저장해준다.
m=(s//60)%60
#5. 초를 60으로 나눈 나머지를 sec변수에 저장해준다.
s=s%60
print("평균 시속 : {} km/h".format(speed))
print("이동 시간 : {} 시간 {} 분 {} 초".format(h,m,s))
print("이동 거리 :",speed*time,"km")