package self.study.stackAndQueue;

import java.util.*;

public class StackQueue007{

	/* Problem7:
	 * ������ 1�� ������ ������ȹ�� ¥�� �մϴ�.
	 * �����߿��� �ʼ������� �ֽ��ϴ�. �� �ʼ������� �ݵ�� �̼��ؾ� �ϸ�, �� ������ ������ �ֽ��ϴ�.
	 * ���� �� ������ A, B, C, D, E, F, G�� �ְ�, 
	 * ���⼭ �ʼ������� CBA�� �־����� �ʼ������� C, B, A�����̸� �� ������� �� ������ȹ�� ¥�� �մϴ�.
	 * ���⼭ ������ B������ C������ �̼��� �Ŀ� ���� �ϰ�, 
	 * A������ C�� B�� �̼��� �Ŀ� ���� �Ѵٴ� ���Դϴ�.
	 * ������ C, B, D, A, G, E�� ������ȹ�� ¥�� ����� �� ����������
	 * C, G, E, A, D, B ������ ®�ٸ� �� �� ����� ������ȹ�� �˴ϴ�.
	 * ������ȹ�� �� ������� �տ� ������ �̼��Ǹ� ���� ������ �����ϴٴ� ������ �ؼ��մϴ�.
	 * ������ȹ������ �� ������ ������ �̼��ȴٰ� �����մϴ�.
	 * �ʼ���������� �־����� ������ § N���� �������谡 �ߵ� ���̸� ��YES", 
	 * �߸��� ���̸� ��NO���� ����ϴ� ���α׷��� �ۼ��ϼ���.
	 * 
	 * input: ù �ٿ� �� �ٿ� �ʼ������� ������ �־����ϴ�. ��� ������ ���� �빮���Դϴ�.
	 * �� �� ° �ٺ��� ������ § �������谡 �־����ϴ�.(���������� ���̴� 30�����̴�)
	 * output: ù �ٿ� �������谡 �ߵ� ���̸� ��YES", �߸��� ���̸� ��NO���� ����մϴ�.
	 */
	
	//solution:
	public String solution(String must, String plan){
		String answer="YES";
		Queue<Character> Q = new LinkedList<>();
		for(char x : must.toCharArray()) Q.offer(x);
		for(char x : plan.toCharArray()){
			if(Q.contains(x)){
				if(x!=Q.poll()){
					return "NO";
				} 
			}
		}
		if(!Q.isEmpty()) return "NO";
		return answer;
	}

	public static void main(String[] args){
		StackQueue007 T = new StackQueue007();
		Scanner kb = new Scanner(System.in);
		String a=kb.next();
		String b=kb.next();
		System.out.println(T.solution(a, b));
	}
}
