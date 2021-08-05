N, M = map(int, input().split())
ranks = [list(map(int,input().split())) for _ in range(M)]

def problem2_12(N,M,ranks):
    pairs=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            cnt=0
            for s in range(M):
                pos_i, pos_j=0,0
                for t in range(N):
                    if ranks[s][t]==i:
                        pos_i=t
                    if ranks[s][t]==j:
                        pos_j=t
                if pos_i<pos_j:
                    cnt+=1
            if cnt==M:
                pairs+=1
    return pairs

print(problem2_12(N,M,ranks))