def solution(x):
    answer = True
    x_list = []
    str_x = str(x)
    for i in str_x:
        x_list.append(int(i))

    sum_x = sum(x_list)
    if x % sum_x == 0:
        return True
    else:
        return False