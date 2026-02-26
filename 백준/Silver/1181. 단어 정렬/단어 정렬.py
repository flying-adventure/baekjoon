N=int(input())
word=set()
for _ in range(N):
    word.add(input().strip())
word=sorted(word,key=lambda x: (len(x),x))
for i in word:
    print(i)