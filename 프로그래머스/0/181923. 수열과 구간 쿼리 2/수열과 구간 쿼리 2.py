def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        candidates = []
        for i in range(s, e + 1):
            if arr[i] > k:
                candidates.append(arr[i])
        if candidates:
            answer.append(min(candidates))
        else:
            answer.append(-1)
    return answer
