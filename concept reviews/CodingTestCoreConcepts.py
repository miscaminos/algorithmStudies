class CodingTestCoreConcepts:

#Concept review and example problems from notion's (핵준특) 코딩테스트 핵심준비 특강

##############################################################################
    #concept: stack & queue
        #problem: Given a board of stacks, pop numbers from these stacks according to the
        #number of stack given by the moves array, and place the numbers in a bucket.
        #If the two consecutive numebrs are the same in the bucket, remove them.
        #Find the number of the removed numbers from the bucket.
        #(If the numbers left in the stack are all 0's, then move on to the next.)
    def stack_and_queue(self,board,moves):
        from collections import deque
        moves=deque(moves)
        buckets =[]
        cnt=0

        while moves:
            move = moves.popleft()

            for i in range(len(board)):
                doll = board[i][move-1]
                if doll!=0:
                    board[i][move-1]=0
                    if buckets and buckets[-1]==doll:
                        buckets.pop()
                        cnt+=2
                    else:
                        buckets.append(doll)
                    break
        print(cnt)
        return cnt

#board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
#moves=[1,5,3,5,1,2,1,4]
#s1.stack_and_queue(board, moves)


##############################################################################
    #conept: 탐색(완전탐색, binary search)
        #problem: Given a string, shorten the string by collapsing the repeated substrings  by
        #replacing the repated substrings with "number of repetition" + "repeated substring"
        # example) Given "abcabcabcde", the shortened version is "3abcde"
        # Find the length of the shortest shortened version of the given string.
    def binary_search(self, s):
        answer=len(s)
        unit=1
        while unit <= len(s)//2:
            word = ""
            count = 1
            #indexing을 이용한 string slicing. [시작점 (포함) :끝나는점 (미포함)]
            comp= s[ : unit]
            for i in range(unit, len(s), unit):
                if comp == s[i : i+unit]:
                    count +=1
                else:
                    if count ==1:
                        word += comp
                    else:
                        word += str(count) + comp
                    comp=s[i : i+unit]
                    count=1
            print(word+"\n")
                    
            if count ==1:
                word+=comp
            else:
                word+=str(count)+comp
            print(str(unit)+ ": "+word+"\n")
            unit +=1
            answer = min(len(word),answer)
        print(answer)
        return answer
    
#string="abcabcdede"
#s1.binary_search(string)


##############################################################################
    #concept: BFS(Breadth First Search)
        #Problem: Given a maze witd dimension N by M,
        # find the shortest distance of the route from starting point (0,0) to exit point (N-1,M-1).
        #import sys
        #from collections import deque
        #N,M = map(int, input().split())
        #maze = [input() for i in range(N)]   
    def BFS(self, N, M, maze):
        maze = list(map(lambda x: list(x), maze))
        dist = [[-1]*M for i in range(N)] #방문여부 확인 하기 위해 -1로 초기화
        #상하좌우
        dx = [1,0,-1,0]
        dy=[0,1,0,-1]

        q = deque()
        q.append((0,0))
        dist[0][0] = 0
        cnt = 0
        while q:
            cur = q.popleft() #(0,0)부터 시
            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]
                if nx >= 0 and nx < N and ny >=0 and ny < M:
                    if dist[nx][ny] < 0 and maze[nx][ny] == '1':
                        dist[nx][ny] = dist[cur[0]][cur[i]]+1
                        q.append((nx,ny))
        cnt = dist[N-1][M-1] + 1
        print(cnt)
        return cnt


##############################################################################
    #concept: Bitwise Computation
    # to convert n to binary(2진수) value: bin(n), to octal(8진수) value: oct(n), to hexadecimal(16진수) value: hex(n)
    # to convert n to decimal(10진수) value = int(n)
        # problem: Given a square map composed of n by n unit squares,
        # each square is either blocked or blank. Given two maps, find the overlapped version of these maps.
        # condition: If one map's particular unit square is blocked, then the overlapped map has that unit blocked.
        # In order for the overlapped map's unit square to be blank, that particular unit square of all maps must be blank.
        # ==> this condition translates to OR operation of two binary numbers.
        # Each map is encrypted as an array of decimal numbers
        # convert each row in the map into a binary number (0=blank, 1=blocked)
        # to get a string representation of the map (' '=blank, '#'=blocked)
    def bit_computation (self, n, arr1, arr2):
        answer = []
        for i in range(n):
            final_line  = str(bin(arr1[i] | arr2[i]))[2:]
            final_line = '0'*(n-len(final_line))+final_line
            final_line = final_line.replace('1', '#')
            final_line = final_line.replace('0', ' ')
            answer.append(final_line)
        print(answer)
        return answer

        # Enhance the computation above by modifying the for each statement
        # While "for i in range(n)" statement orders to iterate n times with a hidden counter,
        # zip( ) method can read each element of given sets in a simpler way.
        # "for a1, a2, ..., an in zip(array1, array2, ..., arrn)" : given n arrays which are all same lengths, this for each statement
        #                                                                           returns list of elements of the same index from each of the n arrays 
    def bit_computation_zip (self, n, arr1, arr2):
        answer = []
        for a1, a2 in zip(arr1, arr2):
            final_line  = str(bin(a1 | a2))[2:]
            final_line = '0'*(n-len(final_line))+final_line
            final_line = final_line.replace('1', '#')
            final_line = final_line.replace('0', ' ')
            answer.append(final_line)
        print(answer)
        return answer
    
#arr1=[48, 53, 33, 22, 31, 50]
#arr2=[27, 56, 19, 14, 14, 10]
#n=6
#s1.bit_computation_zip(n, arr1, arr2)


##############################################################################
    #concept: Hash (the concept of hash is used as dictionary in python)
    # Use key-value pairs in a dictionary to store, modify and retreive data about a chatroom
    #problem: Given a set of user ID and nicknames and actions(enter, change, leave) in an array "record"
    # find an array of log messages (in the same order as the given record) which announces
    # the action and the nickname(the final nickname of the user after re-entering the chatroom or changing the nickname)
    def find_chatlog(self, record):
        answer = []
        user_dict = {}
        chatlog = []
        enter_msg = "%s님이 들어왔습니다."
        leave_msg = "%s님이 나갔습니다."
        for rec in record:
            info = rec.split(" ")
            if info[0]=="Enter":
                user_dict[info[1]]=info[2]
                chatlog.append([enter_msg, info[1]])
            elif info[0]=="Leave":
                chatlog.append([leave_msg, info[1]])
            elif info[0]=="Change":
                user_dict[info[1]]=info[2]
        for log in chatlog:
            answer.append(log[0] % user_dict[log[1]])
        print(answer)
        return answer
    
#record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
#s1.find_chatlog(record)

    
##############################################################################        
    #concept: (재귀함수) Recursion
    # example1: factorial
    def factorial(self,n):
        if n==1:
            return 1
        else:
            return n*factorial(n-1)
        
    # example2: recursion problem (Kakao coding test 2020)
    # Follow the instructions to implement the logic described below:
    def recursion_solution(self,p):
        #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환 한다.
        if p =="":
            return p
        #2. 문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리한다.
        #   단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리 할 수 없어야 하며 v는 빈 문자열이 될 수 있다
        cnt, idx = 0, 0
        for i in range(len(p)):
            if p[i] == "(":
                cnt +=1
            else:
                cnt-=1
            if cnt ==0:
                idx = i
                break
        u, v = p[ :idx+1], p[idx+1: ]
        #3. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행한다.
        #   3-1. 수행한 결과 문자열을 u에 이어 붙힌 후 반환한다.
        if u[0] =="(":
            return u + recursion_solution(v)
        #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행한다.
        #   4-1. 빈 문자열에 첫번째 문자로 '('를 붙인다.
        #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        #   4-3. ')'를 다시 붙인다.
        #   4-4. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
        #   4-5. 생성된 문자열을 반환한다. 
        else:
            new_u=""
            u = u[1:-1]
            for i in u:
                if i == "(":
                    new_u += ")"
                else:
                    new_u += "("
            return "(" + recursion_solution(v) + ")" + new_u

#s1.factorial(3)
#p="()))((()"
#s1.recursion_solution(p)


##############################################################################
        # concept: Dynamic programming (동적계획법)
        # problem: 


        # concept: Dijkstra(다익스트라) algorithm
        # 
        
        
        
        
        
    


s1 = CodingTestCoreConcepts()
