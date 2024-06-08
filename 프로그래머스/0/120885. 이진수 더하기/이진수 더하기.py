def solution(bin1, bin2):
    
#2==10, 인덱스의 맨 끝부터 x[-1] + y[-1]
#if n == 2 append 10 
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    answer = num1 + num2 
    return bin(answer)[2:]