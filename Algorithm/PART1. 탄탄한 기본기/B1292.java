import java.util.*;

public class B1292 {
    static int check_out(int num) {
        int sum = 0, i;
        for (i = 1; sum < num; i++) {
            sum += i;
        }
        return i - 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int sum = 0;
        sc.close();
        for (int i = A; i <= B; i++) {
            sum += check_out(i);
        }

        System.out.println(sum);
    }
}

