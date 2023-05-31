'''
작성일 : 5월 31일
학과 : 컴퓨터공학부
학번 : 202395010
이름 : 김재현
설명 : 레포트1번 6장 2번
'''
#1. 소수 저장 리스트 생성
sosu=[]
#2. i가 1부터 1000 까지반복
for i in range(1,1001):
    #3. j가 1부터 i까지 반복
    for j in range(1,i):
        #4. j에 1을 더한 값과 i가 같은가?
        if j+1==i:
            #4-1. 같다면 sosu리스트 뒤에 i 값 추가
            sosu.append(i)
        #4-2. 아니고 만약 i를 j로 나눈 나머지가 0이고 j는 1보다 큰가
        elif i%j==0 and j>1:
            #4-2-1. 참이라면 반복문을 빠져나가라
            break
#5. 소수 리스트 출력
print("==소수리스트==")
#6. i가 0부터 sosu의 길이만큼 반복 하며 소수값 출력
for i in range(0,len(sosu)):
    print(sosu[i])
#7. 소수의 총 길이 출력
print("==소수의 갯수: {}개==".format(len(sosu)))