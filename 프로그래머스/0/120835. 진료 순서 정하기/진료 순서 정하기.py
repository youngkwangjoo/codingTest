def solution(emergency):
    answer = {}
    emergencys = sorted(emergency, reverse = True)
    
    for i,v in enumerate(emergencys):
        answer[v] = i+1
    
    ranked_emergency = []
    
    for v in emergency:
        ranked_emergency.append(answer[v])

    return ranked_emergency
