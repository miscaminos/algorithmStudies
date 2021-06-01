package self.study.twopointers;

import java.util.*

public class TwoPointer002{

	/* Problem 2: 
	 * A, B 두 개의 집합이 주어지면 두 집합의 공통 원소를 추출하여 오름차순으로 출력하는 프로그램을 작성하세요.
	 * 입력조건: 첫 번째 줄에 집합 A의 크기 N(1<=N<=30,000)이 주어집니다.
	 * 두 번째 줄에 N개의 원소가 주어집니다. 원소가 중복되어 주어지지 않습니다.
	 * 세 번째 줄에 집합 B의 크기 M(1<=M<=30,000)이 주어집니다.
	 * 네 번째 줄에 M개의 원소가 주어집니다. 원소가 중복되어 주어지지 않습니다.
	 * 각 집합의 원소는 1,000,000,000이하의 자연수입니다.
	 */
	
	//solution:
	public ArrayList <Integer> solution(int n, int m, int[] a, int[] b){
		ArrayList <Integer> ans = new ArrayList<>();
		Arrays.sort(a);
		Arrays.sort(b);
		int x =0;
		int y =0;
		while(x<n && y<m) {
			if(a[x] == b[y]) {
				ans.add(a[x]);
				x++;
				y++;
			}
			else if(a[x]<b[y]) x++;
			else y++;
		}
		return ans;
	}
	
	public static void main(String[] args) {
		TwoPointer002 T = new TwoPointer002();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int[] a=new int[n];
		for(int i=0; i<n; i++){
			a[i]=kb.nextInt();
		}
		int m=kb.nextInt();
		int[] b=new int[m];
		for(int i=0; i<m; i++){
			b[i]=kb.nextInt();
		}
		for(int x : T.solution(n, m, a, b)) System.out.print(x+" ");
	}

}
