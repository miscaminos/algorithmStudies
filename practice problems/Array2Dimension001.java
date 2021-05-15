package self.study.array;

import java.util.Scanner;

public class Array2Dimension001{

	/*
	 * Problem 9:
	 * 5*5 격자판에 아래롸 같이 숫자가 적혀있습니다
	 * N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.
	 * 첫 줄에 자연수 N이 주어진다.(2<=N<=50) 
	 * 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.
	 */
	
	//my solution:
	//Utilize Math class의 max method for better coding(much more concise)
	public int solution(int n, int[][] arr) {
		int ans =0;
		int r=0, c=0;
		for (int i=0; i<n; i++) {
			r=0;
			c=0;
			for (int j=0; j<n; j++) {
				r+=arr[i][j];
				c+=arr[j][i];
			}
			if(r>ans && r>c) {
				ans=r;
			}
			else if(c>ans && c>r) {
				ans=c;
			}
			else {
				continue;
			}
		}
		int d1=0;
		int d2=0;
		for (int i=0; i<n; i++) {
			d1+=arr[i][i];
			d2+=arr[i][n-i-1];
		}
		if(d1>ans && d1>d2) {
			ans=d1;
		}
		else if(d2>ans && d2>d1) {
			ans=d2;
		}
		else {
			ans=ans;
		}
		return ans;
	}
	
	
	//teacher's solution:
	public int solution1(int n, int[][] arr){
		int answer=-2147000000;
		int sum1=0, sum2=0;
		for(int i=0; i<n; i++){
			sum1=sum2=0;
			for(int j=0; j<n; j++){
				sum1+=arr[i][j];
				sum2+=arr[j][i];
			}
			answer=Math.max(answer, sum1);
			answer=Math.max(answer, sum2);
		}
		sum1=sum2=0;
		for(int i=0; i<n; i++){
			sum1+=arr[i][i];
			sum2+=arr[i][n-i-1];
		}
		answer=Math.max(answer, sum1);
		answer=Math.max(answer, sum2);
		return answer;
	}
	
	
	public static void main(String[] args) {
		Array2Dimension001 ss = new Array2Dimension001();
		Scanner in = new Scanner(System.in);
	
		int n = in.nextInt();
		int[][] given = new int[n][n];
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				given[i][j]=in.nextInt();
			}
		}
		
//		int n = 5;
//		int[][] given = {{10,13,10,12,15},{12,39,30,23,11},
//				{11,25,50,53,15},{19,27,29,37,27},{19,13,20,13,19}};

		System.out.println(ss.solution(n, given));

	}

}
