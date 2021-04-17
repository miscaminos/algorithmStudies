package practicetest;

import java.util.ArrayList;
import java.util.Arrays;

public class ConditionLoop004{

	
	/*
	 * Problem: 
	 * 스미드 교수는 논리 수업을 가르친다. 어느 날 그는 다음과 같은 문장을 칠판에 썼다.
	 * 이 문장들 중 정확히 a개의 문장이 참이다.이 문장들 중 정확히 b개의 문장이 참이다.
	 * 이 문장들 중 정확히 c개의 문장이 참이다.
	 * a, b, c 등은 각각 숫자이다. 그리고 그는 학생들에게 이 중 몇개의 문장이 참인지 물어보았다.
	 * 주어진 정수 배열 int[] statements에 Smith 교수가 쓴 숫자들이 적혀있다. 
	 * 모두 몇 개의 문장이 참인지 리턴하시오.
	 * 만약 가능한 답이 두개 이상이라면 그 중 더 큰 숫자를 반환하여라. 가능한 답이 없다면 –1을 리턴하시오.
	 * 
	 */
	public int solution(int[] statements) {
		int answer = 0;
		ArrayList <Integer> count = new ArrayList<>();
		//int cnt = 0;
		if (statements.length == 1 && statements[0] == 0) {
			answer =-1;
		}
		else {
			Arrays.sort(statements);
			int m1 = statements[statements.length-1];
			System.out.println("m1:"+m1);
			for(int i=0; i<=m1; i++) {
				int cnt=0;
				for (int s:statements) {
					if(i==s) cnt++;
				}
				System.out.println("cnt:"+cnt);
				count.add(cnt);	
			}
			
			System.out.println("count arraylist:");
			for (int c:count) System.out.println(c);
			
			int m2 = -1;
			for(int i=0; i<=m1; i++) {
				for (int c:count) {
					if(i==c)  m2=i;
				}
			}			
			if(m2==-1 && count.get(0)==0) answer=0;
			else if (m2==-1 && count.get(0)>0) answer=-1;
			else answer = m2;
		}
		return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ConditionLoop004 p4 = new ConditionLoop004();
		int[] statements = {2,9,2,3,4};
		System.out.print(p4.solution(statements));
	}

}
