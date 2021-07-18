package self.study.sortAndSearch;

import java.util.*;

public class SortSearch001{

	/* Problem1:
	 * N���� ���ڰ� �ԷµǸ� ������������ �����Ͽ� ����ϴ� ���α׷��� �ۼ��ϼ���.
 	 * �����ϴ� ����� ���������Դϴ�.
	 * input: 
	 * ù ��° �ٿ� �ڿ��� N(1<=N<=100)�� �־����ϴ�.
	 * �� ��° �ٿ� N���� �ڿ����� ������ ���̿� �ΰ� �Էµ˴ϴ�. 
	 * �� �ڿ����� ������ ���� �ȿ� �ֽ��ϴ�.
	 */
	
	//solution:
	public int[] solution(int n, int[] arr){
		for(int i=0; i<n-1; i++){
			int idx=i;
			for(int j=i+1; j<n; j++){
				if(arr[j]<arr[idx]) idx=j;
			}
			int tmp=arr[i];
			arr[i]=arr[idx];
			arr[idx]=tmp;
		}
		return arr;
	}

	public static void main(String[] args){
		SortSearch001 T = new SortSearch001();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int[] arr=new int[n];
		for(int i=0; i<n; i++) arr[i]=kb.nextInt();
		for(int x : T.solution(n, arr)) System.out.print(x+" ");
	}
}
