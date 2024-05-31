def solution(my_string):
    answer = 0
    result = ''
    for i in my_string:
        if i.isdigit():
            result += i
        else:
            if result:
                answer += int(result)
                result = ''
    if result:
        answer += int(result)
    
    return answer
