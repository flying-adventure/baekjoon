x_p = []
y_p = []

for _ in range(3):
    x, y = map(int, input().split())
    x_p.append(x)
    y_p.append(y)

for i in range(3):
    if x_p.count(x_p[i]) ==1:
        x4 = x_p[i]
    if y_p.count(y_p[i]) ==1:
        y4 = y_p[i]

print(x4, y4)
        