package practicetest;

import java.util.Arrays;
import java.util.Collections;

public class ConditionLoop005{

	/*
	 * Problem:
	 * 생각 경시 대회를 축하하기 위해서 전통적으로 초에 불을 붙인다. 
	 * 대회 첫째날밤에는 하나의 초에 불을 붙인다. 저녁이 끝나면 불을 끈다. 
	 * 다음날마다 전날보다 불을 붙이는 초의 개수를 하나씩 늘려서 (1을 기준으로) 
	 * n번째날 밤에는 n개의 초에 불을 붙인다 (아침에는 모든 초의 불을 끈다). 
	 * 매일밤 불을 붙일때마다 초의 높이는 1씩 줄어든다. 높이가 0이 되면 더 이상 사용할 수 없다.
	 * 주어진  int[] candles의 i번째 요소는 i번째 양초의 높이는 나타낸다. 
	 * 새로운 양초를 구입하지 않고 최대 며칠밤을 축하할 수 있는지 구하여라. 
	 * 예시) 높이 2의 초 3개를 가지고 있다면, 첫째날 초 하나를 밝히고, 
	 * 나머지 두개를 둘째날 밝히고, 셋째날에 모든 초를 밝혀 3일동안 축하할 수 있다.
	 *
	 */
	
	public int solution(int[] candles) {
		int answer = 0;
		int day =0;
		//int[]candles를 desc order로 sort하기(더 빠른 방법은 없나 찾아봐야함):
		Integer[] cand = new Integer[candles.length];
		int i=0;
		for (int c:candles) {
			cand[i]=c;
			i++;
		}
		Arrays.sort(cand, Collections.reverseOrder());
		
		//desc order sort된 candles 배열에서 가장 앞 초부터(가장 긴 초부터) 태우기 시작
		for (int n=0; n<cand.length; n++) {
			//처음 시작에는 day=0. 
			//day=0에 0번째  초  태우기 --> day=1에 0번째와 1번째 초 태우기
			//	--> day2에 0번쩨,1번째,2번째 초 태우기...so on
			for (int m=0; m<n+1; m++) {
				//초 길이가 0에 도달하면 그때의 day 값을 answer로 지정한다.
				if (cand[m]==0) answer=day;
				cand[m]-=1;
			}
			//그 day에 해당하는 초를 다 태운 후, 다음날로 이동
			day++;
		}
		answer = day;
		return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ConditionLoop005 p5 = new ConditionLoop005();
		int[] candles = {4,5,2};
		System.out.println(p5.solution(candles));
	}

}
