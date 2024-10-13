def solution(my_string, s, e):
    answer = ''
    result = my_string[s:e+1]
    result2 = result[::-1]
    return my_string[:s] + result2 + my_string[e+1:]