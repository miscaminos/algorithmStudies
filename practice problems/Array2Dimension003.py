#practice array problems

studentsClasses=[[2, 3, 1, 7, 3],[4, 1, 9, 6, 8],[5, 5, 2, 4, 4],\
                 [6, 5, 2, 6, 7],[8, 4, 2, 2, 2]]

def problem2_11(numOfStudents, studentsClasses):
    answer, maxnum=0,0
    for s1 in range(numOfStudents): #for each one of students
        count=0
        for s2 in range(numOfStudents): #for each one of comparing students
            for c in range(5): #for each class
                if studentsClasses[s1][c]==studentsClasses[s2][c]:
                    count+=1
                    break; #need to break after counting one comparing student
                    # in order to avoid counting the same person twice
        if count>maxnum:
            maxnum = count # update maxnum only when count is greater
            answer=s1+1 #index s2 started at 0, add 1 to get the correct student number
    return answer  

problem2_11(5,studentsClasses)     