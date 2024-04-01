import java.io.*;
import java.util.*;

public class B2667 {
    static int villageCount = 1; // put -> villageCount로 변경
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        
        int[][] map = new int[N][N];
        boolean[][] visited = new boolean[N][N];
        int[] cnt = new int[N * N + 1];
        
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                map[i][j] = s.charAt(j) - '0';
            }
        }
        
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    cnt[villageCount] = floodfill(i, j, map, visited, N, villageCount++);
                }
                
            }
        }
        
        // System.out.println("\nafter floodfill\n");
        
        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < N; j++) {
        //         System.out.print(map[i][j]);
        //     }
        //     System.out.println();
        // }
        
        System.out.println(villageCount - 1);
        Arrays.sort(cnt, 1, villageCount); // 단지 내의 집의 개수를 오름차순으로 정렬
        for (int i = 1; i < villageCount; i++) {
            System.out.println(cnt[i]);
        }
        
    }

    
    public static int floodfill(int x, int y, int[][] map, boolean[][] visited, int N, int cnt) {
        if (x < 0 || x >= N || y < 0 || y >= N) {
            return 0;
        }
        if (map[x][y] != 1 || visited[x][y]) {
            return 0;
        }
        visited[x][y] = true;
        map[x][y] = cnt;
        return 1 + floodfill(x - 1, y, map, visited, N, cnt) +
                   floodfill(x + 1, y, map, visited, N, cnt) +
                   floodfill(x, y - 1, map, visited, N, cnt) +
                   floodfill(x, y + 1, map, visited, N, cnt);
    }
}
