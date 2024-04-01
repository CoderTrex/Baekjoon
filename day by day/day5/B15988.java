//package day5;
//
//import java.io.*;
//import java.util.*;
//
//public class B15988 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        Vector<Integer> vec = new Vector<>();
//        Vector<Integer> input = new Vector<>();
//
//        int n = Integer.parseInt(st.nextToken());
//        int find = 0;
//
//        for (int i = 0; i < n; i++) {
//            st = new StringTokenizer(br.readLine());
//            int num = Integer.parseInt(st.nextToken());
//            input.add(num); // input 벡터에 요소 추가
//        }
//
//        Collections.sort(input); // input 벡터 정렬
//
//        int max = input.get(n - 1);
//        for (int i = 0; i < 3; i++) {
//            int num = input.get(i);
//            if (num == 1) {
//                System.out.println(1);
//                find++;
//            } else if (num == 2) {
//                System.out.println(2);
//                find++;
//            } else if (num == 3) {
//                System.out.println(4);
//                find++;
//            }
//        }
//
//        // input 벡터를 사용하여 vec 벡터 초기화
//        vec.add(1);
//        vec.add(2);
//        vec.add(4);
//
//        int new_int;
//        for (int i = 4; i <= max; i++) {
//            new_int = vec.get(0) + vec.get(1) + vec.get(2);
//            if (i == input.get(find)) {
//                System.out.println(new_int);
//                find++;
//            }
//            vec.remove(0);
//            vec.add(new_int);
//        }
//    }
//}

package day5;

import java.io.*;
import java.util.*;

public class B15988 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long[] dp = new long[1000001];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i < 1000001; i++) {
            // dp[i] = 1로 i 만드는 방법 + 2로 i 만드는 방법 + 3으로 i 만드는 방법
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009;
        }

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();

            System.out.println(dp[n]);
        }
    }
}