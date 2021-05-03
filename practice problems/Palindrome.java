package self.study.string;

public class Palindrome {
	
	/*
	 * Problem7: 회문 문자열
	 * 앞에서 읽을 때나 뒤에서 읽을 때나 같은 문자열을 회문 문자열이라고 합니다.
	 * 문자열이 입력되면 해당 문자열이 회문 문자열이면 "YES", 
	 * 회문 문자열이 아니면 “NO"를 출력하는 프로그램을 작성하세요.
	 * 단 회문을 검사할 때 대소문자를 구분하지 않습니다.
	 */
	
	//my solution: CORRECT but 시험해볼 문자열의 길이를 홀/짝수 구분할 필요가없다!
	public String solution(String str) {
		String ans ="";
		str = str.toLowerCase();
		char [] cut = new char[str.length()/2];
		int limit = 0;
		int k = 0;
		if(str.length()%2==0) {
			//when str.length=6, (6/2-1)=2 ==> i=5,4,3
			limit = (str.length()/2)-1; 
		}
		else {
			//when str.length=7, (7/2)=3 ==> i=6,5,4
			limit = str.length()/2; 
		}
		for (int i=str.length()-1; i>limit; i--) {
			cut[k]=str.charAt(i);
			k++;
		}
		String str2 = String.valueOf(cut);
		if(str.substring(0, str.length()/2).equals(str2))
			ans="YES";
		else
			ans="NO";
		return ans;
	}
	
	//강사님 solution1:
	public String solution1(String str) {
		String answer ="YES";
		str = str.toLowerCase();
		int len = str.length();
		for(int i=0; i<len/2; i++) {
			if(str.charAt(i) != str.charAt(len-i))
				return"NO";
		}
		return answer;
	}
	
	//강사님 solution2:
	public String solution2(String str) {
		String answer="NO";
		String tmp = new StringBuilder(str).reverse().toString();
		if(str.equalsIgnoreCase(tmp))
			answer = "YES";
		return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Palindrome p = new Palindrome();
		String str = "abCbbcbA";
		System.out.println(p.solution2(str));
	}

}
