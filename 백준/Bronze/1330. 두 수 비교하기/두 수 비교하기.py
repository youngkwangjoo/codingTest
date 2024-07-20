input_line = input().strip()

# 입력된 문자열을 공백으로 분리하여 두 정수로 변환합니다.
A, B = map(int, input_line.split())

if A > B:
    print(">")
elif B > A:
    print("<")
elif A == B:
    print("==")