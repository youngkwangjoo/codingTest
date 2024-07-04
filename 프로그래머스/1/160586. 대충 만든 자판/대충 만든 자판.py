def create_keymap_dict(keymap):
    dic = {}
    for index, string in enumerate(keymap):
        for pos, char in enumerate(string):
            # 딕셔너리에 문자가 없거나 현재 pos가 더 작을 경우 갱신
            if char not in dic or pos + 1 < dic[char]:
                dic[char] = pos + 1
    return dic

def solution(keymap, targets):
    answer = []
    dic = create_keymap_dict(keymap)
    
    for target in targets:
        count = 0
        for char in target:
            if char in dic:
                count += dic[char]
            else:
                count = -1
                break
        answer.append(count)
                             
    return answer
