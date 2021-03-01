package Fibonacci;

public class FibonacciSum {

	/* problem:
	 * Finn�� ���� ���а��ο� ���� �ֽ��ϴ�. 
	 * ���� ���θ� �ϴ� Finn�� �ڿ��� n�� ������ �ڿ������ ǥ�� �ϴ� ����� ��������� ����� �˰� �Ǿ����ϴ�. 
	 * ������� 15�� ������ ���� 4������ ǥ�� �� �� �ֽ��ϴ�.
	 * 1 + 2 + 3 + 4 + 5 = 15
	 * 4 + 5 + 6 = 15
	 * 7 + 8 = 15
	 * 15 = 15
	 * �ڿ��� n�� �Ű������� �־��� ��, ���ӵ� �ڿ������ n�� ǥ���ϴ� ����� ���� return�ϴ� solution�� �ϼ����ּ���.
	 * 
	 * (condition(���ѻ���): n�� 10,000 ������ �ڿ��� �Դϴ�.
	 */
	
	//solution:
	public int solution(int n) {
        int answer = 0;
        for(int i=1, j=0, a=0; j<n; i++) {
        	int temp = (n-j)%i;
        	if(temp==0) {
        		answer++;
        	}
        	j+=(1+a);
        	a++;
        }
        return answer;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FibonacciSum cs = new FibonacciSum();
		//example) When given int n= 15, the result gives 4
		System.out.println(cs.solution(15));
	}

}
