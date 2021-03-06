class Solution:

    #Problem:
    #이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다.
    # N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다.
    # 그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다.
    # 각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다.
    # 이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다.
    # 만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면
    # 다음 라운드에서 1번을 부여받고, 3번↔4번에서 겨루는 게임에서 3번이 승리했다면
    # 다음 라운드에서 2번을 부여받게 됩니다. 게임은 최종 한 명이 남을 때까지 진행됩니다.
    # 이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와
    # 몇 번째 라운드에서 만나는지 궁금해졌습니다.
    # 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
    # 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와
    # 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요.
    # 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.

    def solution(self,n,a,b):
        nth_round=0
        while a!=b:
            a=(a+1)//2
            b=(b+1)//2
            nth_round+=1
        return nth_round

    # Other's solutions:
    # Solution key: using XOR operator and
    # int.bit_length() which gives number of bits requried to represent an integer in binary
    def solution_o1(self,n,a,b):
        return ((a-1)^(b-1)).bit_length()
    
    # Solution key: a,b each gets its participant number halved when moving onto the next round
    # When they compete and only one winner is found, their numbers are the same
    # so answer increases by 1 until that round. 
    def solution_o2(self,n,a,b):
        answer = 0
        while a != b:
            answer += 1
            a, b = (a+1)//2, (b+1)//2
        return answer

    # Solution key:
    # same idea as above, but the 
    def solution_o3(self,n, a, b):
        answer = 0
        while True:
            if a  == b:
                break
            else:
                if a % 2 == 1:
                    a = a // 2 + 1
                else:
                    a = a // 2
                if b % 2 == 1:
                    b = b // 2 + 1
                else:
                    b = b // 2
                answer += 1
        return answer


s1=Solution()
print(s1.solution(8,4,7))

