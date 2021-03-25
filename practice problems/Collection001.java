package collection;

import java.util.*;

public class Collection001{

	/* Problem:
	 * We have an array of song's genres, and an array of song's play counts (each array in any order)
	 * find an algorithm to return an array which contains
	 * index number of two songs of two genres selected by the following standards:
	 * 1. genre of the most played song must be included first
	 * 2. within the genre most played songs must be included first
	 * 3. if the play counts of two songs are equal, include the song with lower index number first
	 * 
	 * Solution key:
	 * Figure out which collection framework (+their methods) should be used
	 * to arrange & select the desired elements
	 */
	public int[] solution(String[] genres, int[] plays) {
				
		ArrayList<Integer> answerList = new ArrayList<Integer>();
		HashMap<String, Integer> genreCnt = new HashMap<String, Integer>();
		HashMap<Integer, String> cntGenre = new HashMap<Integer, String>();
		
		LinkedList<Integer> sortCnt = new LinkedList<Integer>();
		
		//An unbounded priority queue based on a priority heap.
		//ordered by elements' natural ordering or by a Comparator provided at queue construction time
		//(in this case, Collections.reverseOrder() is provided)
		PriorityQueue<Integer> queue = new PriorityQueue<Integer>(Collections.reverseOrder());
		
        //if same genre exists in genreCnt HashMap already, then add the new cnt number to the existing cnt number
        // so, result in genreCnt HashMap of: keys=unique genres & values=each genre's total play cnt numbers
        for(int i=0; i<genres.length; i++) {
            if(genreCnt.containsKey(genres[i])) genreCnt.put(genres[i], genreCnt.get(genres[i])+plays[i]);
            else genreCnt.put(genres[i], plays[i]);
        }
        //cntGenre will have map of key=total play counts & values=genre
        //sortCnt will have linkedList of total play counts for each genre
        for(String tmp: genreCnt.keySet()) {
        	cntGenre.put(genreCnt.get(tmp),tmp);
        	sortCnt.add(genreCnt.get(tmp));        	
        }
        //order the total play counts for each genre in asc order
        Collections.sort(sortCnt);
        String firstPriorityGenre = "";
        
        for (int i=0; i<genreCnt.size(); i++) {
        	//last element in sortCnt is the highest of the total play counts of genres
        	firstPriorityGenre = cntGenre.get(sortCnt.pollLast());
        	for(int j=0; j<plays.length; j++) {
        		//when firstPriorityGenre=genre, that index number's plays count is added to queue
        		//In the case of example, the most played genre's play counts (more than two) will be added to the queue
        		//Remember queue is a PriorityQueue obj which is in desc order (by specifying Collections.reverseOrder() at its construction time)
        		if(genres[j].equals(firstPriorityGenre)) {
        			queue.add(plays[j]);
        		}
        	}
        	//highest play count from plays[] is put into firstCnt, since poll() is used, the play count is removed from queue.
            int firstCnt = queue.poll();
            int firstIndex = -1;
            int secondCnt = -1;
            boolean flag = true;
            //is queue is not empty yet, second play count is put into secondCnt
            if( !queue.isEmpty()) {
            	secondCnt = queue.poll();
            	queue.clear(); //empty out the play count queue for the next most played genre
            }
            for(int j=0; j<plays.length;j++) {
            	//flag is used to skip the following if condition statements when firstIndex is found
            	if(flag) {
            		if(plays[j] == firstCnt && genres[j].equals(firstPriorityGenre)) {
            			answerList.add(j);
            			flag=false;
            			firstIndex=j;
            			j=0;
            		}
            	}
            	if(firstIndex>=0 && secondCnt>0 && genres[j].equals(firstPriorityGenre)) {
            		if(plays[j] == secondCnt && j!= firstIndex) {
            			answerList.add(j);
            			break;
            		}
            	}
            }
        }
        int[] ans = new int[answerList.size()];
        for( int i=0; i<answerList.size(); i++) {
        	ans[i] = answerList.get(i);
        }
		return ans;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] genres = {"classic", "pop", "classic", "classic", "pop"};
		int[] plays= {500, 600, 150, 800, 2500};
		BestAlbumSolution ba = new BestAlbumSolution();
		for (int x : ba.solution(genres, plays))
			System.out.print(x+" ");
	}

}
