import sys
input = sys.stdin.readline

N = int(input())
book_count = {}

for _ in range(N):
    book = input().strip()
    book_count[book] = book_count.get(book, 0) + 1

max_count = max(book_count.values())
answer = []

for book in book_count:
    if book_count[book] == max_count:
        answer.append(book)

answer.sort()
print(answer[0])