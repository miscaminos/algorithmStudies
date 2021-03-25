class Solution:
    # Problem:
    # 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이
    # 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은
    # 앞에 있는 기능이 배포될 때 함께 배포됩니다.
    # 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
    # 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
    # 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
    #
    # Example) given:
    # progresses=[95, 90, 99, 99, 80, 99]
    # speeds=[1,1,1,1,1,1]
    # solution=[1,3,2]

    # Solution Key:
    #
    # Find an array of remaining days of each function (calculated by (100-progresses[i])/speeds[i]))
    # When the later function has smaller remaining days, it will only be abled to be published after
    # the earlier function with the bigger remaining days is published first.
    #
    # So, switch the remaismaller ning days of later functions with the bigger remaining days of earlier function.
    # How? each remaining day act like a "standard" to compare against
    # each of other remaining days of functions later than the "standard".
    # Setup a conditional statement:
    # if(remaining days' index>"standard"'s index & remaining days < standard)
    # then remaining days = standard
    #
    # Then, I have an array of remaining days in asc order where later functions' remaining days are
    # all set equal to the remaining days of earlier function
    #
    # Finally, count the number of unique elements in the array of remaining days to find the solution

    #need to improve efficiency
    def solution(self, progresses, speeds):
        remainDays=[]
        i=0
        while i<len(progresses):
            x=(100-progresses[i])/speeds[i]
            remainDays.append(x)
            i+=1
        #print(remainDays)
        j=0
        for x in remainDays:
            stnd=x
            j=remainDays.index(x)
            while j<len(remainDays):
                if(j>remainDays.index(stnd) and remainDays[j]<stnd):
                     remainDays[j]=stnd   
                j+=1
        #print(remainDays)
        unique=[]
        ans=[]
        cnt,k=0,0
        for x in remainDays:
           if x not in unique:
              unique.append(x)
        #print(unique)
        for x in unique:
            for y in remainDays:
                if y==x:
                    cnt+=1
            ans.append(cnt)
            cnt=0

        #print(ans)
        return ans
    
    # Other's solution:
    # Solution key:
    # Let time increases by 1, and check the condition:(progresses[0] + time*speeds[0]) >=100
    # When >=100 is satisfied, remove from the array (using pop(index=0)) and add 1 to the count.
    # Since, we are checking the condition and removing from the 0th index,
    # the condition in which earlier function must be published first is satisfied.
    
    # Until the progress of 0th index function reaches 100,
    # only the else statement will be called, and time will increase.
    # When time has flown enough to have progress exceed 100, function is popped and count increase by 1
    
    # Else is called only after pop & count++, so after removing all the earlier completed functions,
    # the total added count is put into the answer array and time increases by 1.
        
    def solution_o(self, progresses, speeds):
        print(progresses)
        print(speeds)
        answer = []
        time = 0
        count = 0
        while len(progresses)> 0:
            if (progresses[0] + time*speeds[0]) >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                if count > 0:
                    answer.append(count)
                    count = 0
                time += 1
        answer.append(count)
        print(answer)
        return answer

s1=Solution()
progresses1=[95, 90, 99, 99, 80, 99]
speeds1=[1, 1, 1, 1, 1, 1]

progresses2=[93, 30, 55]
speeds2=[1,30,5]
#s1.solution(progresses2, speeds2)

s1.solution_o(progresses2, speeds2)
