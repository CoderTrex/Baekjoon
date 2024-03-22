package day3;


import java.awt.*;
import java.util.*;
import java.io.*;

public class B13549 {
    static int subin, sister, time, cnt;



    static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[100001];
        int[] dist = new int[100001];

        q.add(subin);
        visited[subin] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (cur == sister) {
                time = dist[cur];
                return;
            }

            if (cur * 2 <= 100000 && !visited[cur * 2]) {
                q.add(cur * 2);
                visited[cur * 2] = true;
                dist[cur * 2] = dist[cur];
            }
            if (cur - 1 >= 0 && !visited[cur - 1]) {
                q.add(cur - 1);
                visited[cur - 1] = true;
                dist[cur - 1] = dist[cur] + 1;
            }
            if (cur + 1 <= 100000 && !visited[cur + 1]) {
                q.add(cur + 1);
                visited[cur + 1] = true;
                dist[cur + 1] = dist[cur] + 1;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        subin = Integer.parseInt(st.nextToken());
        sister = Integer.parseInt(st.nextToken());

        if (subin >= sister) {
            System.out.println(subin - sister);
            return;
        }
        bfs();

        System.out.println(time);
    }
}
