import java.util.*;
import java.io.*;

public class Main {
    public static int cnt = 0;
    public  static int[][] map;
    public  static boolean[][] visited;
    public final static int BLACK = 1, WHITE = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        visited = new boolean[M][N];
        map = new int[M][N];

         for (int i = 0; i < M; i++) {
             String str = br.readLine();
             for (int j = 0; j < N; j++) {
                map[i][j] = str.charAt(j) == 'W' ? 0 : 1;
                visited[i][j] = false;
             }
         }

         int blackCnt = 0, whiteCnt = 0;
         for (int i = 0; i < M; i++) {
             for (int j = 0; j < N; j++) {
                 if (!visited[i][j])
                     check(i, j, map[i][j]);
                 if (map[i][j] == BLACK)
                    blackCnt += cnt * cnt;
                 else
                    whiteCnt += cnt * cnt;
                cnt = 0;
             }
         }
         System.out.println(whiteCnt + " " + blackCnt);
    }

    public static void check(int y, int x, int color) {
        if (y < 0 || x < 0 || y >= map.length || x >= map[0].length) {
            return;
        }
        if (map[y][x] != color || visited[y][x]) {
            return;
        }
        visited[y][x] = true;
        if (y + 1 < map.length) {
            if (map[y + 1][x] == color) {
                check(y + 1, x, color);
            }
        }
        if (y - 1 >= 0) {
            if (map[y - 1][x] == color) {
                check(y - 1, x, color);
            }
        }
        if (x + 1 < map[0].length) {
            if (map[y][x + 1] == color) {
                check(y, x + 1, color);
            }
        }
        if (x - 1 >= 0) {
            if (map[y][x - 1] == color) {
                check(y, x - 1, color);
            }
        }
        cnt++;
    }
}