def solution(hp):
    #장군 공 5, 병정 공 3, 일 공 1
    x, y, z =5, 3, 1
    a = hp // x
    num1 = hp % x
    b = num1 // y
    num2 = num1 % y
    c = num2 // z
    
    return a + b + c
        