class Solution:
    #problem:
    #당신에게 적군의 코드를 해석하라는 비밀 미션이 주어졌다.
    #당신은 그들이 메세지를 다음과 같은 방법으로 암호화한다는 것을 이미 알아냈다.
    #'a'와 'z'사이의 알파벳을 두자리수 01과 26 사이의 숫자에 할당한다.
    #메세지는 각 알파벳을 할당된 숫자로 변환하여 암호화된다.
    #예를 들어, 't'는 20에 할당되고, 'e'는 05에 할당되고,
    #'s'는 19에 할당되어 "test"는 "20051920"으로 암호화된다.
    #모든 원본 메세지는 소문자만으로 구성되어 있다.
    #주어진 **string code**에는 숫자와 문자의 할당이 나타나 있다.
    #첫번째 문자는 01에 할당되고, 두번째 문자는 02에 할당되는 식으로 26까지 이어진다.
    #또한 주어진 **string message** 에는 암호화되지 않은 원본 메세지 혹은 암호화된 메시지가 있다.
    #만약 원본 메세지가 주어졌다면 메세지를 암호화하여 반환하고,
    #암호화된 메세지가 주어졌다면 원본 메세지를 반환하라.

    #solution:
    #배울점: utilize isdigit(str) method (returns true if all characters in str are digits, false otherwise)
    #if the elements in an array are numbers (esp. if they are in order) use them as indices
    #Be able to use a string as an array of characters (get access to characters via index numbers)
    def solutionkey(self, code, message):
        answer = ""
        # message가 암호화된 메세지일 경우
        if message[0].isdigit():
            for i in range(0, len(message), 2):
                answer = answer + code[int(message[i:i+2])-1]
        # message가 암호화되지 않은 원본 메세지일 경우
        else:
            for i in range(len(message)):
                for j in range(len(code)):
                    if message[i]==code[j]:
                        if j+1<10:
                            answer = answer + "0" + str(j+1)
                        else:
                            answer = answer + str(j+1)                  
        return answer

    #my solution:
    def solution4(self, code, message):
        ans=[]
        alphs=list(code)
        nums=['01','02','03','04','05','06','07','08','09']
        for i in range(10,27):
            n=str(i)
            nums.append(n)
        #message로 alphabet이 주어진다면,
        if message[0] in alphs:
            msg=list(message)
            for x in msg:
                for i in range(26):
                    if x==alphs[i]:
                        y=nums[i]
                ans.append(y)
        #message로 numbers가 주어진다면,
        else:
            msg=[]
            for i in range(0, len(message), 2):
                e=message[i:i+2]
                msg.append(e)
            for z in msg:
                for j in range(26):
                    if z==nums[j]:
                        y=alphs[j]
                ans.append(y)
        answer=""
        for w in ans:
            answer+=w
        return answer

    
