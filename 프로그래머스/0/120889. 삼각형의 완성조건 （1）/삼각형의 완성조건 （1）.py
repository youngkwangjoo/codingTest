def solution(sides): 
    maxs = max(sides) 
    sums = sum(sides)
    if maxs >= sums - maxs :
        answer = 2
    else :
        answer = 1
    return answer
    