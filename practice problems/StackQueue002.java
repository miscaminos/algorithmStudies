package self.study.stackAndQueue;

import java.util.*;

public class StackQueue002{

	/* Problem2:
	 * �Էµ� ���ڿ����� �Ұ�ȣ ( ) ���̿� �����ϴ� ��� ���ڸ� �����ϰ� ���� ���ڸ� ����ϴ� ���α׷��� �ۼ��ϼ���.
	 * input: ù �ٿ� ���ڿ��� �־�����. ���ڿ��� ���̴� 100�� ���� �ʴ´�.
 	 * output: ���� ���ڸ� ����Ѵ�.
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
