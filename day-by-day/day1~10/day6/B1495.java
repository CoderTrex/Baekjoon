package day6;

import java.util.*;
import java.io.*;
//(1 ≤ N ≤ 50, 1 ≤ M ≤ 1,000, 0 ≤ S ≤ M
public class B1495 {
    public static int N, S, M; // N: 곡의 개수, M: 볼륨의 최대값, S: 시작 볼륨
    public static int sum = 0;
    public static int[] V;
    public static int max = -1, secondMax = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            V[i] = Integer.parseInt(st.nextToken());
        }

        // 1. dp 방법
        boolean[][] dp = new boolean[N + 1][M + 1];

        dp[0][S] = true;

        // 세로 N, 가로 M
        for (int i = 0; i < N; i++) { // 더하는 값
//            System.out.println(Arrays.toString(dp[i]));
            for (int j = 0; j <= M; j++) { // 현재 값 및 값의 범위
                if (dp[i][j]) {
                    if (j + V[i] <= M) {
                        dp[i + 1][j + V[i]] = true;
                    }
                    if (j - V[i] >= 0) {
                        dp[i + 1][j - V[i]] = true;
                    }
                }
            }
        }

        for (int i = 0; i <= M; i++) {
            if (dp[N][i]) {
                max = i;
            }
        }

        System.out.println(max);

        // 2. dfs 방법
//        int volume = S;
//        dfs(0, volume, sum);
//        System.out.println(max);
    }

//    public static void dfs(int index, int volume, int sum) {
//        if (index == N - 1) {
//            if (volume + V[index] <= M) {
//                volume += V[index];
//                if (max < volume) {
//                    max = volume;
//                }
//            }
//            if (volume - V[index] >= 0) {
//                volume -= V[index];
//                if (max < volume) {
//                    max = volume;
//                }
//            }
//            return ;
//        }
//        if (volume + V[index] <= M) {
//            dfs(index + 1, volume + V[index], sum - V[index]);
//        }
//        if (volume - V[index] >= 0) {
//
//            if (volume - V[index] + sum < max) {
//                if (secondMax == -1) {
//                    secondMax = volume - V[index] + sum;
//                }
//                else {
//                    if (secondMax > volume - V[index] + sum) {
//                        return ;
//                    }
//                }
//            }
//
//            dfs(index + 1, volume - V[index], sum - V[index]);
//        }
//    }
}
