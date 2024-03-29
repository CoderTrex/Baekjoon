import java.util.*;

public class B14888 {
    public static Scanner sc = new Scanner(System.in);
    public static int N, MIN = Integer.MAX_VALUE, MAX = Integer.MIN_VALUE;
    public static int[] arr, cal;

    public static void main(String[] arg) {
        N = sc.nextInt();
        arr = new int[N];
        cal = new int[4];

        for (int i = 0; i < N; i++) {
            arr[i]  = sc.nextInt();
        }
        for (int i = 0;  i < 4; i++) {
            cal[i] = sc.nextInt();
        }

        dfs(arr[0], 1);
        System.out.println(MAX);
        System.out.println(MIN);
    }

    public static void dfs (int num, int idx) {
        if (idx == N) {
            if (num > MAX)
                MAX = num;
            if (num < MIN)
                MIN = num;
            return ;
        }
        
        for (int i = 0; i < 4; i++) {
            if (cal[i] > 0) {
                cal[i]--;
                switch (i) {
                    case 0:
                        dfs(num + arr[idx], idx + 1);
                        break;
                    case 1:
                        dfs(num - arr[idx], idx + 1);
                        break;
                    case 2:
                        dfs(num * arr[idx], idx + 1);
                        break;
                    case 3:
                        dfs(num / arr[idx], idx + 1);
                        break;
                }
                cal[i]++;
            }
        }
    }
}