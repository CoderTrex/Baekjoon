package day11;
//  | 정렬 방식 | 시간 복잡도
//
//Arrays.sort() | DualPivotQuicksort
//평균 : O(nlog(n)) / 최악 : O(n^2)
//
//Collections.sort() | TimeSort (삽입정렬과 합병정렬을 결합한 정렬)
//평균, 최악 : O(nlog(n))


import javax.swing.plaf.synth.SynthUI;
import java.io.*;
import java.util.*;

public class B12869 {
    public static int[] arr = {1, 3, 9};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        Queue<ArrayList<Integer>> q = new LinkedList<>();
        ArrayList<Integer> temp = new ArrayList<>();
        for (int i = 0; i < n; ++i)
            temp.add(Integer.parseInt(st.nextToken()));
        if (n == 1) {
            temp.add(0);
            temp.add(0);
        } else if (n == 2) {
            temp.add(0);
        }

        Collections.sort(temp);
        q.offer(temp);

        bfs(q);
    }

    public static void bfs(Queue<ArrayList<Integer>> que) {

        int cnt = 0;
        while (!que.isEmpty()) {
            cnt++;
            // System.out.print("cnt : " + cnt);
            // System.out.println("  que size : " + que.size());


            int size = 0;
            int qSize = que.size();
            while (size < qSize) {
                size++;

                // System.out.println("size : " + size + "  que size : " + que.size() + "  qSize : " + qSize + "  cnt : " + cnt);

                ArrayList<Integer> temp = que.poll();
                // System.out.println(temp);

                if (temp.get(0) <= 0 && temp.get(1) <= 0 && temp.get(2) <= 0 ){
                     System.out.println(cnt - 1);
                    return;
                }
                Collections.sort(temp, Collections.reverseOrder());

                ArrayList<Integer> temp2 = new ArrayList<>(temp);
                if (temp2.get(1) <= 0) {
                    // System.out.println("temp2.get(1) <= 0");
                    temp2.set(0, temp2.get(0) - 9);
                    temp2.set(1, temp2.get(1) - 3);
                    temp2.set(2, temp2.get(2) - 1);
                    que.offer(temp2);
                } else if (temp2.get(2) <= 0) {
                    // System.out.println("temp2.get(2) <= 0");

                    if (temp2.get(1) > 9) {
                        temp2.set(0, temp2.get(0) - 9);
                        temp2.set(1, temp2.get(1) - 3);
                        temp2.set(2, temp2.get(2) - 1);
                        que.offer(temp2);
                    } else {
                       temp2.set(0, temp2.get(0) - 9);
                       temp2.set(1, temp2.get(1) - 3);
                       temp2.set(2, temp2.get(2) - 1);
                       que.offer(temp2);

                       temp2 = new ArrayList<>(temp);
                       temp2.set(0, temp2.get(0) - 3);
                       temp2.set(1, temp2.get(1) - 9);
                       temp2.set(2, temp2.get(2) - 1);
                       que.offer(temp2);
                    }
               } else {
                    // System.out.println("else");

                    if (temp2.get(2) > 9) {
                        temp2.set(0, temp2.get(0) - 9);
                        temp2.set(1, temp2.get(1) - 3);
                        temp2.set(2, temp2.get(2) - 1);
                        que.offer(temp2);
                    } else {
                        temp2.set(0, temp2.get(0) - 9);
                        temp2.set(1, temp2.get(1) - 3);
                        temp2.set(2, temp2.get(2) - 1);
                        que.offer(temp2);

                        temp2 = new ArrayList<>(temp);
                        temp2.set(0, temp2.get(0) - 9);
                        temp2.set(1, temp2.get(1) - 1);
                        temp2.set(2, temp2.get(2) - 3);
                        que.offer(temp2);

                        temp2 = new ArrayList<>(temp);
                        temp2.set(0, temp2.get(0) - 3);
                        temp2.set(1, temp2.get(1) - 9);
                        temp2.set(2, temp2.get(2) - 1);
                        que.offer(temp2);

                        temp2 = new ArrayList<>(temp);
                        temp2.set(0, temp2.get(0) - 3);
                        temp2.set(1, temp2.get(1) - 1);
                        temp2.set(2, temp2.get(2) - 9);
                        que.offer(temp2);

                        temp2 = new ArrayList<>(temp);
                        temp2.set(0, temp2.get(0) - 1);
                        temp2.set(1, temp2.get(1) - 9);
                        temp2.set(2, temp2.get(2) - 3);
                        que.offer(temp2);

                        temp2 = new ArrayList<>(temp);
                        temp2.set(0, temp2.get(0) - 1);
                        temp2.set(1, temp2.get(1) - 3);
                        temp2.set(2, temp2.get(2) - 9);
                        que.offer(temp2);
                    }
               }
            }
        }
    }
}
