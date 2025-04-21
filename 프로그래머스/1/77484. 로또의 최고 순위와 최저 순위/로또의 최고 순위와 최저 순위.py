def solution(lottos, win_nums):
    number = 7
    number2 = 0  # 맞춘 개수
    number3 = 0  # 맞춘 개수 + 0의 개수

    if lottos.count(0) == 6:
        return [1, 6]

    elif lottos.count(0) == 0:
        for i in lottos:
            if i in win_nums:
                number -= 1
        if number > 6:
            number = 6
        return [number, number]

    else:
        for i in lottos:
            if i in win_nums:
                number2 += 1
                number3 += 1
            elif i == 0:
                number3 += 1

        x = 7 - number2
        y = 7 - number3

        if x > 6:
            x = 6
        if y > 6:
            y = 6

        return [y, x]
