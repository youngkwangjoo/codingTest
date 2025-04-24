import re

def solution(dartResult):
    tokens = re.findall(r'\d{1,2}[SDT][*#]?', dartResult)
    scores = []

    for i, token in enumerate(tokens):
        # 숫자 추출
        num = int(re.match(r'\d+', token).group())
        # 보너스 문자
        bonus = re.search(r'[SDT]', token).group()
        # 옵션 (있을 수도 없을 수도)
        option = re.search(r'[*#]', token)
        option = option.group() if option else ''

        # 보너스 처리
        if bonus == 'S':
            score = num
        elif bonus == 'D':
            score = num ** 2
        elif bonus == 'T':
            score = num ** 3

        # 옵션 처리
        if option == '*':
            score *= 2
            if i > 0:
                scores[i-1] *= 2
        elif option == '#':
            score *= -1

        scores.append(score)

    return sum(scores)
