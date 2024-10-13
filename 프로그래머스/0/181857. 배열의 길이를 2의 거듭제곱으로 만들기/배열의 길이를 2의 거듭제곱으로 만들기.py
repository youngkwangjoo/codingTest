def solution(arr):
    answer = []
    x = len(arr)
    if x & (x - 1) == 0:
        return arr
    y = 1
    while y < x:
        y *= 2
    arr.extend([0] * (y-x))
    return arr
        