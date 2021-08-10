N, K = map(int, input().split())
sales = list(map(int, input().split()))

# wrong solution - time limit over
# this will cause time consumption to be as high as O(N*K)
def solution1(N, K, sales):
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

# Sliding window
# The time consumed can be reduced to O(N) by using sliding window.
# Let window of length K slide throughout the array sales
def solution2(N, K, sales):
    sum = 0
    for i in range(K):
        sum+=sales[i]
    ans=sum
    for j in range(N-K):
        sum-=sales[j]
        j+=K
        sum+=sales[j]
        if sum>ans:
            ans=sum
    return ans

print(solution2(N,K,sales))