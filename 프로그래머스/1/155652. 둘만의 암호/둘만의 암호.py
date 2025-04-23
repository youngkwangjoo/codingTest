def solution(s, skip, index):
    answer = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
         'y', 'z']
    falpha = []
    
    for i in alpha:
        if i not in skip:
            falpha.append(i)

    for j in s:
        num = falpha.index(j)
        nums = (num + index) % len(falpha)
        answer.append(falpha[nums])
    return "".join(answer)