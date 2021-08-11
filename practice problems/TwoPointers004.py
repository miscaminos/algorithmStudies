A,B = map(int, input().split())
arr1= list(map(int, input().split()))

# 시간복잡도 = O(N^2)
# n이 10만이상으로 큰 숫자이고 M이 100만이상으로 큰 숫자이라면,
# 너무 시간복잡도가 커지는 문제가 발생한다.
# O(N^2) --> can reduce to O(N) using two pointers algorithm

# wrong solution - time over
def solution1(N, M, arr):
    sum, count = 0,0
    for i in range(N):
        sum=arr[i]
        for j in range(i+1, N):
            if sum==M:
                count+=1
                break
            elif sum<M:
                sum+=arr[j]
            else:
                sum=0
    return count

# solution
def solution3(N, M, arr):
    cnt, lt, sum = 0,0,0
    for rt in range(N):
        sum+=arr[rt]
        if sum==M: 
            cnt+=1
        while sum >= M:
            sum-=arr[lt]
            lt+=1
            if sum == M:
                cnt+=1
    return cnt

print(solution3(A,B,arr1))