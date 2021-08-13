str1 = input()
str2 = input()

def solution(str1, str2):
    chars1 = dict(); chars2 = dict()
    keys1=[]; keys2=[]
    for a in range(len(str1)): keys1.append(str1[a])
    for b in range(len(str2)): keys2.append(str2[b])

    for k1 in set(keys1):
        cnt=0
        for i in range(len(str1)):
            if k1==str1[i]: cnt+=1
        chars1[k1]=cnt
    for k2 in set(keys2):
        cnt=0
        for j in range(len(str2)):
            if k2==str2[j]: cnt+=1
        chars2[k2]=cnt
    tmp=0
    print("chars1: ", chars1)
    print("chars2: ", chars2)
    for c1 in chars1:
        for c2 in chars2:
            if c1 == c2:
                tmp+=1
    print("tmp: ",tmp)
    
    if tmp == len(chars1):
        ans="YES"
    else: ans="NO"
    return ans
        
print(solution(str1, str2))        
