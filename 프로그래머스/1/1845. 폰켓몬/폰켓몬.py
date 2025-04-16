def solution(nums):
    
    answer2 = len(set(nums))
    return min(answer2, len(nums)/2)