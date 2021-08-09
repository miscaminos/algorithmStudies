N, K = map(int, input().split())
sales = list(int(input()) for _ in range(N))

def solution(N, K, sales):
    ans=0
    for r in range(K):
        ans+=sales[r]
    for i in range(N-K+1):
        tmp =0
        for j in range(i,i+K):
            tmp += sales[j]
        if tmp>ans:
            ans=tmp
    return ans

print(solution(N,K,sales))