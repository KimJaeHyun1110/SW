'''
작성일 : 11월 15일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 9장
    트위터 메시지 처리의 단어 추출
    띄어쓰기로 문자열을 분리하고. 단어의 개수를 찾아라.
'''
text="There's a reason some people are working to make it harder to vote, especially for people of color. It’s because when we show up, things change."

#띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.
#len()=>길이(개수):리스트의 항목 찾는 함수
print(len(text.split()))

#도전문제 9.1
#회사 이름은 **로 표시
#KT, Samsung, LG, SKT
#1. 필요 리스트 및 변수 선언 원본 텍스트, 변환후 택스트, 회사리스트 com
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '
text2=""
com=['KT','SAMSUNG','LG','SKT']
#2. text를 공백으로 나눴을때 생성된 리스트에서 첫번째 부터 마지막까지 word에 원소를 하나씩 주면서 반복
for word in text.split():
    #2-1. com리스트에서 첫번째 부터 마지막까지 test에 원소를 하나씩 주면서 반복
    for test in com:
        #2-1-1. 만약 test랑 word를 대문자로 바꾼 문자열이랑 같다면 word에 '**'를 저장한다
        if test==word.upper():
            word='**'
    #2-2. text2에 word+' '를 더해준다
    text2+=word+' '
#3. 바뀌기 전 후 문자열을 출력해준다
print("===바꾸기전===")
print(text)
print("===바꾼 후===")
print(text2)