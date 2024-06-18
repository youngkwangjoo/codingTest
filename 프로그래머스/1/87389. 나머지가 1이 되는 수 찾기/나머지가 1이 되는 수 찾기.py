def solution(n):
    num_list = []
    for i in range(1,n):
        if n % i == 1:
            num_list.append(i)
    answer = min(num_list)
    return answer