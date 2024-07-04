def solution(numbers, hand):
    # 키패드 좌표 초기화
    keypad = {
        1: (1, 1),
        2: (1, 2),
        3: (1, 3),
        4: (2, 1),
        5: (2, 2),
        6: (2, 3),
        7: (3, 1),
        8: (3, 2),
        9: (3, 3),
        0: (4, 2),
        '*': (4, 1),
        '#': (4, 3)
    }

    # 초기 왼손 위치와 오른손 위치 설정
    left_position = '*'
    right_position = '#'

    # 왼손과 오른손의 거리를 계산하는 함수
    def distance_to_hand(hand_position, target_position):
        hand_x, hand_y = keypad[hand_position]
        target_x, target_y = keypad[target_position]
        return abs(hand_x - target_x) + abs(hand_y - target_y)

    # 결과를 저장할 리스트
    result = []

    # 각 숫자에 대해 처리
    for num in numbers:
        if num in [1, 4, 7]:
            result.append('L')
            left_position = num
        elif num in [3, 6, 9]:
            result.append('R')
            right_position = num
        else:
            # 숫자가 2, 5, 8, 0 일 경우
            left_distance = distance_to_hand(left_position, num)
            right_distance = distance_to_hand(right_position, num)
            
            if left_distance < right_distance:
                result.append('L')
                left_position = num
            elif right_distance < left_distance:
                result.append('R')
                right_position = num
            else:
                # 거리가 같을 경우
                if hand == 'left':
                    result.append('L')
                    left_position = num
                else:
                    result.append('R')
                    right_position = num
    
    return "".join(result)