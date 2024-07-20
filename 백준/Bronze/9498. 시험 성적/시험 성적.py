# 입력을 받습니다.
score = int(input().strip())

# 조건문을 사용하여 점수에 따라 학점을 출력합니다.
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')
