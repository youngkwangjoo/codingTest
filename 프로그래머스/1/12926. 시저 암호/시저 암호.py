def solution(s, n):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    for char in s:
        if char in lower:
            # 소문자일 경우
            index = lower.index(char)
            shifted_index = (index + n) % 26
            result.append(lower[shifted_index])
        elif char in upper:
            # 대문자일 경우
            index = upper.index(char)
            shifted_index = (index + n) % 26
            result.append(upper[shifted_index])
        else:
            # 공백일 경우
            result.append(char)
    
    return ''.join(result)