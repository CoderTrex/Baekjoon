// import java.io.*;
// import java.util.*;

// public class B2293 {
//     public static int n, k;
//     public static int[] coins;
//     public static int count = 0;

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         n = Integer.parseInt(st.nextToken());
//         k = Integer.parseInt(st.nextToken());
//         coins = new int[n];

//         for (int i = 0; i < n; i++) {
//             coins[i] = Integer.parseInt(br.readLine());
//         }

//         dp(0, 0);
//         System.out.println(count);
//     }

//     public static void dp(int sum, int index) {
//         if (sum == k) {
//             count++;
//             return;
//         }
//         if (sum > k || index >= n) {
//             return;
//         }
//         dp(sum + coins[index], index);
//         dp(sum, index + 1);
//     }
// }

import java.io.*;
import java.util.*;

public class B2293 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] coins = new int[n];
        int[] dp = new int[k + 1];
        dp[0] = 1; 

        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
            for (int j = coins[i]; j <= k; j++) {
                dp[j] += dp[j - coins[i]];
            }
        }

        System.out.println(dp[k]);
    }
}

