# @는 *3 , %는 +5 , # = -7



for k in range(0, int(input())):

    oh_shit = list(input().split()) #수학식 입력 받기
    number = float(oh_shit[0])
    
    for i in range(1, len(oh_shit)):
        if oh_shit[i] == '@':
            number *= 3
        if oh_shit[i] =='%':
            number += 5
        if oh_shit[i] == '#':
            number -= 7

        
    print("%0.2f" %number) 

