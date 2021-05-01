package self.study.array;

public class Array1Dimension001{

	/*
	 * Problem2:
	 * 선생님이 N명의 학생을 일렬로 세웠습니다. 
	 * 일렬로 서 있는 학생의 키가 앞에서부터 순서대로 주어질 때, 맨 앞에 서 있는
	 * 선생님이 볼 수 있는 학생의 수를 구하는 프로그램을 작성하세요. 
	 * (앞에 서 있는 사람들보다 크면 보이고, 작거나 같으면 보이지 않습니다.)
	 * input: 첫 줄에 정수 N(5<=N<=100,000)이 입력된다. 
	 * 그 다음줄에 N명의 학생의 키가 앞에서부터 순서대로 주어진다.
	 */
	
	//my solution: CORRECT
	public int solution(int n, int[] numbers) {
		//맨 앞사람은 항상 보인다
		int answer = 1;
		//i번째의 앞에 있는 사람들중 가장 큰사람이 tmp. i번째는 tmp보다 커야지 보인다.
		int tmp = numbers[0];
		for(int i=1; i<numbers.length; i++) {
			//아래 해당조건에서만 tmp를 갱신
			if(numbers[i]>tmp) {
				answer++;
				tmp=numbers[i];	
			}	
		}
		return answer;
	}
	
	//강사님 solution:
	public int solution1(int n, int[] arr){
		int answer=1, max=arr[0];
		for(int i=1; i<n; i++){
			if(arr[i]>max){
				max=arr[i];
				answer++;
			}
		}
		return answer;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		VisibleTallerKids vk = new VisibleTallerKids();
		int [] numbers= {130, 135, 148, 140, 145, 150, 150, 153};
		int n = 8;
		System.out.println(vk.solution(n, numbers));

	}

}
