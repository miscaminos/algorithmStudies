package self.study.twopointers;

import java.util.Scanner;

public class TwoPointer005{

	/* Problem5:
	 * N입력으로 양의 정수 N이 입력되면 2개 이상의 연속된 자연수의 합으로 정수 N을 표현하는 
	 * 방법의 가짓수를 출력하는 프로그램을 작성하세요. 만약 N=15이면
	 * 7+8=15
	 * 4+5+6=15
	 * 1+2+3+4+5=15
	 * 와 같이 총 3가지의 경우가 존재함
	 */
	
	//solution - correct
	public int solution(int n){
		int answer=0, sum=0;
		int m=n/2+1;
		int[] arr=new int[m];
		for(int i=0; i<m; i++) arr[i]=i+1;
		int lt=0;
		for(int rt=0; rt<m; rt++){
			sum+=arr[rt];
			if(sum==n) answer++;
			while(sum>=n){
				sum-=arr[lt++];
				if(sum==n) answer++; 
			}
		}
		return answer;
	}

	public static void main(String[] args){
		TwoPointer005 T = new TwoPointer005();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		System.out.print(T.solution(n));
	}
}
