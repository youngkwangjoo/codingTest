def solution(d, budget):
    answer = 0
    #b가 주어질때 이걸 최대한 많은 수를 넣는다. 이러면 sort로 배열해가지고
    #그걸 b에서부터 빼서 0이 나오는지 보면되겟네
    d.sort()  # 신청 금액을 오름차순으로 정렬
    count = 0  # 지원한 부서의 수
    for amount in d:
        if budget - amount < 0:
            break
        budget -= amount
        count += 1
    return count