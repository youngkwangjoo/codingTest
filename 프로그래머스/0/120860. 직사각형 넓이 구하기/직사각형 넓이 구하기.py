def solution(dots):
    # x좌표와 y좌표를 각각 분리
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]

    # x좌표의 최대값과 최소값 차이가 직사각형의 가로 길이
    width = max(x_coords) - min(x_coords)
    
    # y좌표의 최대값과 최소값 차이가 직사각형의 세로 길이
    height = max(y_coords) - min(y_coords)

    # 넓이 계산
    return width * height