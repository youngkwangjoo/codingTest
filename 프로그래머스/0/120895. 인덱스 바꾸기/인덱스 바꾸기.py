def solution(my_string, num1, num2):
    llist = list(my_string)
    llist[num1], llist[num2] = llist[num2], llist[num1]
    return "".join(llist)
        



#my_string[num1] == a 로 바꾸고, my_string[num2] == b 로 바꾼다음
# 출력을 my_string[num1]