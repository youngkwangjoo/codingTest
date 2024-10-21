def solution(str_list):
    answer = []
    if "l" in str_list and "r" in str_list:
        lindex = str_list.index("l")
        rindex = str_list.index("r")
        if lindex < rindex:
            return str_list[:lindex]
        else:
            return str_list[rindex + 1:]
        return answer
    elif "l" in str_list:
        return str_list[:str_list.index("l")]
    elif "r" in str_list:
        return str_list[str_list.index("r")+1:]
    else:
        return []