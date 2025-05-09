def solution(code):
    code = list(code)
    mode = 0
    ret = []

    for i in range(len(code)):
        if code[i] == "1":
            mode = 1 - mode  
        else:
            if mode == 0 and i % 2 == 0:
                ret.append(code[i])
            elif mode == 1 and i % 2 == 1:
                ret.append(code[i])
                
    answer = ''.join(ret)
    if answer == "":
        answer = "EMPTY"
    return answer
