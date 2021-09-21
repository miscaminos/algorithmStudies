package self.study.recursiveTreeGraph;

import java.util.*;

public class recursiveTreeGraph003{
	
	//use recursive function to print binary factorial
	public int DFS(int n){
		if(n==1) return 1;
		else return n*DFS(n-1);
	}
	public static void main(String[] args){
		recursiveTreeGraph003 T = new recursiveTreeGraph003();
		System.out.println(T.DFS(5));
	}	

}