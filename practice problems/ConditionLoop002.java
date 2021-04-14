package practicetest;


public class ConditionLoop002 {

	/*
	 * Problem: 세 자매가 해외여행 중 기념품 가게에 왔습니다.
	 * 이 기념품 가게에서는 한번에 50달러 이상 지출하면, 10달러를 할인해주는 행사를 하고 있습니다.
	 * 그녀들은 구매한 물건을 합하여 계산하면, 각자 따로 지불하는 것보다 적게 지불할 수 있다는 것을 깨달았습니다.
	 * 예를들어 그들이 각각 46달러, 62달러, 9달러만큼의 상품을 구입하는 경우, 
	 * 46달러와 9달러를 합치는 것으로 2번의 구매를 할 수 있습니다.
	 * 이렇게 하면 55달러와 62달러로 거래하게 되어 총 20달러의 할인을 받을 수 있습니다.
	 * 여기 int[] goods가 주어집니다.int[] goods의 각 요소는 한 명이 구매하려는 물품의 총 비용입니다.
	 * 세 자매가 모든 상품을 구입하는데 드는 최소 비용을 리턴하세요.
	 * 
	 */
	public int solution(int[] goods) {
		int price =0;
		int total =0;
		int discount =0;
		for(int i=0; i<goods.length; i++) {
			price+=goods[i];
			if (goods[i]<50) total += goods[i];
			else discount+=10;
		}
		if (total>=50) discount +=10;
		
		price -= discount;
		return price;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ConditionLoop002 p = new ConditionLoop002 ();
		int[] goods = {35,60,10};
		System.out.println(p.solution(goods));
	}

}
