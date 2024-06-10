def solution(numbers, k):
    index = (2 * (k-1)) % len(numbers)   
    return numbers[index]

#넘버스의 길이는 랜덤이야 k의 값만큼 돌리면되는거고
#인덱스는 1부터 시작으로 보고 계산해보자. 인덱스 x+k값으로하고 x=0으로 정의
#만약에 numbers가 ?
