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



# //은 정수형을 나타내기 위한 연산자다.
# / 는 나누어 떨어져도 50.0 이런 실수형으로 나와버리니깐~
#그 외로 소수점 조절하는 방법 {:.2f}.format()   이거는 소수점 2자리까지  출력하겠다.
#print(f'어쩌규ㅜ저쩌구{sum: .0f}') f-string을 나타낼 수 있게 문자열 앞에 f를 붙여준다.
        
