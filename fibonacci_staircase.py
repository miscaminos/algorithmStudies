class Solution:

# 문제: 효진이는 멀리 뛰기를 연습하고 있습니다.
# 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다.
# 멀리뛰기에 사용될 칸의 수 n이 주어질 때,
# 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내,
# 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.
# (제한사항: n은 1 이상, 2000 이하인 정수입니다.)

    def solution(self,n):
        answer =0
        prev_prev=1
        prev=1
        new_fib=0
        i=1

        # staircase의 n의 뛰는 방법의 수를 S(n)이라고 한다면,
        # staircase의 n이 1일때에는 뛰는 방법의 수는 1개임으로 1을 지정.
        # S(1)=1
        if n==1:
            answer=1%1234567
            
        # n개의 step를 뛰기위해서는,
        # 1step + n-1 steps를 뛰는 (n-1)개의 방법과
        # 2steps + n-2 steps를 뛰는 (n-2)개의 방법을 더하면된다.
        # S(n) = S(n-2) + S(n-1)
        # 어디서 많이 본 pattern인데....Fibonacci!!!
        
        # Fibonacci sequence: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3,...
        # S(n) sequence: S(0)=1. S(1)=1, S(2)=2, S(3)=3, S(4)=5,....
        # staircase의 n의 뛰는 방법의 수는 (n+1번째) Fibonacci숫자와 같다.
        # (이미 if n=1, then S(n)=1으로 1개 shift한 상태임으로,
        # 아래와같이 n>1 경우의 S(n)을 찾으면 총 방법의 수를 찾을 수 있다!
        else:
            while i<n:
                new_fib = prev_prev + prev
                prev_prev = prev
                prev = new_fib
                i+=1
            answer = new_fib%1234567
        return answer

s1 = Solution()
print(s1.solution(6))
