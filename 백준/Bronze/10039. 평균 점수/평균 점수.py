#어째서 하루라도 코드를 안짜면 코드 짜는 방법을 홀라당 다 까먹는지?? 
#역시 난 슈퍼최강빡대가리인게 분명함~

sum=0

for i in range(0,5):
    score = int(input())
    if score <= 40:
        sum += 40
    if score > 40:
        sum += score
print(sum//5)   

    