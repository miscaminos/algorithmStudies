package self.study.recursiveTreeGraph;

import java.util.*;

public class recursiveTreeGraph001{
	
	public void DFS(int n){
		if(n==0) return;
		else{
			DFS(n-1);
			System.out.print(n+" ");
		}
	}

	public void solution(int n){
		DFS(n);
	}
	public static void main(String[] args){
		recursiveTreeGraph001 T = new recursiveTreeGraph001();
		T.solution(3);
		//System.out.println(T.solution(3));
	}

}