def solution(sizes):
    answer_sort = []
    #그럼 가로세로 상관없이 sort로 크기정렬한다음에 두개중 큰거 가져오면되는거 아닌가?
    for i in sizes:
        sort_size = sorted(i,reverse = True)
        answer_sort.append(sort_size)
    
    max_l = 0
    max_r = 0
    #오름차순된 answer_sort에서 큰 가로세로 뽑아서 곱하기
    for i in answer_sort:
        max_l = max(max_l, i[0])
        max_r = max(max_r, i[1])
    answer = max_l * max_r
    return answer