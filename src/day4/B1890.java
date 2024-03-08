package day4;

import java.io.*;
import java.util.*;

public class B1890 {
    public static int N, cnt = 0;
    public static int[][] board;
    public static long[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        dp = new long[N * N];


        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++)
                board[i][j] = Integer.parseInt(st.nextToken());
        }

        dp[0] = 1;
        for (int i = 0; i < N * N; i++) {

            if (dp[i] == 0) continue;

            int jump = board[i / N][i % N];

            int y = i / N, y_jump = y + jump; // 이동한 y 좌표
            int x = i % N, x_jump = x + jump; // 이동한 x 좌표
            if (x == N - 1 && y == N - 1) {
                break;
            }
            if (y_jump < N) {
//                System.out.print("y_jump: ");
//                System.out.println("i: " + i + " y: " + y + " x: " + x + " jump: " + jump);
                dp[y_jump * N + x] += dp[i];
            }
            if (x_jump < N){
//                System.out.print("x_jump: ");
//                System.out.println("i: " + i + " y: " + y + " x: " + x + " jump: " + jump);
                dp[y * N + x_jump] += dp[i];
            }
        }

        System.out.println(dp[N * N - 1]);
//        dfs(0, 0);
//        System.out.println(cnt);
    }

//    public static void dfs(int x, int y) {
//        if (x == N - 1 && y == N - 1) {
//            cnt++;
//            return;
//        }
//        if (x < 0 || x >= N || y < 0 || y >= N ) return;
//        if (dp[x][y] != 0) return;
//
//        int jump = board[x][y];
//        x = jump + x;
//        if (x < N && y < N) {
//            dfs(x, y);
//        }
//        x = x - jump;
//        y = jump + y;
//        if (x < N && y < N) {
//            dfs(x, y);
//        }
//    }
}

