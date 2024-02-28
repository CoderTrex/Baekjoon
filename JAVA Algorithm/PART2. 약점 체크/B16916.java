import java.io.*;

public class B16916 {
    public static int ans, pi[];
    public static String all, pattern;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        all = br.readLine();
        pattern = br.readLine();
        pi = new int[pattern.length()]; // 패턴의 길이만큼 pi 배열 생성

        getPi();
        kmp();
        System.out.println(ans);
    }


    // 특정 길이 만큼 갔을 때 해당 위치에서는 얼마나 이동해야 하는지를 저장하는 배열 만든다.
    public static void getPi() {
        int j = 0;
        // 패턴의 길이만큼 반복
        for (int i = 1; i < pattern.length(); i++) {
            // j가 0보다 크고, 패턴의 i번째와 j번째가 다를 때
            while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
                j = pi[j - 1]; // j를 이전의 j번째로 이동
            }
            // 패턴의 i번째와 j번째가 같을 때
            if (pattern.charAt(i) == pattern.charAt(j)) {
                pi[i] = ++j; // pi[i]에 j+1을 저장하고 j를 증가
            }
        }
    }

    public static void kmp() {
        int j = 0;
        for (int i = 0; i < all.length(); i++) {
            while (j > 0 && all.charAt(i) != pattern.charAt(j)) {
                j = pi[j - 1];
            }
            if (all.charAt(i) == pattern.charAt(j)) {
                if (j == pattern.length() - 1) {
                    ans = 1;
                    return;
                } else {
                    j++;
                }
            }
        }
    
    }
}

// import java.io.*;

// public class B16916 {
    
//     public static int getPattern(String s) {
//         int mark = s.length();
//         int i = 0;
//         for (i = 0; i < mark; i++) {
//             if (s.charAt(i) != s.charAt(mark - 1)) {
//                 break;
//             }
//             mark--;
//         }
//         return i;
//     }
//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         String s = br.readLine();
//         String p = br.readLine();

//         int len = getPattern(s);
//         for (int i = 0; i <= s.length() - p.length(); i++) { // i의 범위를 조정하여 문자열을 넘어가지 않도록 함
//             if (s.charAt(i) == p.charAt(0)) {
//                 int j = 0;
//                 for (j = 0; j < p.length(); j++) {
//                     if (s.charAt(i + j) != p.charAt(j)) {
//                         i += len;
//                         break;
//                     }
//                 }
//                 if (j == p.length()) {
//                     System.out.println(1);
//                     return;
//                 }
//             }
//         }
        
//         System.out.println(0);
//     }
// }


// boolean flag = false;
// int s_len = s.length(), i = 0;
// while (s_len > i + p.length() - 1) {
//     if (s.charAt(i) == p.charAt(0)) {
//         for (int j = 0; j < p.length(); j++) {
//             if (s.charAt(i + j) != p.charAt(j)) {
//                 flag = false;
//                 break;
//             }
//             flag = true;
//         }
//         if (flag) {
//             System.out.println(1);
//             return;
//         }
//     }
//     i++;
// }
// System.out.println(0);
// return ;