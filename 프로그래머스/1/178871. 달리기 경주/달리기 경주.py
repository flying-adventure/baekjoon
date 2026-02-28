def solution(players, callings):
    rank_dict = {player: i for i, player in enumerate(players)}
    
    for name in callings:
        # 2. 추월한 선수의 현재 등수와 앞 선수 파악
        current_rank = rank_dict[name]
        prev_rank = current_rank - 1
        prev_player = players[prev_rank]
        
        # 3. 리스트(players)에서 두 선수의 위치 교체
        players[prev_rank], players[current_rank] = players[current_rank], players[prev_rank]
        
        # 4. 딕셔너리(rank_dict)에서도 바뀐 등수 업데이트
        rank_dict[name] = prev_rank
        rank_dict[prev_player] = current_rank
        
    return players