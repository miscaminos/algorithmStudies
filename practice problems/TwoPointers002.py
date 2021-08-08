n, m = map(int, input().split())
a = list(map(int, input().split()))
b= list(map(int, input().split()))

# problem 3_2
def solution(n,m,a,b):
    a.sort()
    b.sort()
    p1, p2 = 0,0
    ans =[]
    while p1<n and p2<m:
        if a[p1]==b[p2]:
            ans.append(a[p1])
            p1+=1
            p2+=1
        elif a[p1]<b[p2]:
            p1+=1
        else:
            p2+=1
    return ans

print(solution(n,m,a,b))