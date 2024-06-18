def solution(numbers):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    answer = []
    for i in num_list:
        if i not in numbers:
            answer.append(i)
    return sum(answer)