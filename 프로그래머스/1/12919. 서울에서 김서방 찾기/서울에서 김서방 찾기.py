def solution(seoul):
    for idx, name in enumerate(seoul):
        if name == "Kim":
            answer = idx
            break  # "Kim"을 찾으면 반복문을 종료합니다.
    
    x = f"김서방은 {answer}에 있다"
    return x