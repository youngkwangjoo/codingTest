def solution(k, score):
    answer = []
    answer1 = []
    for i in score:
        answer.append(i)
        answer.sort(reverse=True)
        if len(answer) > k:
            answer.pop()
        answer1.append(answer[-1])
    return answer1

#매일 1명씩 노래를 부르는데 상위 k번째이면 명예의 전당에 올림
#k일까지는 숫자가 부족하니 모두 명예의 전당 k일 다음부터는 출연가수 점수가 k번째순위보다 높으면
#t순위가 바뀜 최하위 점수를 발표함