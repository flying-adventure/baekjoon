hour, min = map(int, input().split())
if min>=45:
    print(hour,min-45)
if min<45:
    hour-=1
    min+=15
    if hour<0:
        hour=23
    print(hour,min)
