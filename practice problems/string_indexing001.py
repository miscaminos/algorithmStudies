class Solution:

# 문제: 주어진 string s 뒤에 0개 이상의 문자를 추가해 생성할 수 있는 
# 가장 짧은 팰린드롬을 찾기

    def solution(self, s):
        not_in = []
        copy = list(s)
        desc = []
        for i in copy:
            desc.append(i)
        desc.reverse()
        
        # string s 내부의 팰린드롬 찾기
        while True :
            if copy == desc :
                break
            else:
                not_in.append(copy[0])
                del copy[0]
                desc = []
                for i in copy:
                    desc.append(i)
                desc.reverse()
        
        # 팰린드롬에 포함되지 않은 요소들 붙여 주기
        copy = list(s)
        not_in.reverse()
        copy += not_in

        length = len(copy)
        return length, copy

# solution의 핵심: given string과 reverse를 비교하는 방식

# 1) 주어진 string s를 copy list로 변환 (index 단위로 사용하기 위해)
# 2) copy와 desc(copy의 reverse)가 일치하는지 확인
# 3) 일치하지 않는다면 string의 0번 index를 not_in으로 옮긴 후 다시 확인
# 4) copy가 팰린드롬임을 확인 OR len(copy)=1 때까지 1~3번의 작업을 반복
# 5) 수정된 copy를 다시 string s로 초기화하고  
# 6) 앞선 작업에서 팰린드롬에 포함되지 않아 not_in으로 이동된 요소들을 역순으로 바꿔줌 
# 7) 수정한 not_in을 copy의 마지막에 붙인 후 copy의 길이를 반환

s1 = Solution()
print(s1.solution('abcdee'))
