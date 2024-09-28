def solution(myString, pat):
    answer = 0
    resultm = myString.upper()
    resultp = pat.upper()
    
    if resultp in resultm:
        return 1
    else:
        return 0