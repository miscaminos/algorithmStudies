package self.study.array;

import java.util.Scanner;

public class Array1Dimension002{

	/* Problem5:
	 * 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
	 * 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
	 * 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
	 */
	
	//solution1: incorrect
	//파라미터 N이(2<=N<=200,000)범위내에서 아주 큰 숫자가 될수도있기때문에 
	//for loop을 두겹사용하면 time limit을 못지키는 문제 발생한다.
	//더 가벼운 방법 찾아봐야함.
	public int solution(int n) {
		int answer =0;
		boolean[] numbers = new boolean[n-1];
		for (int i=2; i<n+1; i++) {
			numbers[i]=true;
			for (int j=2; j<n+1; j++) {
				//index=i일때 j로 배열 전체를  확인...?
			}
		}
		return answer;
	}
	
	
	//solution2: correct 
	//n=20이라면,
	//(0,1은 제외하고, 소수가 아니니까!)
	//{2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
	//이 배열에 각각 일단 소수라는 true값을 넣어놓고 순서대로 하나씩 체크한다:
	//2자체는 소수가 맞으니, 소수 count+1. 그리고 배열의 숫자들을 차례대로 2의 배수인것들을 false처리.
	//다음, 3자체는 소수가 맞으니, count+1. 그리고 배열의 숫자를 차례대로 3의 배수인것들을 false처리.
	//다음, 4는 이미 2의 배수로서,false로 처리되었었기때문에, 소수가 아님.
	//다음, 5자체는 소수가 맞으니, count+1. 그리고 배열의 숫자들을 차례대로 5의 배수인것들을 false처리.
	//이렇게 배열의 끝까지 traverse하며 prime(소수)의 count값을 구한다.
	public int solution1(int n) {
		int count =0;
		int[] numbers = new int[n+1];
		for(int i=2; i<=n; i++) {
			//빈 정수 배열을 만들면, default값 0가 들어가있다.
			//즉, 0이라면 아직 손대지않은 배열 원소 또는 소수값의 원소라는 뜻임.
			if(numbers[i]==0) {
				count++;
				//j가 i의 배수인 경우만 찾는것이기때문에, j가 i씩 증가한다.
				for (int j=i; j<=n; j=j+i) {
					numbers[j]=1;
				}
			}
		}
		return count;
	}
	
	public static void main(String[] args) {
	    Array1Dimension002    ep = new Array1Dimension002();
	    Scanner in=new Scanner(System.in);
	    int n = in.nextInt(); 
	    System.out.println(ep.solution1(n));
	}

}
