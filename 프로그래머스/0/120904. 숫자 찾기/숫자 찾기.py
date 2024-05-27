def solution(num, k):
    strn = str(num)
    kn = str(k)
    for i, x in enumerate(strn):
        if x == kn:
            return i+1
    return -1