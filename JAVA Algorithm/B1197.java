import java.util.*;
import java.io.*;


class Edge implements Comparable<Edge> {
    int V1, V2, weight;

    public Edge(int V1, int V2, int weight) {
        this.V1 = V1;
        this.V2 = V2;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge e) {
        return this.weight - e.weight;
    }
}


public class B1197 {
    static StringTokenizer st;
    static int V, E;
    static int[] parent;
    static PriorityQueue<Edge> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        parent = new int[V+1];
        queue = new PriorityQueue<>();

        for (int i = 0; i <= V; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int V1 = Integer.parseInt(st.nextToken());
            int V2 = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            queue.add(new Edge(V1, V2, weight));
        }

        int span = 0;
        while (!queue.isEmpty()) {
            Edge edge = queue.poll();
            if (find(edge.V1) != find(edge.V2)) {
                union(edge.V1, edge.V2);
                span += edge.weight;
            }
        }

        System.out.println(span);
    }

    public static int find(int V) {
        if (V == parent[V]) return V;
        return parent[V] = find(parent[V]);
    }

    public static void union(int V1, int V2) {
        V1 = find(V1);
        V2 = find(V2);
        if (V1 != V2) parent[V2] = V1;
    }
}
