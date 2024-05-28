def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i
    return "".join(sorted(answer))