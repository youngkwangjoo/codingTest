def is_perfect_square(x):
    if x < 0:
        return False
    s = int(x**0.5)
    return s * s == x

def find_largest_perfect_square(N, M, table):
    max_square = -1
    
    for i in range(N):
        for j in range(M):
            for dr in range(-N, N):
                for dc in range(-M, M):
                    if dr == 0 and dc == 0:
                        continue
                    
                    num_str = ""
                    r, c = i, j
                    
                    while 0 <= r < N and 0 <= c < M:
                        num_str += table[r][c]
                        num = int(num_str)
                        if is_perfect_square(num):
                            max_square = max(max_square, num)
                        r += dr
                        c += dc

    return max_square

# 입력 받기
N, M = map(int, input().strip().split())
table = [input().strip() for _ in range(N)]

# 가장 큰 완전 제곱수 찾기
result = find_largest_perfect_square(N, M, table)

# 결과 출력
print(result)
