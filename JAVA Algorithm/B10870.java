import java.util.Scanner;

public class B10870 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[30];
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 1;

        int n = sc.nextInt();
        if (n == 0) {
            System.out.println(0);
            return;
        }
        else if (n == 1 || n == 2) {
            System.out.println(1);
            return;
        }
        else {
            for (int i = 3; i <= n; i++) {
                arr[i] = arr[i - 1] + arr[i - 2];
            }
        }
        System.out.println(arr[n]);
    }
}
