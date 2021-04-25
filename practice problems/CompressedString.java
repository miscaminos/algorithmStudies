package self.study.string;

public class CompressedString {
	
	/*
	 * Problem11:
	 * 알파벳 대문자로 이루어진 문자열을 입력받아 같은 문자가 연속으로 반복되는 경우 반복되는
	 * 문자 바로 오른쪽에 반복 횟수를 표기하는 방법으로 문자열을 압축하는 프로그램을 작성하시오.
	 * 단 반복횟수가 1인 경우 생략합니다 
	 */
	
	//my solution: INCORRECT...missing the last character!
	public String solution1(String str) {
		String ans = "";
		int m = 1;
		for(int i=1; i<str.length(); i++) {
			if(str.charAt(i-1)==str.charAt(i)) {
				m++;
				if(i==str.length()-1) {
					ans+=str.charAt(i)+String.valueOf(m);
				}	
			}
			else {
				if(m>1) {
					ans+=str.charAt(i-1)+String.valueOf(m);
					m=1;
				}
				else ans+=str.charAt(i-1);
			}
		}
		return ans;
	}
	
	//my solution: CORRECT
	public String solution2(String str) {
		String ans = "";
		String str_ext=str+" ";
		int m = 1;
		for(int i=0; i<str.length(); i++) {
			if(str_ext.charAt(i)==str_ext.charAt(i+1)) {
				m++;
			}
			else {
				if(m>1) {
					ans+=str.charAt(i)+String.valueOf(m);
					m=1;
				}
				else ans+=str.charAt(i);
			}
		}
		return ans;
	}
	
	//강사님 solution: String문자열을 새로 생성하지않고 인자값으로 받은 그대로에
	//맨뒤 blank space하나만 더해서 탐색+답을 구한다. 
	public String solution(String str) {
		String ans = "";
		str+=" ";
		int cnt=1;
		for(int i=0; i<str.length()-1; i++) {
			if(str.charAt(i)==str.charAt(i+1)) cnt++;
			else {
				ans += str.charAt(i);
				if(cnt>1) ans += String.valueOf(cnt);
				cnt=1;
			}
		}
		
		return ans;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CompressedString cs = new CompressedString();
		String str = "KKHSSSSSSSE";
		System.out.println(cs.solution2(str));
		String str1 = "KSTTTSEEKFKKKDJJGG";
		System.out.println(cs.solution2(str1));
	}

}
