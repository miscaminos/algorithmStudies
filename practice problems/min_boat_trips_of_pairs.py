import math
class Solution:
    #Problem:
    # 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다.
    # 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
    # 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고
    # 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만
    # 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
    # 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
    # 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
    # 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

    #other's solutions:
    # solution key: arrange the people array in asc order
    # check the first(lightest) + last(heaviest) pair and "remove" them by shifting the index a, b
    # total num of pairs - num of the "removed" pairs = remaining person
    # since the people array was already sorted and the ones heavier than the limit are already removed,
    # one more trip is needed for one remaining person
    # so the total num of trips = total people - num of "removed" pairs

    #using list's pop, remove, del supposedly causes bad efficiency
    # this method avoids using those methods
    def solution_o1(self, people, limit) :
        answer = 0
        people.sort()
        a = 0
        b = len(people) - 1
        while a < b :
            if people[b] + people[a] <= limit :
                a += 1
                answer += 1
            b -= 1
        return len(people) - answer
    
    #brute-force solution with flaws. Need to find a better way!!
    def solution(self, people, limit):
        totalpairs, overweight,pairweight=0,0,0
        ans=0
        options=[]
        n=len(people)
        totalpairs = math.factorial(n)/(2*math.factorial(n-2))
        
        for i in range(0,n):
            for j in range(i+1,n):
                pairweight = people[i] + people[j]
                overweight=abs(pairweight-limit)
                options.append([overweight,pairweight, people[i], people[j]])      
        print(options)

        while(len(options)>0):
            overs=[]
            for z in options:
                overs.append(z[0])
            min_over=min(overs)
            print(min_over)
            saved=[]
            for x in range(len(options)):
                if options[x][0]==min_over:
                    saved=options[x]
                    if options[x][1]<=limit:
                        ans+=1
                        break
                    else:
                        ans+=2
                        break
            print(saved)
            print(ans)
            remain=[]
            for y in options:
                if(y[2]!=saved[2] and y[3]!=saved[3]):
                    remain.append(y)
            print(remain)
            options=remain
            for q in people:
                if q==saved[2]: 
                    people.remove(q)
            for p in people:
                if p==saved[3]:
                    people.remove(p)
            print(people)
                    
        if len(people)>0:
            if people[0]>limit:
                ans+=int(people[0]//limit)
            else:
                ans+=1
        print(ans)
        return ans

    from collections import deque
    def solution_o2(people, limit):
        result = 0
        deque_people = deque(sorted(people))

        while deque_people:
            left = deque_people.popleft()
            if not deque_people:
                return result + 1
            right = deque_people.pop()
            if left + right > limit:
                deque_people.appendleft(left)
            result += 1
        return result

s1=Solution()
limit1=200
people1=[160, 150, 140, 60, 50, 40]
limit2=100
people2=[70,50,80,50]
limit3=100
people3=[70,80,50]
limit=240
people=[100,240,40,40,60,80,80]

print(s1.solution_o1(people,limit))
