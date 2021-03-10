class Solution:
    #problem1 : 민아는 새 차를 사려고 합니다.
    #그녀는 돈이 여유롭지 않아 싼 차를 선호합니다.
    #문제가 있다면, 가장 싼 차는 품질이 의심스럽다는 점입니다.
    #그래서 민아는 자동차 가격표를 만들고 세 번째로 낮은 가격의 차를 사기로 결심했습니다.
    #vector<int> prices 가 주어집니다.
    #같은 가격이 vector<int> prices 에서 여러 번 나올 수 있지만,
    #가격 순서에는 한 번만 반영합니다.
    #solution
    #배울점: set(prices)를 사용하면 더 간단하게 given array prices내 중복 요소를 제외할 수 있다
        def solutionkey1(self, prices):
        #자동차의 가격을 오름차순으로 정렬한다.
        price = sorted(set(prices))
        #만약 자동차가 3개보다 적을경우 -1을 리턴한다.
        if(len(price)<3):
            result = -1
        #3개보다 많을 경우 가격이 3번째로 낮은 차의 가격을 결과에 저장한다.
        else:
            result = price[2]   
        return result

    #my solution:
        def solution1(self, prices):
        ans=0
        unique=[]
        for x in prices:
            if x not in unique:
                unique.append(x)
        if(len(unique)<3):
            ans=-1
        else:
            unique.sort()
            ans=unique[2]
        return ans

    #problem2: 문자열 배열 **vector<string> text**가 있습니다.
    #모든 문자열이 가장 긴 문자열의 길이와 동일한 길이를 가지도록 하고 싶습니다.
    #만약 어떤 문자열의 길이가 가장 긴 문자열의 길이보다 짧다면, 길이가 가장 긴 문자열의 길이와 같아 질때 까지, 그 문자열의 앞에 빈문자를 추가합니다.
    #위 규칙대로 변환된 문자열 배열을 리턴하세요.
    #solution:
    #배울점: No need to make  separate array of lengths.
    # Just work with length numbers and utilize while loop to repeat adding " " right num of times.
        def solutionkey2(self, text):
            max = 0;
            for i in text:
                if len(i) > max:
                    max = len(i)      
            for i in range(len(text)):
                while len(text[i]) < max:
                    text[i] = " " + text[i]
            return text
        
    #my solution:
        def solution2(self, text):
            lengths=[]
            ans=[]
            for x in text:
                lengths.append(len(x))
            maxlength=max(lengths)
            for y in text:
                if(len(y)<maxlength):
                    y=" "*(maxlength-len(y))+y
                    ans.append(y)
                else:
                    ans.append(y)
            return ans
        
    #problem3: 정렬할때, 숫자들을 문자열 처럼 취급하는것은 흔한 실수입니다.
    #예를 들어, ["1", "174", "23", "578", "71", "9"]와 같이 정렬된 배열은 해당 요소가
    #문자열이 아닌 숫자로 해석되는 경우 올바르지 않습니다.
    #문자열 비교를 사용하여 정렬된 문자열 배열 **vector<string> sequence**가 제공됩니다.
    #숫자 비교를 사용하여 이 시퀀스를 오름차순 정렬하여 리턴하세요.
        def solutionkey3(self, sequence):
            newArray = []
            result = []
            #string형 리스트를 int형으로 변환한다.
            for i in range(len(sequence)):
                newArray.append(int(sequence[i]))  
            #list를 오름차순 정렬한다.
            list.sort(newArray)
            #다시 string형 리스트로 변환한다.
            for i in range (len(newArray)):
                result.append(str(newArray[i]))    
            #결과를 반환한다.
            return result

    #my solution:
        def solution3(self, sequence):
            temp=[]
            ans=[]
            for x in sequence:
                y = int(x)
                temp.append(y)
            temp.sort()
            for z in temp:
                w=str(z)
                ans.append(w)
            return ans
