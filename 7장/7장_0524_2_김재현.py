'''
실습예제7-1
랜덤으로 1~100사이의 값을 10개 생성한 세트 2개 만들고,
합집합, 교집합, 차집합을 출력하시오.
[알고리즘]
1.비어있는 세트 2개 만들기
2.렌덤으로 2개의 세트에 각각 10개의 값 저장.
반복하면서 10개의
1)값 저장(추가).
3.2개의 세트값 출력
합집합, 교집합, 차집합 출력
'''
import random
set1=set()
set2=set()
for i in range(10):
    set1.add(random.randint(1, 10))
    set2.add(random.randint(1, 10))

print("세트 set1 내용 : ",set1)
print("세트 set2 내용 : ",set2)
print("set1과 set2의 합집합",set1|set2)
print("set1과 set2의 교집합",set1&set2)
print("set1과 set2의 차집합",set1-set2)
'''
세트 set1 내용 :  {1, 2, 3, 5, 8, 9, 10}
세트 set2 내용 :  {1, 2, 4, 5, 6, 10}
set1과 set2의 합집합 {1, 2, 3, 4, 5, 6, 8, 9, 10}
set1과 set2의 교집합 {1, 2, 10, 5}
set1과 set2의 차집합 {8, 9, 3}
'''