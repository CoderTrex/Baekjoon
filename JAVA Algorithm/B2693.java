import java.util.*;

public class B2693 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] arr = new int[T];

        for (int i = 0; i < T; i++) {
            PriorityQueue<Integer> pQ = new PriorityQueue<>(Collections.reverseOrder());
            for (int k = 0; k < 10; k++) {
                pQ.offer(sc.nextInt());
            }
            pQ.poll();
            pQ.poll();
            arr[i] = pQ.poll();
        }
        for (int i = 0; i < T; i++) {
            System.out.println(arr[i]);
        }
    }
}
