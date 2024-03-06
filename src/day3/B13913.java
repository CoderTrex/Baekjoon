package day3;


import java.util.*;
import java.io.*;

public class B13913 {
    public static int subin, sister, time, cnt;
    public static Stack<Integer> pathQ;

    static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        pathQ = new Stack<>();
        int[] path = new int[100001]; // 이전 위치를 저장하기 위한 배열
        boolean[] visited = new boolean[100001];
        int[] dist = new int[100001];

        q.add(subin);
        visited[subin] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (cur == sister) {
                time = dist[cur];
                int idx = cur;
                while (idx != subin) {
                    pathQ.add(idx);
                    idx = path[idx];
                }
                pathQ.add(subin);
                return;
            }

            if (cur + 1 <= 100000 && !visited[cur + 1]) {
                q.add(cur + 1);
                visited[cur + 1] = true;
                dist[cur + 1] = dist[cur] + 1;
                path[cur + 1] = cur;
            }
            if (cur * 2 <= 100000 && !visited[cur * 2]) {
                q.add(cur * 2);
                visited[cur * 2] = true;
                dist[cur * 2] = dist[cur] + 1;
                path[cur * 2] = cur;
            }
            if (cur - 1 >= 0 && !visited[cur - 1]) {
                q.add(cur - 1);
                visited[cur - 1] = true;
                dist[cur - 1] = dist[cur] + 1;
                path[cur - 1] = cur;
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
            for (int i = subin; i >= sister; i--) {
                System.out.print(i + " ");
            }
            return;
        }
        bfs();

        System.out.println(time);
        while (!pathQ.isEmpty()) {
            System.out.print(pathQ.pop() + " ");
        }
    }
}