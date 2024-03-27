package day6;

import java.io.*;

public class B11058{
    public static int N;
    public static long[] dp;

    public  static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new long[N + 1];
        
        if (N <= 6) {
            System.out.println(N);
            return;
        }

        for (int i = 1; i <= 6; i++)
            dp[i] = i;

        for (int i = 7; i <= N; i++) {
            for (int j = 3; j <= i; j++) {
                long copied = dp[j]; // 복사된 수
                long paste = dp[j] * (i - j - 2); // 붙여넣기
                // System.out.println("i: " + i + " j: " + j + " copied: " + copied + " paste: " + paste);
                if (paste <= 0)
                    break;
                if (dp[i] < copied + paste)
                    dp[i] = copied + paste;
            }
        }

        System.out.println(dp[N]);
    }
}