import java.util.*;

public class B1978 {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), cnt = 0;
        int[] arr = new int[N];   
        
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        for (int i = 0; i < N; i++) {
            if (arr[i] == 0 || arr[i] == 1) {
                cnt++;
                continue;
            }
            for (int j = 2; j <= Math.sqrt(arr[i]); j++) {
                if (arr[i] % j == 0) {
                    cnt++;
                    break;
                }
            }
        }

        System.out.println(N - cnt);
    }
}
