package loop;

public class ConditionLoop01 {
	/* 1번: 주요문법-조건문
	 * 상자에 책을 넣고 있는데, 상자의 무게 제한을 넘지 않고 최대한 많이 넣어야 한다. 
	 * 한 상자에 최대한 많이 책을 넣은 다음 상자를 닫고 봉인한 후, 다음 상자에 책을 넣을 수 있다. 
	 * 책은 차곡차곡 쌓여있는데, 무조건 가장 위에서부터 책을 꺼내야 한다.
	 * 책들의 무게는 int[] weights로써 주어진다. 
	 * 이 배열의 첫 번째 요소가 쌓여있는 책 중에서 가장 위에 있는 책이고, 
	 * 배열의 마지막 요소가 가장 밑에 있는 책이다. 
	 * 상자에 담을 수 있는 최대 무게는 int maxWeight 로 주어진다. 
	 * 책을 전부 담기 위한 상자의 최소 개수를 구하시오.
	 */
    public int solution(int[] weights, int maxWeight){
        int sum=0, numBoxes=0;
        if(weights.length>0){
	    	 numBoxes = 1;
	    	 int i=0, j=0;
	    	 for (i=j; i<weights.length;i++) {
	    		 sum += weights[i];
	    		 if(sum>maxWeight) {
	    			 numBoxes++;
	    			 sum=0;
	    			 j=i-1;
	    			 i=j;
	    		 }
	    	 }	 
	     }
         return numBoxes;
    }

/* solution의 핵심: for loop과 condition을 사용하기 
	1) 반복적으로 weight를 더하고(for loop), 더한 합을 maxWeight 기준에 비교(condition)
	2) 합이 maxWeight보다 클 경우에 한 박스가 다 찼다는 의미로 boxes수에 1 추가
 */
}
