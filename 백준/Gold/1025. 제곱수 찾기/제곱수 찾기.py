import math

def is_perfect_square(x):
    if x < 0:
        return False
    s = int(math.isqrt(x))
    return s * s == x

def find_largest_perfect_square(n, m, grid):
    largest_square = -1
    
    for i in range(n):
        for j in range(m):
            for di in range(-n, n):
                for dj in range(-m, m):
                    if di == 0 and dj == 0:
                        continue
                    
                    num_str = ""
                    ni, nj = i, j
                    while 0 <= ni < n and 0 <= nj < m:
                        num_str += grid[ni][nj]
                        num = int(num_str)
                        if is_perfect_square(num):
                            largest_square = max(largest_square, num)
                        ni += di
                        nj += dj
    
    return largest_square

# 입력 받기
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# 가장 큰 완전 제곱수 찾기
result = find_largest_perfect_square(n, m, grid)
print(result)
