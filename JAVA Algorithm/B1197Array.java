import java.util.*;
import java.io.*;

public class B1197Array {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int[][] graph = new int[V+1][V+1];
        int[] visited = new int[(V+1)];
        int span = 0, cnt = 0;

        for (int i = 0; i < V+1; i++) {
            Arrays.fill(graph[i], Integer.MAX_VALUE);
            visited[i] = 0;
        }
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[start][end] = cost;
        }
        
        
        while ( cnt < V - 1) {
            int min_value = Integer.MAX_VALUE, min_x = 0, min_y = 0;
            for (int i = 1; i < V + 1; i++) {
                for (int j = i + 1; j < V + 1; j++) {
                    if (graph[i][j] == Integer.MAX_VALUE) continue;
                    if (graph[i][j] < min_value) {
                        min_value = graph[i][j];
                        min_x = i;
                        min_y = j;
                    }
                }
            }
            if (visited[min_x] < 2 && visited[min_y] < 2) {
                min_value = graph[min_x][min_y];
                visited[min_x] += 1;
                visited[min_y] += 1;
                span += min_value;
                graph[min_x][min_y] = Integer.MAX_VALUE;
                cnt++;
            }
            else {
                graph[min_x][min_y] = Integer.MAX_VALUE;
            }
        }
        
        System.out.println(span);
    }
}
