package day3;


import java.util.*;
import java.io.*;

public class B2606 {

    public static int N, M, cnt = 0;
    public static int[][] arr;
    public static boolean[] visited;

    public static void dfs (int start) {
        visited[start] = true;
        cnt++;
        for (int i = 1; i <= N; i++) {
            if (arr[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st2.nextToken());

        arr = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = 1;
        }

        dfs(1);
        System.out.println(cnt - 1);
    }

}

//
//import java.util.Scanner;
//
//public class Main {
//    static int map[][];
//    static boolean visit[];
//    static int n, m, v;
//    static int count = 0;
//
//    public static int dfs(int i) {
//        visit[i] = true;
//
//        for(int j=1; j<=n; j++) {
//            if(map[i][j] == 1 && visit[j] == false) {
//                count ++;
//                dfs(j);
//            }
//        }
//        return count;
//    }
//
//    public static void main(String[] args) {
//        Scanner scan = new Scanner(System.in);
//        n = scan.nextInt();	// 컴퓨터 수(정점)
//        m = scan.nextInt();	// 연결된 컴퓨터 쌍의 수(간선)
//        v = 1;	// 탐색 시장할 정점의 번호
//        map = new int[n+1][n+1];	// 각 정점간 탐색 경로를 저장할 배열
//        visit = new boolean[n+1];	// 정점의 탐색 여부 체크
//
//        for(int i=0; i<m; i++) {
//            int a = scan.nextInt();
//            int b = scan.nextInt();
//            map[a][b] = map[b][a]= 1;
//        }
//
//        System.out.println(dfs(1));
//        scan.close();
//    }
//}