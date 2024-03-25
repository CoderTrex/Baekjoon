package day3;


import java.io.*;
import java.util.*;

public class B17086 {
    public  static int height, width, max = Integer.MIN_VALUE;
    public static int[][] map , map_result;
    public static int[] dx = {0, 0, 1, -1, 1, 1, -1, -1};
    public static int[] dy = {1, -1, 0, 0, 1, -1, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        height = Integer.parseInt(st.nextToken());
        width = Integer.parseInt(st.nextToken());
        map = new int[height][width];
        map_result = new int[height][width];

        for (int i = 0; i < height; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < width; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) map_result[i][j] = 0;
                else map_result[i][j] = Integer.MAX_VALUE;
            }
        }

        int cntt = 0;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
//                if (map[i][j] == 1 && cntt == 0) {
//                    cntt++;
                if (map[i][j] == 1) {
                    bfs(i, j , new boolean[height][width], 0);

//                    for (int k = 0; k < height; k++) {
//                        for (int l = 0; l < width; l++) {
//                            System.out.print(map_result[k][l] + " ");
//                            max = Math.max(max, map_result[k][l]);
//                        }
//                        System.out.println();
//                    }

                }
            }
        }

        for (int k = 0; k < height; k++) {
            for (int l = 0; l < width; l++) {
//              System.out.print(map_result[k][l] + " ");
                max = Math.max(max, map_result[k][l]);
            }
            System.out.println();
        }

        System.out.println(max);
    }
    public static void bfs(int i, int j, boolean[][] visited, int count) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j, count});
        map[i][j] = 0;
        visited[i][j] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int c = current[2];
            if (map[x][y] == 1) {
                return;
            }

//            System.out.println("start");
//            for (int k = 0; k < height; k++) {
//                for (int l = 0; l < width; l++) {
//                    System.out.print(map_result[k][l] + " ");
//                    max = Math.max(max, map_result[k][l]);
//                }
//                System.out.println();
//            }

            for (int k = 0; k < 8; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (nx >= 0 && ny >= 0 && nx < height && ny < width && !visited[nx][ny] && map[nx][ny] == 0) {
                    visited[nx][ny] = true;
//                    System.out.println("nx : " + nx + " ny : " + ny + " c : " + c);
                    if (map_result[nx][ny] > c + 1) {
                        map_result[nx][ny] = c + 1;
                    }
                    queue.add(new int[]{nx, ny, c + 1});
                }
            }
        }
    }
}
