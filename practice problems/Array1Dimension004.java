package self.study.array;

import java.util.ArrayList;
import java.util.Scanner;

public class Array1Dimension004{

	/* Problem 6:
	 * N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 
	 * 그 소수를 출력하는 프로그램을 작성하세요.
	 * 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다. 
	 * 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
	 */
	
	//teacher's solution
	//lesson-learned: breakdown the task into components
	public ArrayList <Integer>  solution1(int n, int[] arr) {
		ArrayList <Integer> answer = new ArrayList<>();
		//숫자 뒤집기
		for(int i=0; i<n; i++) {
			int tmp=arr[i];
			int res=0;
			while(tmp>0) {
				int t=tmp%10;
				res=res*10+t;
				tmp=tmp/10;
			}
			//소수인 숫자만 답 배열에 추가
			if(isPrime(res)) answer.add(res);
		}
		return answer;
	}
	
	public boolean isPrime(int num) {
		if(num==1) return false;
		for (int i=2; i<num; i++) {
			if(num%i==0) return false;
		}
		//위에서 filter되는 과정에서 false로 return되지 않고 여기까지 왔다면,
		//파라미터 num은 1도 아니고, 2이상의 약수도 없기때문에 num은 prime number이다.
		return true;
		//위는 false(소수가아닌)경우만 filter한것이다.
		//num=2의 경우, filter되지 않아서 true값으로 return된다. (2는 소수가 맞기때문에,Ok)
	}
	
	
	//my solution: INCORRECT
	//prime number인지 확인하는 부분 미흡
	public ArrayList <Integer>  solution(int n, int[] nums) {
		ArrayList <Integer> answer = new ArrayList<>();
		int[] nums_rev = new int[n];
		for (int i=0; i<n; i++) {
			StringBuilder y = new StringBuilder(String.valueOf(nums[i]));
			nums_rev[i] = Integer.valueOf(y.reverse().toString());
		}
		//뒤집어진 숫자들 (nums_rev의 숫자들)에서 소수인지 확인해서 선별
		for (int j=0; j<n; j++) {
			if(nums_rev[j]==2) answer.add(nums_rev[j]);
			else {
				int acc =0;
				for(int k=3; k<Math.sqrt(nums_rev[j]); k++) {
					if(nums_rev[j]%k==0) break;
					else {
						acc += nums_rev[j]%k;
					}
				}
				if(acc>0) answer.add(nums_rev[j]);
			}	
		}	
		return answer;

	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Array1Dimension004 r = new Array1Dimension004();
		int n = in.nextInt();
		int[] given = new int[n];
		for (int i=0; i<n; i++) {
			given[i]=in.nextInt();
		}
		for (int c : r.solution1(n, given)) System.out.print(c+" ");
		
	}
}
