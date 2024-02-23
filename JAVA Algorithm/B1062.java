import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1062 {
    static int[] words;
    static int maxWords = 0;
    static int n, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        words = new int[n];

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            for (int j = 0; j < word.length(); j++) {
                words[i] |= (1 << (word.charAt(j) - 'a'));
            }
        }

        findMaxReadableWords(0, 0);

        System.out.println(maxWords);
    }

    static void findMaxReadableWords(int start, int learned) {
        if (Integer.bitCount(learned) == k) {
            int count = 0;
            for (int word : words) {
                if ((word & learned) == word) {
                    count++;
                }
            }
            maxWords = Math.max(maxWords, count);
            return;
        }

        for (int i = start; i < 26; i++) {
            if ((learned & (1 << i)) == 0) {
                findMaxReadableWords(i + 1, learned | (1 << i));
            }
        }
    }
}


// import java.util.*;
 
// public class Main {
 
//     static int n, k;
//     static int max = Integer.MIN_VALUE;
//     static boolean[] visited;
//     static String[] word;
    
//     public static void main(String[] args) {
//         Scanner scan = new Scanner(System.in);
 
//         n = scan.nextInt();
//         k = scan.nextInt();
        
//         scan.nextLine();
//         word = new String[n];
//         for(int i = 0; i < n; i++) {
//             String str = scan.nextLine();
//             str = str.replace("anta", "");
//             str = str.replace("tica", "");
//             word[i] = str;
//         }
        
//         if(k < 5) { //a c i n t의 개수가 5개이므로
//             System.out.println("0");
//             return;
//         } else if(k == 26) { //모든 알파벳을 다 읽을 수 있다.
//             System.out.println(n);
//             return;
//         }
        
//         visited = new boolean[26]; //각 알파벳을 배웠는지 체크
//         visited['a' - 'a'] = true;
//         visited['c' - 'a'] = true;
//         visited['i' - 'a'] = true;
//         visited['n' - 'a'] = true;
//         visited['t' - 'a'] = true;
        
//         backtracking(0, 0);
//         System.out.println(max);
//     }
    
//     public static void backtracking(int alpha, int len) {
//         if(len == k - 5) {
//             int count = 0;
//             for(int i = 0; i < n; i++) { //뽑은 알파벳으로 몇개의 단어를 읽을 수 있는지 카운트.
//                 boolean read = true;
//                 for(int j = 0; j < word[i].length(); j++) {
//                     if(!visited[word[i].charAt(j) - 'a']) {
//                         read = false;
//                         break;
//                     }
//                 }
//                 if(read) count++;
//             }
//             max = Math.max(max, count);
//             return;
//         }
        
//         for(int i = alpha; i < 26; i++) {
//             if(visited[i] == false) {
//                 visited[i] = true;
//                 backtracking(i, len + 1);
//                 visited[i] = false;
//             }
//         }
//     }
// }