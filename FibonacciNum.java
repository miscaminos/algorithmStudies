package Fibonacci;

public class FibonacciNum {

	
	/* problem:
	 * �Ǻ���ġ ���� F(0) = 0, F(1) = 1�� ��, 
	 * 1 �̻��� n�� ���Ͽ� F(n) = F(n-1) + F(n-2) �� ����Ǵ� �� �Դϴ�.
	 * �������
	 * F(2) = F(0) + F(1) = 0 + 1 = 1
	 * F(3) = F(1) + F(2) = 1 + 1 = 2
	 * F(4) = F(2) + F(3) = 1 + 2 = 3
	 * F(5) = F(3) + F(4) = 2 + 3 = 5
	 * �� ���� �̾����ϴ�.
	 * 
	 * 2 �̻��� n�� �ԷµǾ��� ��, n��° �Ǻ���ġ ���� 1234567���� ���� �������� �����ϴ� �Լ�, 
	 * solution�� �ϼ��� �ּ���.
	 * ���� ����: n�� 1�̻�, 100000������ �ڿ����Դϴ�.
	 */
	
	//solution:
    public int solution(int n) {
        int answer = 0;
        int a=1;
        int b=1;

        for(int i=3;i<=n;i++){
            answer=(a+b)%1234567;
            a=b;
            b=answer;
        }
        return answer;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FibonacciNum fn = new FibonacciNum();
		System.out.println(fn.solution(5));
	}

}
