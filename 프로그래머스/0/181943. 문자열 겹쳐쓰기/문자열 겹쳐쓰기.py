def solution(my_string, overwrite_string, s):
    answer = ''
    os = len(overwrite_string)
    answer1 = my_string[:s]
    answer2 = my_string[s+os:]
    return answer1+overwrite_string+answer2