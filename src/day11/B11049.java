package day11;


import java.io.*;
import java.util.*;

public class B11049 {
    static int n, INF = Integer.MAX_VALUE;
    static int[] data;
    static int[][] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int size = arr.length;
        int[][] dp = new int[size][size];

        for (int i = 0; i < size - 1; ++i) {
            dp[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1];
        }

        for (int gap = 2; gap < size; gap++) {
            for (int i = 0; i + gap < size; i++) {
                int j = i + gap;
                dp[i][j] = INF;
                for (int k = i; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1]);
                }
            }
        }

        System.out.println(dp[0][size-1]);
    }
}