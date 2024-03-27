package day5;

import java.io.*;
import java.util.*;
public class B12101 {
    public static int n, k;
    public static int[] dp;
    public static int[][] array = new int[11][];

    public static void main(String[] args) throws  IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        ArrayList<String>[] arr = new ArrayList[12];
        for(int i = 0; i <= n+2; i++)
            arr[i] = new ArrayList<>();

        arr[1].add("1");
        arr[2].add("1+1");
        arr[2].add("2");
        arr[3].add("1+1+1");
        arr[3].add("1+2");
        arr[3].add("2+1");
        arr[3].add("3");

        for(int i = 4; i <= n; i++)
            for(int j = 1; j <= 3; j++)
                for(String str : arr[i-j])
                    arr[i].add(j + "+" + str);


        if(arr[n].size() < k)
            System.out.println(-1);
        else
            System.out.println(arr[n].get(k-1));
    }
}
