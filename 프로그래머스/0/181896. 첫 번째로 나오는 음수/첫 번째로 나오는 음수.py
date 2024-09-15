def solution(num_list):
    answer = 0
    for index,i in enumerate(num_list):
        if i < 0:
            return index
    return -1