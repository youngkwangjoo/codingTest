def solution(rank, attendance):
    x = []
    result = dict(enumerate(rank,start = 0))
    print(result)
    for i in range(len(rank)):
        if attendance[i] == True:
            x.append(rank[i])
    x.sort()
    keys_for_x = []
    for value in x:
        for key, val in result.items():
            if val == value:
                keys_for_x.append(key)
    a,b,c = keys_for_x[0], keys_for_x[1],keys_for_x[2]
    answer = a *10000 + b*100 +c
    return answer