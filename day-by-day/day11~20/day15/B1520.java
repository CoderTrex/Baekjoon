package day15;

import java.util.Scanner;

public class B1520 {
    static int M, N;
    static int[][] map;
    static int[][] dp;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        M = scanner.nextInt();
        N = scanner.nextInt();

        map = new int[M][N];
        dp = new int[M][N];

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = scanner.nextInt();
                dp[i][j] = -1; // 초기값 -1로 설정
            }
        }
        System.out.println(dfs(0, 0));
    }

    static int dfs(int x, int y) {
        if (x == M - 1 && y == N - 1) // 도착 지점에 도달한 경우
            return 1;

        if (dp[x][y] != -1) // 이미 계산한 경우
            return dp[x][y];

        dp[x][y] = 0; // 초기화

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) // 범위를 벗어나는 경우
                continue;

            if (map[nx][ny] < map[x][y]) // 이동 가능한 경우
                dp[x][y] += dfs(nx, ny);
        }

        return dp[x][y];
    }
}
