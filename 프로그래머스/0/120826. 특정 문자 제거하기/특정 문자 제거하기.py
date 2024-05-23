def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i == letter:
            return my_string.replace(letter, '')
        else:
            answer += i
    return answer