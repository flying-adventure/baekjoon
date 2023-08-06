#재밌겠다
#서로 다른 n개의 자연수의 합이 s일 때 자연수 n의 최댓값
#을 어떻게 알지?
s = int(input())
#일단 입력 받고,,,,,,자연수 n의 최댓값을 구하려면 1씩 차이나는 자연수....
num=0
sum=0
while sum<=s:
    num += 1
    sum += num


        
print(num-1)    