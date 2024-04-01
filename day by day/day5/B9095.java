package day5;


import java.io.*;
import java.util.*;

public class B9095 {
    public static int N;
    public static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[11];

        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 4;
        for (int i = 3; i < 11; i++) {
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3];
//            System.out.println(dp[i]);
        }
        for (int i = 0; i < 3; i++) {
            System.out.println(dp[arr[i] - 1]);
        }
    }
}


//package day5;
//
//import java.io.*;
//        import java.util.*;
//
//public class B9095 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int T = Integer.parseInt(br.readLine()); // 테스트 케이스의 개수
//
//        int[] dp = new int[11]; // dp 배열 초기화
//
//        dp[0] = 1;
//        dp[1] = 2;
//        dp[2] = 4;
//
//        for (int i = 3; i < 11; i++) {
//            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
//        }
//
//        for (int t = 0; t < T; t++) {
//            int n = Integer.parseInt(br.readLine()); // 입력값 n
//
//            System.out.println(dp[n-1]); // 정답 출력
//        }
//    }
//}
