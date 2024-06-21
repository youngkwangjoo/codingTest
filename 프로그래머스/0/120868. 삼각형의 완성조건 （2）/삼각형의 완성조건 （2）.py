def solution(sides):
    #가능성은 a < b+c, b < a+c, c < b+a
    a, b = sorted(sides)
    return (a + b - 1) - (b - a + 1) + 1 
#           11 +7-1 17 -  -3