package day12;

import java.io.*;
import java.util.*;

public class B12996 {
    public static int S, dotorya, kesakiyo, hongjun7;
    public static long[][][][] dp;

    public static long dp(int s, int dotorya, int kesakiyo, int hongjun7) {
        if (s <= 0) {
            if (dotorya == 0 && kesakiyo == 0 && hongjun7 == 0) {
                return 1;
            } else {
                return 0;
            }
        }
        if (dotorya < 0 || kesakiyo < 0 || hongjun7 < 0) {
            return 0;
        }
        if (dp[s][dotorya][kesakiyo][hongjun7] != -1) {
            return dp[s][dotorya][kesakiyo][hongjun7];
        }
        long result = 0;
        result += dp(s - 1, dotorya - 1, kesakiyo, hongjun7);
        result += dp(s - 1, dotorya, kesakiyo - 1, hongjun7);
        result += dp(s - 1, dotorya, kesakiyo, hongjun7 - 1);
        result += dp(s - 1, dotorya - 1, kesakiyo - 1, hongjun7);
        result += dp(s - 1, dotorya - 1, kesakiyo, hongjun7 - 1);
        result += dp(s - 1, dotorya, kesakiyo - 1, hongjun7 - 1);
        result += dp(s - 1, dotorya - 1, kesakiyo - 1, hongjun7 - 1);
        result %= 1000000007;
        return dp[s][dotorya][kesakiyo][hongjun7] = result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        dotorya = Integer.parseInt(st.nextToken());
        kesakiyo = Integer.parseInt(st.nextToken());
        hongjun7 = Integer.parseInt(st.nextToken());

        dp = new long[S + 1][dotorya + 1][kesakiyo + 1][hongjun7 + 1];
        for (int i = 0; i <= S; i++) {
            for (int j = 0; j <= dotorya; j++) {
                for (int k = 0; k <= kesakiyo; k++) {
                    Arrays.fill(dp[i][j][k], -1);
                }
            }
        }
        System.out.println(dp(S, dotorya, kesakiyo, hongjun7));
    }
}

//package day12;
//
//import java.util.*;
//import java.io.*;
//
//public class B12996 {
//
//    // 차례대로 총 곡수, a,b,c가 부를 곡 일 때 가능한 경우의 수를 담을 변수
//    static long[][][][] d;
//    static final long mod = 1000000007;
//
//    static long go(int s, int a, int b, int c){
//
//        // 모든 곡을 다 불렀다!
//        if( s <= 0 ){
//            // abc 모두가 할당량만큼 불렀다! -> 성공
//            if( a == 0 && b == 0 && c == 0) return 1;
//                // 누군가는 할당량만큼 부르지 못했다 -> 실패
//            else return 0;
//        }
//
//        // 어레이 인덱스 못잡는 에러 막기 위함
//        if( a < 0 || b < 0 || c < 0){
//            return 0;
//        }
//
//        // 메모된 값이 있다면 꺼내쓰자
//        if(d[s][a][b][c] != -1 ){
//            return d[s][a][b][c];
//        }
//
//        // 가능한 경우의 수를 누적시킬 변수
//        long ans = 0;
//
//        for(int i = 0 ; i <= 1 ; i++){
//            for(int j = 0 ; j <= 1 ; j++){
//                for(int k = 0 ; k <= 1 ; k++){
//                    if(i+j+k > 0){ // 누구든 부르기만 한다면
//                        ans += go(s-1, a-i, b-j, c-k); // 부르러 가자!
//                    }
//                }
//            }
//        }
//
//        ans %= mod;
//        // 메모이제이션 잊지 말자
//        d[s][a][b][c] = ans;
//        // 날 부른 go에게 내가 만들 수 있는 모든 경우의 수를 바친다
//        return ans;
//    }
//
//
//    public static void main(String []args) throws IOException{
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        int s = Integer.parseInt(st.nextToken());
//        int a = Integer.parseInt(st.nextToken());
//        int b = Integer.parseInt(st.nextToken());
//        int c = Integer.parseInt(st.nextToken());
//        d = new long[s+1][a+1][b+1][c+1];
//
//        for(int i = 0 ; i <= s ; i++ ){
//            for(int j = 0 ; j <= a ; j++){
//                for(int k = 0 ; k <= b ; k++ ){
//                    Arrays.fill(d[i][j][k], -1);
//                }
//            }
//        }
//        System.out.println(go(s, a, b, c));
//    }
//}
