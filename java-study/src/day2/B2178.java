package day2;


import java.io.*;
import java.util.*;
public class B2178 {
    public static int N, M;
    public static int[][] map;

    public static int cnt = Integer.MAX_VALUE;
    public static int[] dx = {1, 0, -1, 0};
    public static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        boolean[][] visited = new boolean[N][M];
        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }
//      dfs(0, 0, 1, visited);
        bfs(0, 0, 1, visited);
        System.out.println(cnt);
    }
    public  static void bfs(int x, int y, int count, boolean[][] visited) {
        Queue<Integer[][]> q = new LinkedList<>();
        q.offer(new Integer[][]{{x, y, count}});
        visited[x][y] = true;

        while (!q.isEmpty()) {
            int x1 = q.peek()[0][0];
            int y1 = q.peek()[0][1];
            int count1 = q.peek()[0][2];

            if (x1 == N - 1 && y1 == M - 1) {
                if (cnt > count1) {
                    cnt = count1;
                }
                return;
            }
            q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = x1 + dx[i];
                int ny = y1 + dy[i];
                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }
                if (map[nx][ny] == 0 || visited[nx][ny]) {
                    continue;
                }
                q.offer(new Integer[][]{{nx, ny, count1 + 1}});
                visited[nx][ny] = true;
            }
        }
    }

    public static void dfs(int x, int y, int count, boolean[][] visited) {
        if (x == N - 1 && y == M - 1) {
            if (cnt > count) {
                cnt = count;
            }
            return;
        }
        if (x < 0 || y < 0 || x >= N || y >= M || map[x][y] == 0 || visited[x][y]) {
            return;
        }
        visited[x][y] = true;
        dfs(x + 1, y, count + 1, visited);
        dfs(x, y + 1, count + 1, visited);
        dfs(x - 1, y, count + 1, visited);
        dfs(x, y - 1, count + 1, visited);
        visited[x][y] = false;
    }
}

