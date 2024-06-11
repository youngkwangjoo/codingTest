def solution(s):
    nump = 0
    numy = 0
    for i in s:
        if i == "p" or i == "P":
            nump += 1
        elif i == "y" or i == "Y":
            numy += 1
    return nump == numy
