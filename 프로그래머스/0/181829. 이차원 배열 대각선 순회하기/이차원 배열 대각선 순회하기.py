def solution(board, k):
    total_sum = 0
    
    # Iterate over the rows and columns of the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Check if the condition i + j <= k is satisfied
            if i + j <= k:
                total_sum += board[i][j]
    
    return total_sum