package loop;

public class ConditionLoop01 {
	/* 1��: �ֿ乮��-���ǹ�
	 * ���ڿ� å�� �ְ� �ִµ�, ������ ���� ������ ���� �ʰ� �ִ��� ���� �־�� �Ѵ�. 
	 * �� ���ڿ� �ִ��� ���� å�� ���� ���� ���ڸ� �ݰ� ������ ��, ���� ���ڿ� å�� ���� �� �ִ�. 
	 * å�� �������� �׿��ִµ�, ������ ���� ���������� å�� ������ �Ѵ�.
	 * å���� ���Դ� int[] weights�ν� �־�����. 
	 * �� �迭�� ù ��° ��Ұ� �׿��ִ� å �߿��� ���� ���� �ִ� å�̰�, 
	 * �迭�� ������ ��Ұ� ���� �ؿ� �ִ� å�̴�. 
	 * ���ڿ� ���� �� �ִ� �ִ� ���Դ� int maxWeight �� �־�����. 
	 * å�� ���� ��� ���� ������ �ּ� ������ ���Ͻÿ�.
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

/* solution�� �ٽ�: for loop�� condition�� ����ϱ� 
	1) �ݺ������� weight�� ���ϰ�(for loop), ���� ���� maxWeight ���ؿ� ��(condition)
	2) ���� maxWeight���� Ŭ ��쿡 �� �ڽ��� �� á�ٴ� �ǹ̷� boxes���� 1 �߰�
 */
}
