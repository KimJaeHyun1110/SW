'''
작성일 : 11월 1일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 7장 튜플
'''

#1. 도시튜플을 저장하는 리스트를 선언한다
city_info=[('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]

#2. 각종 필요변수를 선언한다
max_population=0
min_population=9999999999999
total_population=0
max_city=None
min_city=None

#3. city_info리스트에 더이상 불러올 원소가 없을때 까지 순서대로 원소를 불러와 city에 저장한다
for city in city_info:
    #3-1. 불러온 도시튜플의 인구수인 튜플의 1번지를 전체 인구수에 더한다
    total_population+=city[1]
    #3-2. 만약 도시의 인구수가 max_population보다 큰가
    if city[1]>max_population:
        #3-2-1. max_population에 도시 인구수를 저장한다
        max_population=city[1]
        #3-2-2. max_city에 city를 저장한다
        max_city=city
    #3-3. 만약 도시의 인구수가 max_population보다 큰가
    if city[1]<min_population:
        #3-3-1. max_population에 도시 인구수를 저장한다
        min_population=city[1]
        #3-3-2. max_city에 city를 저장한다
        min_city=city

#4. 최대인구를 가진 도시를 출력하기위해 max_city의 0번지를 이름, 1번지를 인구수로 출력한다
print('최대인구: {}, 인구: {}천명'.format(max_city[0],max_city[1]))
#5. 최소인구를 가진 도시를 출력하기위해 MIN_city의 0번지를 이름, 1번지를 인구수로 출력한다
print('최소인구: {}, 인구: {}천명'.format(min_city[0],min_city[1]))
#6. 도시 평균인구를 출력하기위해 총인구에 city_info의 길이를 나눠주고 그 결과를 출력한다
print('리스트 도시 평균 인구: {}천명'.format(total_population/len(city_info)))