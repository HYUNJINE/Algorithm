x= int(input())
# 생각을 해보자.
# d[0]
# 정수는 0 부터 3만이다.
# 0일때  0  1일 때 0번이다.
# 2일때 1번 
# 3일때 1번
# 4일 때 2번
# 5일 때 1번
# 6일때 2번
# 7일때 3  번
# 8일 때 4번 ? 아니지 4랑 d[4] + 1 이랑  더 작은 값 계산해줘야지.... 그니까 3이야
# 9일때 4? 아니지 d[3] + 1이랑 계산 2번이지 ㅋ
# 10일때 3 ? 아니지 d[5] + 1 이랑 계산 ㅋ  2번이지 ㅋㅋ
# 11일때 3 번이겠지 ㅋ
# 12일때 4? 아니지 d[6] + 1  , 즉 3



d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i] , d[i //2] + 1)
    if i % 3 == 0:
        d[i] == min(d[i], d[i//3] + 1)
    if i % 5 ==0:
        d[i] = min(d[i], d[i // 5] + 1)

    
print(d[x])







#쉽게 생