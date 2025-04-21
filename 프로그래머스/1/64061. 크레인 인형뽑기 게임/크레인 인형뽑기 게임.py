def solution(board, moves):
    result = []
    answer = []
    num = 0
    stack = []
    for col in range(len(board[0])): 
        new_row = []
        for row in board:
            new_row.append(row[col]) 
        result.append(new_row)

    for i in moves:
        col_index = i-1
        for j in result[col_index]:
            if j == 0:
                continue
            else:
                result[col_index][result[col_index].index(j)] = 0 
                if stack and stack[-1] == j:
                    stack.pop()
                    num += 2
                else:
                    stack.append(j)
                break
    return num

# 각 아이콘은 고유의 수를 갖게됨
# moves를 통해 가져온 숫자가 연속해서 같은 숫자일 경우 둘다 delete하면됨
# 나라면 배열을 바꾼다음에 0이면 pass 0이아니면 추가해서 같은 숫자면 그 수를 세