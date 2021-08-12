N = int(input())
str = input()

def solution(N, str):
    listall=[]
    for j in range(len(str)): listall.append(str[j])
    candidates = set(listall)
    result={}
    for c in candidates:
        cnt=0
        for i in range(N):
            if c == listall[i]:
                cnt+=1
        #print(c, "candidate received ", cnt)
        result[c]=cnt
    #rint(result)
    ans = max(result, key=result.get)
    return ans

print(solution(N, str))

