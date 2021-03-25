class Solution:

    # Problem:
   
    # You have two options to move:
    # (1) jump k steps by using k amount of battery or
    # (2) move instantly to the (jx2)th step by using no amount of battery,
    # where j is the number of steps you've come so far.
    # You need to find what's the smallest amount of battery consumption in order to move n steps.
    
    # Example) In order to move 5 steps, I used the 1st option by consuming battery amount of 1
    # and taking 1 step. Then I used the 2nd option to use no battery and move to the (1x2=)2nd step.
    # Then I used the 2nd option again to move to (2x2=)4th step.
    # Lastly, I used the 1st option to move 1 more step to get to the 5th step.
    # In total, I used 2 amount of battery. There are several other options and out of all,
    # the smallest amount of battery consumption is 2.


    # Solution key: imagine going backward, from the destination nth step to 0th step.
    # Since you want to use the 2nd option the most, and the 1st option the least,
    # you want to move backward by dividing the nth step by half. 
    # But when the nth step is an odd number, you must've had no other option but to use the 1st option.
    
    def solution(self, n):
            # p = amount of battery used
            # x = next step after using the 2nd option
            p,x=0,0
            while n>=0:
                # When nth step is an odd num, must use 1 amount of battery to get the next even num.
                if n%2==1:
                    x=(n-1)//2
                    p+=1
                # When nth step is an even num, use 2nd option, use no battery
                else:
                    x=n//2
                # Iterate by placing x into n (remaining steps)    
                n=x
                # When reached the 0th step, quit
                if n==0:
                    break
            return p

    
s1 = Solution()
print(s1.solution(5000))
            
        
