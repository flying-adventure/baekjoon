for i in range(int(input())):
    num,text = input().split()
    for k in text:
        print(k*int(num), end="")
    print()