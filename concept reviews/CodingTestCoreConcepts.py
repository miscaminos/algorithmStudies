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
            return n*self.factorial(n-1)
        
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
            return u + self.recursion_solution(v)
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
            return "(" + self.recursion_solution(v) + ")" + new_u

#s1 = CodingTestCoreConcepts()
#s1.factorial(3)
#p="()))((()"
#s1.recursion_solution(p)


##############################################################################
        # concept: Floyd Warshall (플로이드 와샬) algorithm
        # problem: Find the shortest route with lowest cost
        # that passes through every node of given n nodes
        def solution_fw(n, costs):
            #비용 배열 values[]: all max values 2^31-1
            #2^31-1 : maximum number of 32bit integer values above zero
            #거리 배열 visited[]: all False
            values = [2**31-1 for i in range(n)]
            visited = [False for i in range(n)]
            #0번 node를 시작점으로 설정
            start = 0
            visited[start] = True
            values[start] = 0
            #방문하지 않은 node가 있다면 (visited 배열에 False가 있는 동안 실행)
            while False in visited:
                #node 완전 탐색으로 비용배열의 거리 값 최소화
                for i in costs:
                    if(visited[i[1]]==False and i[0]==start):
                        values[i[1]]=min(values[i[1]],i[2])
                    if(visited[i[0]]==False and i[1]==start):
                        values[i[0]]=min(values[i[0]],i[2])
                refer = 2**31-1
                #방문하지 않은 node중 최소 비용 node 위치 탐색
                for i in range(n):
                    if(visited[i] == False and values[i]!=0):
                        refer = min(refer,values[i])
                answer=0
                answer += refer
                #해당 node 방문 여부 check
                for i in range(n):
                    if(visited[i]==False and values[i]==refer):
                        visited[i]=True
                        #이동
                        start=i
                        break              

        # concept: Dijkstra(다익스트라) algorithm
        # problem: Find the shortest route from one particular node to another
        def solution_d(n, costs):
            #비용배열, 거리배열 선언
            visited = [False for _ in range(n)]
            cost = [sys.maxsize for _ in range(n)]
            #0번 node를 시작점으로 설정한 case
            visited[0] = True
            cost[0] = 0
            length = len(visited)
            #방문하지 않은 node가 있는 동안:
            while False in visited:
                #방문하지 않은 지역 중, 최소값 찾기
                checkLoc = -1
                checkValue = sys.maxsize
                #검사 할 후보를 하나씩 체크해서 가장 작은 cost의 node선택 (checkLoc에 대입)
                for i in range(length):
                    if visited[i] == False and cost[i] < checkValue:
                        checkLoc = i
                        checkValue = cost[i]
                #검사 할 후보가 없다면 탈출
                if checkLoc == -1:
                    break
                visited[checkLoc] = True
                #경로 완전탐색으로 비용배열 수정
                for v1, v2, c in costs:
                    #다음 이동할 node의 cost비교시,
                    #현재  node까지 오기위해 소모한  cost도 더해주어야한다
                    if v1 == checkLoc and visited[v2] == False:
                        cost[v2] = min(cost[v2], cost[v1]+c)
                    if v2 == checkLoc and visited[v1] == False:
                        cost[v1] = min(cost[v1], cost[v2]+c)
        
        # Dijkstra example problem
        # Find the shortest route
        import sys
        import heapq

        input = sys.stdin.readline
        INF = sys.maxsize

        #input V: node 개수, E: 간선의 개수, K:시작 node 번호
        V, E = map(int, input().split())
        K = int(input())
        #distance: 최단경로 값을 저장하는 list 
        distance = [INF]*(V+1)
        #graph: node들이 연결된 관계를 나타내는 list
        graph = [[]for _ in range(V+1)]
        #q: 우선순위 큐 (priority queue)
        pq = []

        for _ in range(E):
            #u에서 v로 가는 간선의 가중치 w으로 입력받은 값들을 mapping해서 graph에 추가
            u, v, w = map(int, input().split())
            graph[u].append((w,v))

        def solution(start):
            distance[start]=0
            heapq.heappush(pq, (0, start))
            while pq:
                #heap에 push된 가중치와 현재node번호를 가져와서
                weight, current = heapq.heappush(pq)
                #distance에서 현재 node의 가중치값이 더 작다면, continue
                if distance[current] < weight:
                    continue
                #graph에서 보이는 현node의 기준으로, 다음 node의 가중치 값이
                # (=현node까지의 가중치 + 다음 node 가중치)
                #distance에 저장된 가중치값보다 더 작다면,
                # 더 작은 가중치 값으로 distance의 값을 replace한 후, 다음 pq를 heap으로 push
                for w, nextNode in graph[current]:
                    if distance[nextNode] > weight + w:
                        distance[nextNode] = weight + w
                        heapq.heappush(pq, (weight+w, nextNode))
                        
        #check solution:
        solution(K)
        for i in range(1, V+1):
            print("INF" if distance[i] == INF else distance[i])


##############################################################################
        # concept: Greedy algorithm (탐욕법)
        # Greedy algorithm: 여러 경우 중 하나를 선택할때 
        # 가장 좋다고 생각하는것을 선택해 나가면 결과적으로도 최선이 될것이다

        # problem: 회의실 배정
        # 일찍 끝나는 회의를 선택하면, 결과적으로 가장 많은 회의 가능
        # 주의: 회의의 시작시간과 끝나는 시간이 같을 수 있다.

        import sys

        N = int(sys.stdin.readline())
        meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

        # 끝나는 시간 기준으로 정렬
        #--> meetings.sort(key = lambda x:x[1])

        #만약 동일한 끝시간이 있다면, 시작시간이 빠른것부터 정렬
        #람다식 설명: x[1]를 기준으로 먼저 정렬, 그다음에 x[0]를 기준으로 정렬
        #--> meetings.sort(key = lambda x:(x[1], x[0]))

        #solution:
        def solution(N,meetings):
            meetings.sort(key = lambda x:(x[1], x[0]))
            cnt = 0
            end_time =0
            for meeting in meetings:
                if meeting[0] >= end_time:
                    end_time = meeting[1]
                    cnt+=1
            return cnt


########################################################################
#concept: LinkedList & Trie structure
#LinkedList 구현:
#define Node:
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
#define LinkedList:
class LinkedList():
    def __init__(self):
        self.head = None
        self.count = 0

    #LinkedList 맨앞에 node 추가:   
    def appendHead(self, node):
        if self.head == None:
            self.head = node
            self.count = 1
        else:
            self.count +=1
            currentHead = self.head
            self.head = node
            node.next = currentHead

    #LinkedList 맨뒤에 node 추가:
    def append(self, node):
        if self.node == None:
            self.head = node
            self.count = 1
        else:
            now = self.head
            while now.next != None:
                now = now.next
            now.next = node
            self.count += 1

    #index위치에 node 추가:
    def insertNodeAtIndex(self,node,index):
        if index<0 or index>self.count:
            return -1
        elif self.count == index:
            self.append(node)
        elif index==0:
            self.appendHead(node)
        else:
            now = self.head
            while index>0:
                index -=1
                now = now.next
            self.count -=1
            nextNode = now.next
            now.next = node
            node.next = nextNode

    #node 삭제:
    def deleteData(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.count-=1
        else:
            first = self.head
            second = first.next
            while second != None:
                if second.data == data:
                    first.next = second.next
                    self.count-=1
                    break
                first = second
                second = second.next

    #연결리스트의 node 갯수 찾기:
    def getCount(self):
        return self.count

#Trie 구조 구현:
#define node:
class Node():
    def __init__(self,data):
        self.data = data
        self.children = {}
        
#define Trie structure:
class Trie():
    def __init__(self,data):
        self.head = Node(None)
        
    #Trie에 data insert:
    def insert(self, string):
        head = self.head
        for s in string:
            children = head.children
            if s not in children:
                children[s] = Node(s)
            head = children[s]

#binary search (이진탐색)기반의 길찾기 문제
#Given node의 x,y좌표(where every node has distinct x position)
#Nodes in the same level get same y position
#child node's y position is always smaller than the parent node's y position
# 1:[5,3],2:[11,5],3:[13,3],4:[3,5],5:[6,1],6:[1,3],7:[8,6],8:[7,2],9:[2,2]
# y position으로 level을 나누면: (from highest level 6 to lowest 1)
#                               7 -> 2,4 -> 1,3,6 -> 8,9 -> 5
# Preorder(전위순회) = DFS방식으로 트리 탐색 왼쪽먼저 전위, 그 다음 오른쪽 전위
# 결과 리스트 = [7,4,6,9,1,8,5,2,3]
# Postorder(후위순회) = 왼쪽 오른쪽 자식 노드부터 순서대로 탐색
# 결과 리스트 = [9,6,4,8,1,4,3,2,7]

# 해결 과정:
# 1)각 노드에 순서를 매긴다
# 2)노드에 고유한 level값을 찾는다 (y position)
# 3)level순서대로 역순 정렬한다
# level이 동일한 경우, x position이 작은 순서대로 정렬
# 4)트리에 각 순서값을 삽입
# 각 level에 대해 부모 노드의 x position보다 작으면 왼쪽 노드에 삽입,
# 부모 노드의 x position보다 크면 오른쪽 노드에 삽입
# 완성된 트리에 대해, 전위순회, 후위순회

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

def makeTree(nodes, levels, curLevel):
    cur = nodes.pop(0)
    root = TreeNode(cur[-1]) #마지막 element가 순서값

    if nodes:
        for i in range(len(nodes)):
            if nodes[i][1] == levels[curLevel + 1]: #동일한 레벨이면,
                #부모node의 x 값과 비교해서 더 작으면 왼쪽에 생성, 크면 오른쪽에 생성
                if nodes[i][0] < cur[0]:
                    root.left = makeTree([x for x in nodes if x[0] < cur[0]], levels, curLevel+1)
                else:
                    root.right = makeTree([x for x in nodes if x[0] > cur[0]], levels, curLevel+1)
    return root

preResult = []
def preorder(node):
    if node is None:
        return
    preorder(node.left)
    preorder(node.right)
    preResult.append(node.val)
    
    
postResult = []
def postorder(node):
    if node is None:
        return
    postResult.append(node.val)
    postorder(node.left)
    postorder(node.right)
    

def solution(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    nodeinfo = [i+[idx+1] for idx, i in enumerate(nodeinfo)]
    #nodeinfo의 x[1]는 desc order로, x[0]는 asc order로 정렬하기위해 "-x[0]" 
    nodeinfo = sorted(nodeinfo, key=lambda x:(x[1], -x[0]), reverse=True)

    root = makeTree(nodeinfo, levels, 0)

    preorder(root)
    postorder(root)
    return [postResult, preResult]
    

nodeinfo=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]        
print(solution(nodeinfo))