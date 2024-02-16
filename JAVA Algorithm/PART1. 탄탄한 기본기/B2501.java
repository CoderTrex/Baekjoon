

import java.util.Scanner;

public class B2501 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int Num = sc.nextInt();
        int K = sc.nextInt();
        int count = 0;
        sc.close();
        for (int i = 1; i <= Num; i++) {
            if (Num % i == 0) {
                count++;
            }
            if (count == K) {
                System.out.println(i);
                return;
            }
        }
        System.out.println(0);
    }
}
