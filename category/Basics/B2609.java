// import java.util.*;
// import java.math.*;


// public class B2609 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int a, b; 
//         a = sc.nextInt();
//         b = sc.nextInt();
//         int min = Math.min(a, b), max = Math.max(a, b);
//         int gcd = 1, lcm = a * b;
        
//         // gcd
//         for (int i = 2; i < min; i++) {
//             if (a >= i && b >= i){
//                 if (a % i == 0 && b % i == 0) {
//                     gcd = i;
//                 }
//             }
//         }
//         // lcm
//         for (int i = min; i < a * b; i += min) {
//             if (i % max == 0) {
//                 lcm = i;
//                 break;
//             }
//         }
//         System.out.println(gcd);
//         System.out.println(lcm);
//     }
// }

import java.util.*;

public class B2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b; 
        a = sc.nextInt();
        b = sc.nextInt();
        
        int gcd = gcd(a, b);
        int lcm = lcm(a, b, gcd);
        
        System.out.println(gcd);
        System.out.println(lcm);
        sc.close();
    }
    
    // 최대공약수 계산
    static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
    
    // 최소공배수 계산
    static int lcm(int a, int b, int gcd) {
        return (a * b) / gcd;
    }
}
