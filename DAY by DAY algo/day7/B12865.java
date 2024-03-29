package day7;

import java.util.*;
import java.io.*;

public class B12865 {
    public static int N, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // 개수
        K = Integer.parseInt(st.nextToken()); // 무게
        int[][] dp = new int[N + 1][K + 1];


        int[] W = new int[N + 1]; // 무게
        int[] V = new int[N + 1]; // 가치
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }
        
        for (int k = 1; k <= K; k++) {
            for (int i = 1; i <= N; i++) {
                dp[i][k] = dp[i-1][k];
                if (k - W[i] >= 0) {
                    dp[i][k] = Math.max(dp[i - 1][k], V[i] + dp[i - 1][k - W[i]]);
                }
            }
        }

        System.out.println(dp[N][K]);
    }
}