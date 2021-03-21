class CodingTestCoreConcepts:

    #example problems from notion's (핵준특) 코딩테스트 핵심준비 특강

    #concept: stack & queue
    #problem1: Given a board of stacks, pop numbers from these stacks according to the
    #number of stack given by the moves array, and place the numbers in a bucket.
    #If the two consecutive numebrs are the same in the bucket, remove them.
    #Find the number of the removed numbers from the bucket.
    #(If the numbers left in the stack are all 0's, then move on to the next.)
    #
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

    #conept: 탐색(완전탐색, binary search)
    #problem2: Given a string, shorten the string by collapsing the repeated substrings  by
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

s1 = CodingTestCoreConcepts()
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
s1.stack_and_queue(board, moves)
string="abcabcdede"
s1.binary_search(string)
