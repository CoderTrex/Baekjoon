package day4;

import java.io.*;
import java.util.*;

public class B15486 {
    public static int N;
    public static int[] T, P, dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        T = new int[N]; // 상담을 완료하는데 걸리는 시간
        P = new int[N]; // 상담을 완료했을 때 받을 수 있는 금액
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
        }
        dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            if (i + T[i] <= N) {
                dp[i + T[i]] = Math.max(dp[i + T[i]], dp[i] + P[i]);
            }
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);
        }
        int max = 0;
        for (int i = 0; i <= N; i++) {
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}

