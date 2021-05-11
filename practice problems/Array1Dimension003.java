package self.study.array;

import java.util.Scanner;

public class Array1Dimension003{

	/*Problem 3:
	 * A, B 두 사람이 가위바위보 게임을 합니다. 
	 * 총 N번의 게임을 하여 A가 이기면 A를 출력하고, B가 이기면 B를 출력합니다. 
	 * 비길 경우에는 D를 출력합니다.
	 * 가위, 바위, 보의 정보는 1:가위, 2:바위, 3:보로 정하겠습니다.
	 * 두 사람의 각 회의 가위, 바위, 보 정보가 주어지면 각 회를 누가 이겼는지 
	 * 출력하는 프로그램을 작성하세요.
	 */
	
	//my solution
	public String[] solution(int n, int[]A, int[]B) {
		String[] ans = new String[n];
		String result = "D";
		for (int k=0; k<n; k++) {
			if(A[k]==1) {
				if(B[k]==2) result="B";
				else if(B[k]==3) result="A";
				else result="D";
				ans[k]=result;
			}
			else if(A[k]==2) {
				if(B[k]==1) result="A";
				else if(B[k]==3) result="B";
				else result="D";
				ans[k]=result;
			}
			else if(A[k]==3) {
				if(B[k]==1) result="B";
				else if(B[k]==2) result="A";
				else result="D";
				ans[k]=result;
			}
			else
				ans[k]="not valid";
		}
		return ans;
	}
	
	
	//teacher's solution
	//2명이 게임을 하기때문에 기준을 한명으로잡고, 그 한명에 대한 모든 경우를 찾으면
	//게임 결과의 모든 경우를 consider하는것이다.
	public String[] solution1(int n, int[]A, int[]B) {
		String[] ans = new String[n];
		//기준을 A로 잡는다.
		//A가 B와 비기는경우:
		for(int i=0; i<n; i++) {
			if(A[i]==B[i]) ans[i]="D";
			//A가 1(=가위)로 이기는 경우: B가 3(=보)
			else if(A[i]==1 && B[i]==3) ans[i]="A";
			//A가 2(=바위)로 이기는 경우: B가 1(=가위)
			else if(A[i]==2 && B[i]==1) ans[i]="A";
			//A가 3(=보)로 이기는 경우: B가 2(=바위)
			else if(A[i]==3 && B[i]==2) ans[i]="A";
			//A가 지는 경우(B가 이김)
			else ans[i]="B";
		}
		return ans;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Array1Dimension003 h = new Array1Dimension003();
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		
		int[] trialA = new int[n];
		int[] trialB = new int[n];
		for (int i=0; i<n; i++)
			trialA[i]=in.nextInt();
		for (int i=0; i<n; i++)
			trialB[i]=in.nextInt();
		
		String[] answer = h.solution1(n,trialA,trialB);
		for (String x : answer)
			System.out.println(x);
	}

}
