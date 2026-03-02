def solution(n, words):
    #단어를 집합에 저장, 단어가 집합에 들어있을 때 탈락
    #앞사람의 단어 맨 뒷자리와 해당 사람의 단어 앞자리가 동일하지 않을 때 탈락
    # 일정 구간의 숫자를 계속 반복할 때 % 연산자 활용하기
    user_word=set()
    prev=words[0][0]
    
    for idx,word in enumerate(words):
        turn=(idx//n)+1
        turn_peo=(idx%n)+1
        if prev!=word[0] or word in user_word:
            return [turn_peo,turn]
        user_word.add(word)
        prev=word[-1]
        
    return [0,0]