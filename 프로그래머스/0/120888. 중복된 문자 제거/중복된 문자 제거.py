def solution(my_string):
    x = set()
    result =[]
    for i in my_string:
        if i not in x:
            x.add(i)
            result.append(i)
    return "".join(result)
    
    
