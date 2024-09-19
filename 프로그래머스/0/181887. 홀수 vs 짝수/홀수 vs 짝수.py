def solution(num_list):
    """
    주어진 리스트의 짝수 인덱스 요소들의 합과 홀수 인덱스 요소들의 합 중 큰 값을 반환합니다.

    Args:
        num_list: 숫자들의 리스트

    Returns:
        짝수 또는 홀수 인덱스 요소들의 합 중 큰 값
    """

    even_sum = sum(num_list[i] for i in range(0, len(num_list), 2))
    odd_sum = sum(num_list[i] for i in range(1, len(num_list), 2))
    return max(even_sum, odd_sum)