class Solution:
    
    # Problem: Is x a Harshad Number?
    # 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
    # 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
    # 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
    def solution(self, x):
        answer = True
        sum=0
        s=str(x).split()
        for a in s:
            b=int(a)
            sum+=b
        if(x%sum!=0):
            answer=False
        return answer
    
s1 = Solution()
print(s1.solution(521478))
