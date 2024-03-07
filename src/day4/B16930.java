package day4;


import java.io.*;
import java.util.*;

public class B16930 {
    public static int height, width, k;
    public static int x1, y1, x2, y2;
    public static int[][] map, map_result;

    public static int[] dt = {1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        height = Integer.parseInt(st.nextToken());
        width = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        map = new int[height][width];
        map_result = new int[height][width];
        for (int i = 0; i < height; i++) {
            String temp = br.readLine();
            for (int j = 0; j < width; j++) {
                if (temp.charAt(j) == '.') map[i][j] = 0;
                else map[i][j] = 1;
                map_result[i][j] = Integer.MAX_VALUE;
            }
        }
        st = new StringTokenizer(br.readLine());
        y1 = Integer.parseInt(st.nextToken()) - 1;
        x1 = Integer.parseInt(st.nextToken()) - 1;
        y2 = Integer.parseInt(st.nextToken()) - 1;
        x2 = Integer.parseInt(st.nextToken()) - 1;
        map[y1][x1] = 2;
        map[y2][x2] = 3;
        map_result[y1][x1] = 0;
        bfs(y1, x1, new boolean[height][width]);
        System.out.println(map_result[y2][x2] == Integer.MAX_VALUE ? -1 : map_result[y2][x2]);
        return ;
    }

    public static void bfs(int i, int j, boolean[][] visited) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{i, j, 0});
        visited[i][j] = true;

        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            for (int l = 0; l < 2; l++) {
                for (int m = 1; m <= k; m++) {
                    int y = temp[0];
                    int x = temp[1] + dt[l] * m;
                    int cnt = temp[2] + 1;
                    if (x < 0 || y < 0 || y >= height || x >= width || map[y][x] == 1 || map[y][x] == 2) {
                        break;
                    }

                    if (map[y][x] == 0 && !visited[y][x]) {
                        queue.offer(new int[]{y, x, cnt});
                        visited[y][x] = true;
                        if (map_result[y][x] > cnt)
                            map_result[y][x] = cnt;
                    }
                    else if (map_result[y][x] < cnt)
                        break;
                    if (map[y][x] == 3) {
                        if (map_result[y][x] > cnt)
                            map_result[y][x] = cnt;
                    }
                }

                for (int m = 1; m <= k; m++) {

                    int y = temp[0] + dt[l] * m;
                    int x = temp[1];
                    int cnt = temp[2] + 1;
                    if (x < 0 || y < 0 || y >= height || x >= width || map[y][x] == 1 || map[y][x] == 2)  {
                        break;
                    }

                    if (map[y][x] == 0 && !visited[y][x]) {
                        queue.offer(new int[]{y, x, cnt});
                        visited[y][x] = true;
                        if (map_result[y][x] > cnt)
                            map_result[y][x] = cnt;
                    }
                    else if (map_result[y][x] < cnt)
                        break;
                    if (map[y][x] == 3) {
                        if (map_result[y][x] > cnt)
                            map_result[y][x] = cnt;
                    }
                }
            }
        }
    }
}
