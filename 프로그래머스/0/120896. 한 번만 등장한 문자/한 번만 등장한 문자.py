def solution(s):
    answer = []
    for i in s:
        x = s.count(i)
        if x == 1:
            answer.append(i)
    answer.sort()
    return ''.join(answer)

#1개가 있을경우 1, 2개가 있을경우 2를 반환하는데 1만 가져오는 코드??