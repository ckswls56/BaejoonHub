import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		int m = in.nextInt();
		HashMap<String, Integer> map = new HashMap<String,Integer>();
		String arr[] = new String[n];
		for(int i=0; i<n; i++) {
			arr[i] = in.next();
			map.put(arr[i],1);
		}
		
	
		for(int i=0; i<m;i++) {
			String temp = in.next();
			map.put(temp,map.getOrDefault(temp, 0)+1);
		}
		
		int count = 0;
		//BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String list[] = new String[n];
		for(int i=0; i<n; i++) {
			String temp = arr[i];
			
			if(map.get(temp)== 2) {
				list[i]=temp + "\n";
				count++;
			}
			else
				list[i]="";
			
		}
		
		Arrays.sort(list);
		
		System.out.println(count);
		for(int i=0;i<n;i++)
			System.out.print(list[i]);

	}
}
