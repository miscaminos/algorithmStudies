N = int(input())

# using two pointers algorithm
def solution(N):
    ans,sum=0,0
    lt=1
    for rt in range (1, int(N/2)+2):
        sum += rt
        if sum == N:
            ans+=1
        while sum >= N:
            sum -= lt
            lt+=1
            if sum == N:
                ans+=1
    return ans

# using quotient & remainder
def solution2(N):
    sum, limit, ans = 0,0,0
    for i in range(1,int(N/2)):
        sum+=i
        if sum>=N:
            limit=i
            break
    for j in range(2,limit+1):
        subtract=0
        for k in range(1,j+1):
            subtract +=k
        if (N-subtract)%j==0:
            ans+=1
    return ans

# better solution using quotient & remainder
def solution3(N):
    ans, cnt = 0,1
    N-=1
    while N>0:
        cnt+=1
        N=N-cnt
        if N%cnt==0:
            ans+=1
    return ans

print(solution3(N))

