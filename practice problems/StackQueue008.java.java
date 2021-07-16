package self.study.stackAndQueue;

import java.util.*;

class Patient{
	int id;
	int priority;
	public Patient(int id, int priority){
		this.id=id;
		this.priority=priority;
	}
}

public class StackQueue008{

	/* Problem8:
	 * �޵��� ���� ���޽ǿ��� �ǻ簡 �� ��ۿ� �����ϴ�.
	 * ���޽��� ȯ�ڰ� ������ ������� ���Ḧ �մϴ�. ������ ���赵�� ���� ȯ�ڴ� ���� ������ġ�� �ǻ簡 �ؾ� �մϴ�.
	 * �̷� ������ �����ϱ� ���� ���޽��� ������ ���� ������� ȯ���� ��������� ���մϴ�.
	 * ? ȯ�ڰ� ������ ��������� ��Ͽ��� ���� �տ� �ִ� ȯ�ڸ���� �����ϴ�.
	 * ? ������ ��� ��Ͽ��� ���� ȯ�� ���� ���赵�� ���� ȯ�ڰ� �����ϸ� ����� ���� �ڷ� �ٽ� �ֽ��ϴ�. �׷��� ������ ���Ḧ �޽��ϴ�.
	 * �� ����Ͽ� �ڱ� ���� ���赵�� ���� ȯ�ڰ� ���� �� �ڽ��� ���Ḧ �޴� �����Դϴ�.
	 * ���� N���� ȯ�ڰ� ����Ͽ� �ֽ��ϴ�.
	 * N���� ����� ������ ȯ�� ���赵�� �־�����, ����ϻ��� M��° ȯ�ڴ� �� ��°�� ���Ḧ �޴��� ����ϴ� ���α׷��� �ۼ��ϼ���.
	 * ����ϻ��� M��°�� ������� ���� ó�� ȯ�ڸ� 0��°�� �����Ͽ� ǥ���� ���Դϴ�.
	 * input:
	 * ù �ٿ� �ڿ��� N(5<=N<=100)�� M(0<=M<N) �־����ϴ�.
	 * �� ��° �ٿ� ������ ������� ȯ���� ���赵(50<=���赵<=100)�� �־����ϴ�.
	 * ���赵�� ���� ���� ���� �� �����ϴٴ� ���Դϴ�. ���� ���� ���赵�� ������ �� �ֽ��ϴ�.
	 * output:
	 * M��° ȯ���� �� ��°�� ����޴��� ����ϼ���.
	 */
	
	//solution:
	public int solution(int n, int m, int[] arr){
		int answer=0;
		Queue<Patient> Q = new LinkedList<>();
		for(int i=0; i<n; i++){
			Q.offer(new Patient(i, arr[i]));
		}
		while(!Q.isEmpty()){
			Patient tmp=Q.poll();
			for(Patient x : Q){
				if(x.priority>tmp.priority){
					Q.offer(tmp);
					tmp=null;
					break;
				}
			}
			if(tmp!=null){
				answer++;
				if(tmp.id==m) return answer;
			}
		}
		return answer;
	}

	public static void main(String[] args) throws IOException{
		StackQueue008 T = new StackQueue008();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int m=kb.nextInt();
		int[] arr = new int[n];
		for(int i=0; i<n; i++){
			arr[i]=kb.nextInt();
		}
		System.out.println(T.solution(n, m, arr));	
	}
}
