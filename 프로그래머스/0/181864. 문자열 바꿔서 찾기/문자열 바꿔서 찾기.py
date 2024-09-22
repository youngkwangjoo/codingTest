def solution(myString, pat):
    answer = 0
    result = ""
    for i in myString:
        if i == "A":
            result += "B"
        else:
            result += "A"
    if pat in result:
        return 1
    else:
        return 0
