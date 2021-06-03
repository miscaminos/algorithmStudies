package self.study.twopointers;

import java.util.Scanner;

public class TwoPointer004{

	/* Problem4:
	 * N개의 수로 이루어진 수열이 주어집니다.
	 * 이 수열에서 연속부분수열의 합이 특정숫자 M이 되는 경우가 몇 번 있는지 구하는 프로그램을 작성하세요.
	 * 만약 N=8, M=6이고 수열이 다음과 같다면
	 * 1 2 1 3 1 1 1 2
	 * 합이 6이 되는 연속부분수열은 {2, 1, 3}, {1, 3, 1, 1}, {3, 1, 1, 1}로 총 3가지입니다.
	 * 입력 방식: 첫째 줄에 N(1≤N≤100,000), M(1≤M≤100,000,000)이 주어진다.
	 * 
	 */
	
	//solution - correct
	public int solution (int n, int m, int[] arr) {
		int count=0, sum=0, lt=0;
		for(int rt=0; rt<n; rt++) {
			sum += arr[rt];
			if(sum==m) count++;
			while(sum>=m) {
				sum-=arr[lt];
				lt++;
				if(sum==m) count++;
			}
		}
		return count;
	}
	
	public static void main(String[] args){
		TwoPointer004 T = new TwoPointer004();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int m=kb.nextInt();
		int[] arr=new int[n];
		for(int i=0; i<n; i++){
			arr[i]=kb.nextInt();
		}
		System.out.print(T.solution(n, m, arr));
	}

}
