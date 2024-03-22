package day14;
import java.io.*;
import java.util.*;

public class B11722 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken());
        int[] array = new int[num];
        int[] dp = new int[num];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < num; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = 1;
        for (int i = 1; i < num; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (array[i] < array[j] && dp[i] <= dp[j]) {
                    dp[i] = dp[j] + 1;
                }
            }
        }
        int max = 0;
        for (int i = 0; i < num; i++) {
            if (max < dp[i]) {
                max = dp[i];
            }
        }
        System.out.println(max);
    }
}