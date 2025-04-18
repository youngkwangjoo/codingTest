def solution(answers):
    answer = [0, 0, 0]
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == stu1[i % len(stu1)]:
            answer[0] += 1
        if answers[i] == stu2[i % len(stu2)]:
            answer[1] += 1
        if answers[i] == stu3[i % len(stu3)]:
            answer[2] += 1

    max_score = max(answer)
    result = []

    for i in range(3):
        if answer[i] == max_score:
            result.append(i + 1)  # 1번부터 시작하니까 +1

    return result
