def solution(myString, pat):
    count = 0
    pat_len = len(pat)
    
    # myString을 순차적으로 슬라이싱하며 pat과 비교
    for i in range(len(myString) - pat_len + 1):
        # pat과 일치하는 부분 문자열을 찾으면 count 증가
        if myString[i:i + pat_len] == pat:
            count += 1
    
    return count
