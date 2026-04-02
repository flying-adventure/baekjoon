import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()

    
    n = int(input_data[0])
    target_word = input_data[1]
    target_counter = Counter(target_word)
    
    similar_count = 0
    
    for word in input_data[2:]:
        current_counter = Counter(word)
        
        diff_minus = target_counter - current_counter
        diff_plus = current_counter - target_counter
        
        remain_minus = sum(diff_minus.values())
        remain_plus = sum(diff_plus.values())
        
        if remain_minus <= 1 and remain_plus <= 1:
            similar_count += 1
            
    print(similar_count)

if __name__ == "__main__":
    solve()