#과조건이다 아님? 심사위원 수 없어도 되는디..

V = int(input())
vo = input()
A = vo.count("A")
B = vo.count("B")

if A < B:
    print("B")
elif A > B:
    print("A")
else:
    print("Tie")
    
