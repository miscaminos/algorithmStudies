package practicetest;

public class ConditionLoop3{

	/*
	 * 윤호는 64 cm 길이의 막대를 가지고 있지만 x cm만큼 긴 막대가 있다면 더 재밌을 것이라 생각한다. 
	 * 그는 원래 막대를 작은 막대 여러개로 부수고 풀로 붙여서 정확히 x cm만큼 긴 막대를 만들기로 결심했다.
	 * 막대를 부수는 가장 쉬운 방법은 반으로 쪼개는 것이라서 윤호는 다음의 방법을 따르기로 했다:
	 * 모든 막대들의 길이를 더한다 (처음에는 64 cm 길이의 막대 하나만 있었다). 
	 * 길이의 합이 x보다 크다면 다음을 반복한다:
	 * 가장 짧은 길이의 막대를 반으로 부순다.
	 * 만약 두개 중 하나를 버려도 남아있는 막대들의 길이의 합이 x보다 크다면 하나를 버린다.
	 * 마지막으로 남아있는 막대들을 풀로 붙여 x cm길이의 막대를 만든다.
	 * 윤호가 위의 단계를 따라하여 풀로 붙이게 될 마지막에 남은 막대들의 개수를 반환하여라. 
	 * 만약 마지막 단계에서 막대가 하나밖에 없다면 1을 반환하라
	 * 
	 */
	
	public int solution(int x) {
		int answer = 0;
		//막대를 반으로 잘라서 나올 수 있는 막대길이의 리스트 (sort descending order)
		int[] sticks = {64, 32, 16, 8, 4, 2, 1};
		boolean flag = true;
		//원하는 길이(x)보다 작거나 같은 길이 중, 가장 큰 수를 뺀다. 
		//sticks 배열이 이미 desc순서이기때문에 i로 traverse하며 찾는다. 뺀 횟수를 count한 값을 answer로 반환
		while(flag) {
			if (x==0) return answer;
			for (int i=0; i<sticks.length; i++) {
				if(sticks[i]<=x) {
					x -= sticks[i];
					answer +=1;
				}
			}
		}
		return answer;
	}
	
	public static void main(String[] args) {
		ConditionLoop3 p3 = new ConditionLoop3();
		System.out.println(p3.solution(33));	
	}
}
