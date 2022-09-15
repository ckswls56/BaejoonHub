import java.util.HashMap;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		int m = in.nextInt();
		int count = 0;
		HashMap<String, Boolean> map = new HashMap<String,Boolean>();
		
		for(int i=0; i < n; i++) {
			map.put(in.next(), true);
		}
		
		
		for(int i=0;i<m;i++) {
			if(map.get(in.next())!=null)
				count++;
		}
		System.out.println(count);
		
	}

}
