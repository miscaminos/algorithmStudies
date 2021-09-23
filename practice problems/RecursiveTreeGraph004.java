package self.study.recursiveTreeGraph;

import java.util.*;

public class RecursiveTreeGraph004{
	
	//use recursive to create Fibonacci pattern
	public int DFS(int n){
		if(n==1) return 1;
		else if(n==2) return 1;
		else return DFS(n-2)+DFS(n-1);
	}
	public static void main(String[] args){
		RecursiveTreeGraph004 T = new RecursiveTreeGraph004();
		int n=10;
		for(int i=1; i<=n; i++) System.out.print(T.DFS(i)+" ");
	}	

}