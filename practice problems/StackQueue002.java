package self.study.stackAndQueue;

import java.util.*;

public class StackQueue002{

	/* Problem2:
	 * 입력된 문자열에서 소괄호 ( ) 사이에 존재하는 모든 문자를 제거하고 남은 문자만 출력하는 프로그램을 작성하세요.
	 * input: 첫 줄에 문자열이 주어진다. 문자열의 길이는 100을 넘지 않는다.
 	 * output: 남은 문자만 출력한다.
	 */
	
	//solution:
	public String solution(String str){
		String answer="";
		Stack<Character> stack=new Stack<>();
		for(char x : str.toCharArray()){
			if(x==')'){
				while(stack.pop()!='(');
			}
			else stack.push(x);
		}
		for(int i=0; i<stack.size(); i++) answer+=stack.get(i);
		return answer;
	}

	public static void main(String[] args){
		StackQueue002 T = new StackQueue002();
		Scanner kb = new Scanner(System.in);
		String str=kb.next();
		System.out.println(T.solution(str));
	}
}
