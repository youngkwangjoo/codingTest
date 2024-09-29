def solution(todo_list, finished):
    # 결과를 저장할 리스트
    unfinished_tasks = []
    
    # zip을 사용해 두 리스트를 동시에 순회
    for todo, is_finished in zip(todo_list, finished):
        # 만약 finished 값이 False라면 아직 완료되지 않은 작업
        if not is_finished:
            # 해당 작업을 unfinished_tasks 리스트에 추가
            unfinished_tasks.append(todo)
    
    # 완료되지 않은 작업들의 리스트를 반환
    return unfinished_tasks
