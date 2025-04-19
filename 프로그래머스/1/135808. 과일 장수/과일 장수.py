def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    for i in range(0, len(score) // m*m, m):
        answer1 = score[i:i+m]
        answer += min(answer1) * m  
    return answer
# 1~k 점까지 k는 최상품 
# 한상자에 M개를 담아 상자에 최하점이 P면 p x m이 가격이야
# 어떻게 팔아야 최대 이익인가
# 가장 큰값이 m으로 나눠지는가 나눠지면 그대로 리스트에 추가 
    