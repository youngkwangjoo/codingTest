def solution(my_string, is_suffix):
    answer = 0
    m = len(is_suffix)
    a = my_string[-m:]
    if is_suffix == a:
        answer = 1
    else :
        answer = 0
    return answer