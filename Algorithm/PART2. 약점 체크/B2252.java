import java.util.*;
import java.io.*;

public class B2252 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        ArrayList<Integer>[] list = new ArrayList[N+1]; // 인접리스트 : 각 노드에 연결된 노드들을 저장
        int[] arr = new int[N+1]; // 진입차수를 저장할 배열

        for (int i = 0; i <= N; i++) {
            list[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
        
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
        
            list[a].add(b); // a -> b
            arr[b]++; // b의 진입차수 증가
        }

        Queue<Integer> q = new LinkedList<Integer>();

        // 진입차수가 0인 노드들을 큐에 추가
        for (int i = 1; i <= N; i++) {
            if (arr[i] == 0) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            // 큐에서 하나씩 꺼내서 출력
            System.out.print(q.peek() + " "); // 출력
            int x = q.poll();

            // x와 연결된 노드들의 진입차수 감소
            for (int i = 0; i < list[x].size(); i++) {
                int y = list[x].get(i); // x -> y
                arr[y]--; // y의 진입차수 감소
                if (arr[y] == 0) {
                    q.add(y); // 진입차수가 0이면 큐에 추가
                }
            }
        }
    }
}
