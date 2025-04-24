def solution(wallet, bill):
    count = 0
    w, h = wallet
    bw, bh = bill

    while True:
        if (bw <= w and bh <= h) or (bh <= w and bw <= h):
            break
        
        # 긴 쪽을 반으로 접기
        if bw >= bh:
            bw = bw // 2
        else:
            bh = bh // 2
        
        count += 1

    return count

# 우선 wallet 과 bill의 크기를 비교 
#max(wallet) > max(bill)