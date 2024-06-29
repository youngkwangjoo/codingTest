def solution(s):

    lst = []
    for i in s:
        lst.append(i)
    answer = sorted(lst, reverse = True)
    answer_t = "".join(answer)
    return answer_t