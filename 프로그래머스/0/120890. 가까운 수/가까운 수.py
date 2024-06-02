# def solution(array, n):
#     answer = 0 
#     result = []
#     for i in array:
#         absv = abs(i-n)
#         result.append(absv)
#     min_num = min(absv)
#     min_index = result.index(y)
#     answer = array.index(x)
#     return answer
def solution(array, n):
    differences = [(abs(x - n), x) for x in array]  # (차이, 값) 형태의 튜플 리스트 생성
    min_difference = min(differences, key=lambda x: (x[0], x[1]))  # 가장 가까운 값 중 가장 작은 값을 선택
    return min_difference[1]