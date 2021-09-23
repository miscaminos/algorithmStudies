package self.study.recursiveTreeGraph;

import java.util.*;

public class RecursiveTreeGraph002{
	
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
		RecursiveTreeGraph002 T = new RecursiveTreeGraph002();
		T.solution(11);
	}

}