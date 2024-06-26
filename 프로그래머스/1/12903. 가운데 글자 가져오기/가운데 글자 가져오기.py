def solution(s):
    answer = ''
    x = len(s)
    if x % 2 == 1:
        return s[x // 2]
    else:
        return s[x // 2-1] + s[x//2]
