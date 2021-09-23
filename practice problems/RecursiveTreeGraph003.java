package self.study.recursiveTreeGraph;

import java.util.*;

public class RecursiveTreeGraph003{
	
	//use recursive function to print binary factorial
	public int DFS(int n){
		if(n==1) return 1;
		else return n*DFS(n-1);
	}
	public static void main(String[] args){
		RecursiveTreeGraph003 T = new RecursiveTreeGraph003();
		System.out.println(T.DFS(5));
	}	

}