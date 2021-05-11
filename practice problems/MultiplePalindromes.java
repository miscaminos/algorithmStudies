package self.study.string;

import java.util.ArrayList;

public class MultiplePalindromes {

	/*
	 * Problem8:
	 * 앞에서 읽을 때나 뒤에서 읽을 때나 같은 문자열을 팰린드롬이라고 합니다.
	 * 문자열이 입력되면 해당 문자열이 팰린드롬이면 "YES", 
	 * 아니면 “NO"를 출력하는 프로그램을 작성하세요.
	 * 단 회문을 검사할 때 알파벳만 가지고 회문을 검사하며, 대소문자를 구분하지 않습니다.
	 */
	
	//my solution: INCORRECT
	public String solution(String str) {
		String answer="NO";
		ArrayList <Character> alphs = new ArrayList<>();
		for (char g : str.toCharArray()) {
			if(Character.isAlphabetic(g)) {
				g = Character.toLowerCase(g);
				alphs.add(g);
			}
		}
		String s1="";
		for (char a : alphs)
			s1 += String.valueOf(a);
		System.out.println("s1:"+s1);
		String s2 = new StringBuilder(s1).reverse().toString();
		System.out.println("s2:"+s2);
		if(s1.equals(s2))
			answer="YES";
		return answer;
	}
	
	//강사님 solution:
	// ^ :XOR연산자를 사용한다.
	// a^b의 결과는 a와b가 같으면 0(false), a와b가 다르면 1(true)이다.
	//현 문제에서는 str의 문자들이 (a-z사이의)alphabet과 다른경우가 true여서 
	//replace 메소드를 진행하길 원하기때문에 아래와 같이 작성한다.
	public String solution1(String str) {
		String answer="NO";
		str = str.toLowerCase().replaceAll("[^a-z]","");
		//또는: str = str.toUpperCase().replaceAll("[^A-Z]","");
		//확인: System.out.println(str);
		String tmp = new StringBuilder(str).reverse().toString();
		if(tmp.equals(str)) answer="YES";
		return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MultiplePalindromes mp = new MultiplePalindromes();
		String str = "found7, time: study; Yduts; emit, 7Dnuof";
		System.out.println(mp.solution1(str));
	}

}
