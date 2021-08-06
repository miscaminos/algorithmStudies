N,M = map(int, input().split())
arr1=sorted(list(map(int, input().split())))
arr2=sorted(list(map(int, input().split())))

def problem3_1(arr1, arr2):
    arr1.extend(arr2)
    return sorted(arr1)

problem3_1(N, arr1, M, arr2)

# the solution above gets runtime error
# sorting a list of n numbers, the big O =O(n*logn)
# if n=60,000, then we consume O(60,000*log16) =960,000
# so we should use pointers instead.
# when using pointers to sort a list of n numbers,
# the big O =O(n) ==>we simply need to go though n steps, instead of nlogn

# for each of arr1 and arr2, use pointers

N,M = map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))

def problem3_1(N, arr1, M, arr2):
    p1, p2 = 0,0
    ans=[]
    while p1<N and p2<M:
        if arr1[p1]<=arr2[p2]:
            ans.append(arr1[p1])
            p1+=1
        else:
            ans.append(arr2[p2])
            p2+=1

    while p1<N:
        ans.append(arr1[p1])
        p1+=1
    while p2<M:
        ans.append(arr2[p2])
        p2+=1
    return ans

print(problem3_1(N, arr1, M, arr2))



            