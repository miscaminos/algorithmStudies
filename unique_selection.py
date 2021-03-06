class Solution:
    # Problem:
    # 당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에,
    # 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다.
    # N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때,
    # N/2마리의 폰켓몬을 선택하는 방법 중,가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아,
    # 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.
    
    # Solution key:
    # If the number of unique types is greater than N/2, then you are limited to N/2 types of pokemon
    # else, you the max num of types you can get is the given num of unique types of pokemon
    def solution(self,nums):
        
        unique_types = []
        for x in nums:
            if x not in unique_types:
                unique_types.append(x)
        if len(unique_types) >= (len(nums)//2):
            answer = len(nums)//2
        else:
            answer = len(unique_types)
        return answer

s1 = Solution()
print(s1.solution([3,3,3,2,2,2]))
