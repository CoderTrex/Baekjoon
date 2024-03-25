// import java.util.*;
// import java.io.*;

// public class B1916 {
//     static int N, M, start_station, end_station;
//     static Vector<Integer> v_min_loc = new Vector<Integer>();

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         N = Integer.parseInt(st.nextToken());
//         M = Integer.parseInt(br.readLine());
//         int[][] graph = new int[N+1][N+1];
        
//         // 모든 배열의 값을 MAX_VALUE로 초기화
//         for (int i = 0; i < N+1; i++) {
//             Arrays.fill(graph[i], Integer.MAX_VALUE);
//         }

//         // 모든 비용 초기화
//         for (int i = 0; i < M; i++) {
//             st = new StringTokenizer(br.readLine());
//             int start = Integer.parseInt(st.nextToken());
//             int end = Integer.parseInt(st.nextToken());
//             int cost = Integer.parseInt(st.nextToken());
//             graph[start][end] = cost;
//         }

//         st = new StringTokenizer(br.readLine());
//         start_station = Integer.parseInt(st.nextToken());
//         end_station = Integer.parseInt(st.nextToken());


//         for (int k = 1; k < N + 1; k++) {
//             for (int i = 1; i < N + 1; i++) {
//                 for (int j = 1; j < N + 1; j++) {
//                     if (graph[i][k] != Integer.MAX_VALUE && graph[k][j] != Integer.MAX_VALUE && graph[i][k] + graph[k][j] < graph[i][j]) {
//                         graph[i][j] = graph[i][k] + graph[k][j];
//                     }
//                 }
//             }
//         }
        

//         for (int i = 1; i < N + 1; i++) {
//             for (int j = i; j < N + 1; j++) {
//                 if (graph[i][j] == Integer.MAX_VALUE) 
//                     graph[i][j] = 0;
//                 System.out.print(graph[i][j] + " ");
//             }
//             System.out.println();
//         }
//     }
// }


import java.util.*;
import java.io.*;


public class B1916 {
    private static final int INF = Integer.MAX_VALUE / 16;
    static List<ArrayList<Node>> graph;
    static int dist[];

    static int N;

    static class Node implements Comparable<Node> {
        int index;
        int weight;

        public Node(int index, int weight) {
            this.index = index;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return weight - o.weight;
        }
    }


    public static void main (String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        dist = new int[N + 1];
        Arrays.fill(dist, INF);

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph.get(start).add(new Node(end, weight));
        }

        st = new StringTokenizer(br.readLine());
        int start_station = Integer.parseInt(st.nextToken());
        int end_station = Integer.parseInt(st.nextToken());
        
        System.out.println(dijkstra(start_station, end_station));
    }

    static int dijkstra(int start, int end) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean visited[] = new boolean[N + 1];

        dist[start] = 0;
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int curIndex = cur.index;

            if (!visited[curIndex]) {
                visited[curIndex] = true;
                
                for (Node node : graph.get(curIndex)) {
                    if (!visited[node.index] && dist[node.index] > dist[curIndex] + node.weight) {
                        dist[node.index] = dist[curIndex] + node.weight;
                        pq.offer(new Node(node.index, dist[node.index]));
                    }
                }
            }
        }
        return dist[end];
    }
}


