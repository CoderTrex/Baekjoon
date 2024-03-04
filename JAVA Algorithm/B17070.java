// // dp로 풀려다가 멘탈 붕괴후 dfs 방법 찾음.
// public class Main {
//     public  static int n;
//     public static int[][] arr, cal_matrix;
//     public static boolean[][] visited;
//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         n = Integer.parseInt(st.nextToken());
//         arr = new int[n][n];
//         cal_matrix = new int[n][n];

//         for (int i = 0; i < n; i++) {
//             st = new StringTokenizer(br.readLine());
//             for (int j = 0; j < n; j++) {
//                 arr[i][j] = Integer.parseInt(st.nextToken());
//                 cal_matrix[i][j] = 0;
//                 visited[i][j] = false;
//             }
//         }

//         dp(1, 1, 1, 2);
//     }

//     static void dp(int x1, int y1, int x2, int y2) {
//         if (x2 == n && y2 == n) {
//             return;
//         }

//         if (x1 < 1 || y1 < 1 || x2 < 1 || y2 < 1 || x1 > n || y1 > n || x2 > n || y2 > n) {
//             return;
//         }
//         if (arr[y2][x2] == 1 || arr[y1][x1] == 1 ){
//             return;
//         }

//         if (visited[y2 - 1][x2 - 1] && visited[y2 - 1][x2] && visited[y2][x2 - 1]) {
//             return;
//         }

//         cal_matrix[y2][x2] += cal_matrix[y1][x1] + cal_matrix[y2][x1] + cal_matrix[y1][x2];


//         // 1. 가로로 놓여있는 경우
//         if (y1 == y2 && x1 + 1 == x2) {
//             if (arr[y2][x2 + 1] == 0)
//                 dp(x1 + 1, y1, x2 + 1, y2);
//             if (arr[y2 + 1][x2 + 1] == 0)
//                 dp(x1 + 1, y1, x2 + 1, y2 +1);
//         }
//         // 2. 세로로 놓여있는 경우
//         else if (x1 == x2 && y1 + 1== y2) {
//             if (arr[y2 + 1][x2] == 0)
//                 dp(x1, y1 + 1, x2, y2 + 1);
//             if (arr[y2 + 1][x2 + 1] == 0)
//                 dp(x1, y1 + 1, x2 + 1, y2 + 1);
//         }
//         // 3. 대각선으로 놓여있는 경우
//         else if (y1 + 1== y2 && x1 + 1 == x2) {
//             if (arr[y2][x2 + 1] == 0)
//                 dp(x1 + 1, y1 + 1, x2 + 1, y2);
//             if (arr[y2 + 1][x2] == 0)
//                 dp(x1 + 1, y1 + 1, x2, y2 + 1);
//             if (arr[y2 + 1][x2 + 1] == 0)
//                 dp(x1 + 1, y1 + 1, x2 + 1, y2 + 1);
//         }
//     }
// }
import java.util.*;
import java.io.*;

public class Main {
    public  static int n;
    public static int[][] arr;
    public static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp(0, 1, 0);
        System.out.println(answer);
    }

    static void dp(int x, int y, int direction) {
        if (x == n - 1 && y == n - 1) {
            answer++;
            return;
        }
        if (direction == 0) {
            if (y + 1 < n && arr[x][y + 1] == 0) {
                dp(x, y + 1, 0);
            }
        } else if (direction == 1) {
            if (x + 1 < n && arr[x + 1][y] == 0) {
                dp(x + 1, y, 1);
            }
        } else if (direction == 2) {
            if (y + 1 < n && arr[x][y + 1] == 0) {
                dp(x, y + 1, 0);
            }
            if (x + 1 < n && arr[x + 1][y] == 0) {
                dp(x + 1, y, 1);
            }
        }
        if (x + 1 < n && y + 1 < n && arr[x + 1][y] == 0 && arr[x][y + 1] == 0 && arr[x + 1][y + 1] == 0) {
            dp(x + 1, y + 1, 2);
        }
    }
}
