def solution(s):
    words = s.split(' ')  # 문자열을 공백 기준으로 분리
    answer = []
    
    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer.append(new_word)
    
    return ' '.join(answer) 