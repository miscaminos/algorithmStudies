package test;
/*
 * Dynamic Programming example problem 
 */
public class DynamicProgramming {
	
	int MOD = 20170805;
	public int solution(int m, int n, int[][] cityMap) {
		int[][] goRight = new int[m+1][n+1];
		int[][] goDown = new int[m+1][n+1];
		goRight[1][1] = 1;
		goDown[1][1] = 1;
		
		for(int i=1; i<=m; i++) {
			for(int j=1; j<=n; j++) {
				if(cityMap[i-1][j-1] == 0) {
					goRight[i][j] +=(goRight[i-1][j] + goDown[i][j-1]) %MOD;
					goDown[i][j] +=(goRight[i-1][j] + goDown[i][j-1]) %MOD;
				}else if(cityMap[i-1][j-1] == 1) {
					goRight[i][j] =0;
					goDown[i][j] =0;
				}else {
					goRight[i][j] = goRight[i-1][j];
					goDown[i][j] = goDown[i][j-1];
				}
			}
		}
		return (goRight[m-1][n] + goDown[m][n-1])%MOD;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DynamicProgramming s1 = new DynamicProgramming();
		int [][] cityMap = {{0, 2, 0, 0, 0, 2}, {0, 0, 2, 0, 1, 0}, {1, 0, 0, 2, 2, 0}};
		int ans = s1.solution(3,6,cityMap);
		System.out.println(ans);
		
		int[][] cityMap2 = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
		int ans2 = s1.solution(3, 3, cityMap2);
		System.out.println(ans2);
		
	}

}
