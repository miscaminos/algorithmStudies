N,K=map(int, input().split())
arr =list(map(int, input().split()))

# correct solution
def solution2(N, K, arr):
    ans, length, lt, cnt_z = 0,0,0,0
    for rt in range(N):
        if arr[rt] == 0: cnt_z+=1
        while cnt_z>K:
            if arr[lt]==0: cnt_z-=1
            lt+=1
        # length = 연속된 1을 가진 수열의 길이
        length = rt-lt+1
        if length>ans: ans=length
    return ans

# wrong solution
def solution(K, arr):
    ans=0
    sum, lt, cnt_z = 0,0
    for rt in range(len(arr)):
        if cnt_z>=K:
            if arr[rt]==1:
                sum+=arr[rt]
            else:
                if sum>ans:
                    ans=sum
                    sum=0
        else:
            if arr[rt]==0:
                cnt_z+=1
                sum+=1
            else:
                sum+=arr[rt]
    return ans


print(solution2(N, K, arr))

