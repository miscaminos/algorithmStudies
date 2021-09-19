package self.study.recursiveTreeGraph;

import java.util.*;

public class recursiveTreeGraph002{
	
	//use recursive function to print binary number
	public void DFS(int n){
		if(n==0) return;
		else{
			DFS(n/2);
			System.out.print(n%2);
		}
	}

	public void solution(int n){
		DFS(n);
	}
	public static void main(String[] args){
		recursiveTreeGraph002 T = new recursiveTreeGraph002();
		T.solution(11);
	}

}