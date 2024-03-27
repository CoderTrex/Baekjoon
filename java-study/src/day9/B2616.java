package day9;

import java.util.*;
import java.io.*;




public class B2616 {
    public static int N, M; // N: 객차의 수, M: 최대로 물품을 수용할 수 있는 객차의 수
    public static int[] train;
    public static int[] trainSum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        train = new int[N + 1];
        trainSum = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            train[i] = Integer.parseInt(st.nextToken());
            trainSum[i] = trainSum[i - 1] + train[i];
        }

        int[][] dp = new int[4][N + 1];

        st = new StringTokenizer(br.readLine());
        int max = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= 3; i++) {
            for (int j = i * max; j <= N; j++) {
                dp[i][j] = Math.max(dp[i][j - 1], dp[i-1][j-max] + trainSum[j] - trainSum[j - max]);
            }
        }
        System.out.println(dp[3][N]);
    }
}



//public class B2616 {
//    public static int N, M; // N: 객차의 수, M: 최대로 물품을 수용할 수 있는 객차의 수
//    public static int[] train; // 객차별 물품의
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        N = Integer.parseInt(st.nextToken());
//        train = new int[N];
//        st = new StringTokenizer(br.readLine());
//        for (int i = 0; i < N; i++) {
//            train[i] = Integer.parseInt(st.nextToken());
//        }
//        st = new StringTokenizer(br.readLine());
//        M = Integer.parseInt(st.nextToken());
//
//        int[] sum_arr = new int[N - (M - 1)];
//        for (int i = 0; i < N - (M - 1); i++) {
//            for (int j = i; j < i + M; j++) {
//                sum_arr[i] += train[j];
//            }
//        }
//        int MAX = Integer.MIN_VALUE;
//        int value;
//
//        int new_arr_len = N - (M - 1);
//
//        for (int i = 0; i < (new_arr_len - 2 - (M - 1)*2); i++) {
//            for (int j = i + (M); j < (new_arr_len - 1 - (M - 1)); j++) {
//                for (int k = j + (M); k < new_arr_len; k++) {
////                    System.out.println(sum_arr[i] + " " + sum_arr[j] + " " + sum_arr[k]);
//                    value = sum_arr[i] + sum_arr[j] + sum_arr[k];
//                    if (value > MAX) {
//                        MAX = value;
//                    }
//                }
//            }
//        }
//
//        System.out.println(MAX);
//    }
//}
