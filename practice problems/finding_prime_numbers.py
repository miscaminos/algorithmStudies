# finding prime numbers under 1,000
counter=0
for n in range(2,1001):
    for i in range(2,n):
        counter+=1
        if n%i==0:
            break
    else:
        print(n)
print("number of divisions executed: ",counter)


# improvement-1
counter=0
ptr=0
prime=[None]*500

prime[ptr]=2
ptr+=1

for n in range(3,1001,2):
    for i in range(1,ptr):
        counter+=1
        if n%prime[i]==0:
            break
    else:
        prime[ptr]=n
        ptr+=1

for i in range(ptr):
    print(prime[i])
print("number of divisions executed: ",counter)


# improvement-2
counter=0
ptr=0
prime=[None]*500

prime[ptr]=2
ptr+=1

prime[ptr]=3
ptr+=1

for n in range(5,1001,2):
    i=1
    while prime[i]*prime[i] <=n:
        counter +=2
        if n%prime[i]==0:
            break
        i+=1
    else:
        prime[ptr]=n
        ptr+=1
        counter+=1

for i in range(ptr):
    print(prime[i])
print("number of divisions executed: ",counter)