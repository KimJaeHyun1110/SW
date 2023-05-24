'''
랜덤으로 로또번호 알려줘~
1. 로또 번호 저장 할 세트 만들기
2. 6번 반복하면서
1) 1~45사이의 값을 세트 변수에 추가
3. 로또번호 출력
'''
import random
lotto=set()
while not len(lotto)==6:
    lotto.add(random.randint(1, 45))
print("로또번호는",lotto,"입니다.")

lotto2=set()
while True:
    lotto2.add(random.randint(1, 45))
    if len(lotto2)==6:
        break
print("로또번호는",lotto2,"입니다.")