def solution(myStr):
    answer = []
    result = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    answer = result.split()
    
    return answer if answer else ["EMPTY"]  # 빈 리스트일 경우 "EMPTY" 반환