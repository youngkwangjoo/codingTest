def solution(my_string, indices):
    answer = list(my_string)
    result = ""
    for i in range(len(my_string)):
        if i not in indices:
            result += my_string[i]
        
    return result