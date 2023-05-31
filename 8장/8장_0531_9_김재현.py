'''
작성일 : 5월 31일
학과 : 컴퓨터공학
학번 : 202395010
이름 : 김재현
설명 : 8장 파일입출력
'''
#문장을 입력받아 파일에 저장
sentence=[]#빈 리스트 생성
#enter키를 입력 할 때까지 반복하여 문자 입력 받기
while True:
    text=input("저장할 문장 입력(종료: 엔터키): ")
    if text=='':
        break
    sentence.append(text+"\n")

print("입력될 리스트 : ",sentence)

#sentence.txt 파일에 내용 출력(쓰기)
with open("sentence.txt", "w") as f:
    '''
    for text in sentence:
        f.write(text)
    '''
    f.writelines(sentence)
print("sentence.txt파일이 생성 되었습니다.")
