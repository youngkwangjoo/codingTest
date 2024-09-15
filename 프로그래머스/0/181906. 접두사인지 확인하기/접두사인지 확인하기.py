def solution(my_string, is_prefix):
    # my_string의 앞에서 is_prefix 길이만큼 잘라서 비교
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0