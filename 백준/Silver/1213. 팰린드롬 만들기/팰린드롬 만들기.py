# 문자열 길이가 짝수일때는 모든 문자가 짝수개만 있어야함
# 문자열 길이가 홀수일때는 문자 한종류만 홀수개, 나머지는 짝수개여야함.
import sys
from collections import Counter

N = input().strip()
cnt = Counter(N)

odd_chars = [ch for ch, v in cnt.items() if v % 2 == 1]
if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
    sys.exit(0)

middle = odd_chars[0] if odd_chars else ""

left = ""
for ch in sorted(cnt.keys()):
    left += ch * (cnt[ch] // 2)

print(left + middle + left[::-1])
    
    