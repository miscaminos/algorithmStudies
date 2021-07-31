package self.study.sortAndSearch;

import java.util.*;

public class SortSearch002{
	
	 // problem2:
	 // N개이 숫자가 입력되면 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요.
	 // 정렬하는 방법은 버블정렬입니다.
	 // input:첫 번째 줄에 자연수 N(1<=N<=100)이 주어집니다.
	 // 두 번째 줄에 N개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 정수형 범위 안에 있습니다.
	 // output: 오름차순으로 정렬된 수열을 출력합니다.

	//solution:
	public int[] solution(int n, int[] arr){
		for(int i=0; i<n-1; i++){
			for(int j=0; j<n-i-1; j++){
				if(arr[j]>arr[j+1]){
					int tmp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=tmp;
				}
			}	
		}
		return arr;
	}

	public static void main(String[] args){
		SortSearch002 T = new SortSearch002();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int[] arr=new int[n];
		for(int i=0; i<n; i++) arr[i]=kb.nextInt();
		for(int x : T.solution(n, arr)) System.out.print(x+" ");
	}
}