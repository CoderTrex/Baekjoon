import java.util.Scanner;

public class B2581 {
    public static void main(String arg[]) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int sum = 0, first_prime = 0;
        boolean first_prime_find = false;

        for (int i = A; i <= B; i++) {
            boolean isPrime = true;
            if (i < 2) { 
                continue;
            }
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                sum += i;
                if (first_prime_find == false) {
                    first_prime = i;
                    first_prime_find = true;
                }
            }
        }
        if (sum == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sum);
            System.out.println(first_prime);
        }
    }
}
