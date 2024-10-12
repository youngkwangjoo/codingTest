def solution(myString, pat):
    # myString에서 pat이 마지막으로 등장하는 위치를 찾음
    last_index = myString.rfind(pat)
    
    # 마지막으로 pat이 끝나는 부분까지의 문자열을 반환
    return myString[:last_index + len(pat)]
