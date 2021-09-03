package self.study.sortAndSearch;

import java.util.*;

public class Point implements Comparable<Point>{

	public int x, y;

	Point(int x, int y){
		this.x = x;
		this.y = y;
	}

	@Override
	public int compareTo(Point pt){
		result = 0;
		if(this.x==pt.x) {
			result = this.y-pt.y;
		}
		else{
			result = this.x-pt.x; 
		} 
		return result;
	}
}

public class SortSearch007{
	
	public static void main(String[] args){
		Scanner sc= new Scanner(System.in);
		int n = sc.nextInt();

		ArrayList<Point> arr=new ArrayList<>();
		for(int i=0; i<n; i++){
			int x = sc.nextInt();
			int y = sc.nextInt();
			arr.add(new Point(x, y));
		}
		Collections.sort(arr);
		for(Point pt : arr) {
			System.out.println(pt.x+" "+pt.y);	
		}
	}
}