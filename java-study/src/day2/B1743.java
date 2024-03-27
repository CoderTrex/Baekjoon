package day2;

import java.io.*;
import java.util.*;
public class B1743 {
    public static int[][] map;
    public static boolean[][] visited;
    public static int Height, Width, N, max = 0, cnt = 0;
    public static int[] dx = {0, 0, 1, -1}, dy = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Height = Integer.parseInt(st.nextToken());
        Width = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new int[Height][Width];
        visited = new boolean[Height][Width];

        for (int i = 0; i < Height; i++) {
            for (int j = 0; j < Width; j++) {
                map[i][j] = 0;
                visited[i][j] = true;
            }
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            map[y - 1][x - 1] = 1;
            visited[y - 1][x - 1] = false; // 방문 여부 설정
        }


        for (int i = 0; i < Height; i++) {
            for (int j = 0; j < Width; j++) {
                if(map[i][j] == 1 && !visited[i][j]) {
                    cnt = 0;
                    bfs(i, j, 0);
                }
            }
        }
        System.out.print(max + 1);
    }

    public static void bfs(int y, int x, int count){
        Queue<Integer[][]> q = new LinkedList<>();
        q.offer(new Integer[][]{{y, x, count}});
        visited[y][x] = true;

        // 큐가 비어있지 않을 때까지 반복
        // 1. 큐에서 하나를 꺼냄
        // 2. 최대값을 구하기 위해 max와 비교
        // 3. 큐에서 꺼낸 값의 상하좌우를 탐색
            // - 4방향 탐색 -
            // 1. 상하좌우 진행
            // 2. 진행된 방향이 배열의 범위를 벗어나지 않는지 확인
            // 3. 진행된 방향이 0인지 확인 또한 방문한 적이 있는지 확인
            // 4. 방문한 적이 없다면 큐에 넣어줌
            // 5. 해당 방향을 방문한 것으로 표시
        while (!q.isEmpty()) {
            int y1 = q.peek()[0][0];
            int x1 = q.peek()[0][1];
            int count1 = q.peek()[0][2];

            if (max < cnt) {
                max = cnt;
            }

            q.poll();

            for (int i = 0; i < 4; i++) {
                int ny = y1 + dy[i];
                int nx = x1 + dx[i];
                if (nx < 0 || ny < 0 || ny >= Height || nx >= Width)
                    continue;
                if (map[ny][nx] == 0 || visited[ny][nx])
                    continue;
                cnt++;
                q.offer(new Integer[][]{{ny, nx, count1 + 1}});
                visited[ny][nx] = true;
                map[ny][nx] = 0;
            }
        }
    }
}
