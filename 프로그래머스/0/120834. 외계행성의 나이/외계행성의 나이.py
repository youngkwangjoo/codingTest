def solution(age):
    answer = ''
    b = ["a","b","c","d","e","f","g","h","i","j"]
    for i in str(age):
         if i.isdigit:
            num = int(i)
            answer += b[num]
    return answer