class Solution:

    #problem:
    #1부터 n까지 번호가 붙여진 n개의 가방이 있다. 각 가방은 다른 가방에 넣을 수 있으며,
    #다른 가방에 들어간 가방 역시 다른 가방을 넣고 있을 수 있다.
    #문제의 명확성을 위해 가방 i가 가방 j의 안에 있다는 것은 가방 i가 가방 j에 직접적으로 들어있음을의미한다.
    #예를 들어서, 가방 2가 가방 1 안에 있고, 가방 3이 가방 2 안에 있으면,
    #가방 3은 가방 2 안에 있지만 가방 1 안에 있지는 않다.
    #모든 가방은 처음에 다 빈 채로 바닥에 놓여 있다.
    #우리는 다음에 나열되는 것들 중 하나의 행동을 각각 단계적으로 취할 것이다.
    #PUT i INSIDE j - 가방 i를 가방 j안에 넣는다. 이 행동을 취하기 위해서는 가방 i와 j는 반드시
    #바닥에 놓여있어야 한다.SET i LOOSE - 가방 i안에 있는 모든 가방을 다시 꺼내서 바닥에 놓는다.
    #이 행동을 취하기 위해서는 가방 i는 반드시 바닥에 놓여 있어야 한다.
    #SWAP i WITH j - 가방 i와 가방 j의 내용물을 서로 바꾼다
    #(다시 말하면, 가방 i의 모든 내용물을 꺼내서 가방 j에 넣고, 가방 j의 모든 내용물을 꺼내서 가방 i에 넣는다). 
    #이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여 있어야 한다.
    #가방들이 놓여진 마지막 상태에서 어떤 가방도 자기보다 더 작은 번호의 가방 안에
    #들어가 있지 않을 때, 이 상태를 적절하다고 말한다.
    #주어진 가방의 개수 **int n**과 취할 행동의 단계 **vector<string> actions**를 이용하여
    #마지막 상태가 적절한지 판단하여라.
    #만약 적절하다면 마지막 상태에 바닥에 놓인 가방의 개수를 반환하여라.
    #적절하지 않거나 어느 단계의 행동이 유효하지 않다면 -1을 반환하여라.
    
    #solution:
    #배울점: be able to express all necessary states in one dictionary
    # ex) ground = dict() : n+1개의 요소를 가지고있음 (index# & bad# match하기 위해)
    # where ground[x]=y means "x"bag is inside "y"bag and if y=0, "x"bag is on the ground
    # an array of string은 아래와 같이 한번에 each string의 element를 access할 수 있음!
    #   for action in actions:
    #       action = action.split("give delimiter")
    def solution(n, actions):
        # 가방이 어디에 놓여있는지 나타내기 위한 리스트 선언
        # 각 인덱스는 가방의 번호를, 원소는 해당 가방이 놓여있는 가방의 번호를 나타냄 
        # ex) ground[1] = 2 : 1번 가방이 2번 가방 안에 놓여있음 
        # 0: 땅에 놓여있음을 의미 
        # 인덱스와 가방번호를 맞춰주기 위해 n+1 길이의 리스트로 생성 
        ground = [0] * (n+1)

        for action in actions:
            action = action.split(' ') # 공백을 기준으로 action 문자열 분리 
            if action[0] == 'PUT':
                i, j = int(action[1]), int(action[3])
                if (ground[i] | ground[j]) == 0: # 두 가방은 반드시 땅에 놓여있어야 함
                    ground[i] = j # i가 j안에 놓여있음을 마킹 
                else:
                    return -1
            elif action[0] == 'SET' :
                i = int(action[1])
                if ground[i] == 0: # 가방 i는 반드시 바닥에 놓여있어야 함 
                    # ground 리스트를 순회하며 가방이 i안에 있다면
                    # 바닥에 놓음(0으로 마킹)
                    for j in range(1, n+1):
                        if ground[j] == i: 
                            ground[j] = 0 
                else:
                    return -1
            elif action[0] == 'SWAP':
                i, j = int(action[1]), int(action[3])
                if (ground[i] | ground[j]) == 0: # 두 가방은 반드시 땅에 놓여있어야 함
                    # ground 리스트를 순회하며 
                    # i안에 있는 가방과 j안에 있는 가방을 바꿔줌 
                    for c in range(1, n+1):
                        if ground[c] == i:
                            ground[c] = j
                        elif ground[c] == j:
                            ground[c] = i
                else:
                        return -1
        # 완성된 ground 리스트에 대해
        # 바닥에 놓여진 가방의 개수를 카운트해준다
        # 만약, 가방이 자신의 가방 번호보다 더 작은 번호의 가방에 들어가있다면, 적절하지 않으므로 -1을 리턴한다 
        ans = 0
        for i in range(1, n+1):
            if ground[i] == 0:
                ans += 1
            elif ground[i] < i:
                return -1
        return ans



    #mysolution:
    def solution5(self, n, actions):
        #마지막 상태 적절여부:proper=0 부적절, proper=1 적절
        proper=0
        #바닥에 놓인 가방 수
        ans=0
        #state array: 가방이 바닥에 있을시 True, otherwise False
        state=[]
        for bags in range(n):
            state.append(True)
        order=[]
        all_order=[]
        for x in actions:
            order=x.split(" ")
            all_order.append(order)
        print(all_order)
        
        #inside array: 각 가방이 가지고있는 가방 수
        #inwhichbag dict: 각 가방이 (key) 들어가있는 가방 번호(value)
        inside=[]
        inwhichbag={}
        for i in range(n):
            inside.append(0)
            inwhichbag[i]=0
        
        for k in range (0, len(all_order)):
            word=all_order[k][0]
            i=int(all_order[k][1])-1
            if len(all_order[k])>3:
                j=int(all_order[k][3])-1
            bgs=list(inwhichbag.keys())
            if word=="PUT" and (state[i]==True and state[j]==True):
                if i<j:
                    proper=1
                    inside[i]+=1
                    state[i]=False
                    inwhichbag[i]=j
                else:
                    ans=-1
            elif word=="SET" and state[i]==True:
                proper=1
                inside[i]=0
                for t in inwhichbag.values():
                    if t==i:
                        state[bgs[i]-1]=True
            elif word=="SWAP" and (state[i]==True and state[j]==True):
                proper=1
                temp=inside[j]
                inside[j]=inside[i]
                inside[i]=temp
                temp=inwhichbag.get(j)
                inwhichbag[bgs[j]]=inwhichbag.get(i)
                inwhichbag[bgs[i]]=temp 
            else:
                proper=0
        #적절하다면 바닥에 있는 가방 몇개?      
        if proper==0:
            ans=-1
        else:
            for g in state:
                if g==True:
                    ans+=1
        return ans
