package day3;

import  java.util.*;
import java.io.*;

public class B14226 {
    public static int S, time = Integer.MAX_VALUE;
    public static boolean[] visited = new boolean[1001];
    public static void bfs() {
        Queue<int[][]> queue = new LinkedList<>();
        queue.add(new int[][]{{1, 0, 0}});
        visited[1] = true;
        while (!queue.isEmpty()) {
            int[][] cur = queue.poll();
            int value = cur[0][0];
            int copy = cur[0][1];
            int count = cur[0][2];
            visited[value] = true;

//            System.out.println("value: " + value + " copy: " + copy + " count: " + count);
            if (value == S) {
                if (count < time) {
                    time = count;
                }
                break;
            }

            if (value - 1 > 0 && !visited[value - 1]) {
                queue.add(new int[][]{{value - 1, copy, count + 1}});
            }
            if (value + copy <= 1000 && !visited[value + copy]) {
                queue.add(new int[][]{{value + copy, copy, count + 1}});
            }
            if (value != 0)
                queue.add(new int[][]{{value, value, count + 1}});
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        S = Integer.parseInt(st.nextToken());
        for (int i = 0; i < 1001; i++) {
            visited[i] = false;
        }
        bfs();
        System.out.println(time);
    }
}
