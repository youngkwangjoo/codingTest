def solution(numbers):
    # 음수 때문에 복잡해지는데 sort써서 오름차순하고 인덱스 0*1, number(Len(number)-1),-2 해서 더 큰걸 출력
    numbers.sort()
    x = numbers[1] * numbers[0]
    y = numbers[-1] *numbers[-2] 
    return max(x,y)