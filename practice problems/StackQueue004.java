package self.study.stackAndQueue;

import java.util.*;

public class StackQueue004{

	/* Problem4:
	 * ����������� �־����� ������ ����� ����ϴ� ���α׷��� �ۼ��ϼ���.
	 * ���� 3*(5+2)-9 �� ������������� ǥ���ϸ� 352+*9- �� ǥ���Ǹ� �� ����� 12�Դϴ�.
	 * input: ù �ٿ� ����������� �־����ϴ�. ������� ���̴� 50�� ���� �ʽ��ϴ�.
	 * ���� 1~9�� ���ڿ� +, -, *, / �����ڷθ� �̷������.
	 * output: ������ ����� ����մϴ�.
	 */
	
	//solution:
	public int solution(String str){
		int answer=0;
		Stack<Integer> stack = new Stack<>();
		for(char x : str.toCharArray()){
			if(Character.isDigit(x)){
				stack.push(x-48);
			}
			else{
				int rt=stack.pop();
				int lt=stack.pop();
				if(x=='+') stack.push(lt+rt);
				else if(x=='-') stack.push(lt-rt);
				else if(x=='*') stack.push(lt*rt);
				else if(x=='/') stack.push(lt/rt);
			}
		}
		answer=stack.get(0);
		return answer;
	}
	public static void main(String[] args){
		StackQueue004 T = new StackQueue004();
		Scanner kb = new Scanner(System.in);
		String str=kb.next();
		System.out.println(T.solution(str));
	}
}
