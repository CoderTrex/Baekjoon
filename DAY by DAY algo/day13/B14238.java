//package day13;
//
//import java.io.*;
//import java.util.*;
//
//public class B14238 {
//
//    // A는 출근을 매일할 수 있음
//    // B는 출근한 다음날을 무조건 쉬어야함.
//    // C는 출근한 다음날과 다다음날을 무조건 쉬어야함.
//
//    public static boolean flag = false;
//    public static Vector<String> visited = new Vector<>();
//    public static int s_len;
//
//    public static void main(String[] main) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        String s = st.nextToken();
//        s_len = s.length();
//        int[] count = new int[3];
//
//        for (int i = 0; i < s.length(); i++) {
//            if (s.charAt(i) == 'A') count[0]++;
//            else if (s.charAt(i) == 'B') count[1]++;
//            else count[2]++;
//        }
//
//        dfs(s, count, 0, new Vector<>());
//        if (!flag) System.out.println(-1);
//    }
//    public static void dfs(String s, int[] count, int day, Vector<Character> list) {
////        System.out.println("day: " + day + " list: " + list);
//        if (day == s.length()) {
//            if (list.size() == s.length()) {
//                for (char c : list) {
//                    System.out.print(c);
//                    flag = true;
//                }
//            }
//        }
//
//        if (flag) return;
//        if (visited.contains(list.toString()))
//            return;
//        visited.add(list.toString());
//
//
//        for (int i = 2; i >= 0; i--) {
//            // 출근 가능한 날이 없으면 continue
//            if (count[i] == 0) continue;
//
//            Vector<Character> newList = new Vector<>(list); // 새로운 Vector 객체 생성
//
//            // 출근 가능한 날이 있을 경우
//            // case1. C출근 전날과 전전날 출근이 없는 경우만 출근 가능
//            if (i == 2 && count[2] > 0 && count[1] < s_len - day - 1 && (list.get(i - 1) == 'B' || list.get(i - 1) == 'A')) {
//                if (day == 0) {
//                    newList.add('C');
//                    dfs(s, new int[]{count[0], count[1], count[2] - 1}, day + 1, newList);
//                } else if (day == 1) {
//                    if (list.get(day - 1) != 'C') {
//                        newList.add('C');
//                        dfs(s, new int[]{count[0], count[1], count[2] - 1}, day + 1, newList);
//                    }
//                } else {
//                    if (list.get(day - 1) != 'C' && list.get(day - 2) != 'C') {
//                        newList.add('C');
//                        dfs(s, new int[]{count[0], count[1], count[2] - 1}, day + 1, newList);
//                    }
//                }
//            }
//            // case2. B출근 전날 출근이 없는 경우만 출근 가능
//            if (i == 1 && count[1] > 0) {
//                if (day == 0) {
//                    newList.add('B');
//                    dfs(s, new int[]{count[0], count[1] - 1, count[2]}, day + 1, newList);
//                } else {
//                    if (list.get(day - 1) != 'B') {
//                        newList.add('B');
//                        dfs(s, new int[]{count[0], count[1] - 1, count[2]}, day + 1, newList);
//                    }
//                }
//            }
//            // case3. A출근 전날 출근과 상관 없이 출근이 가능
//            if (i == 0 && count[0] > 0) {
//                newList.add('A');
//                dfs(s, new int[]{count[0] - 1, count[1], count[2]}, day + 1, newList);
//            }
//        }
//    }
//}
//

package day13;

import java.io.*;

public class B14238 {
    static int[][][][][] dp;
    static boolean flag = false;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new  BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int a_cnt = 0;
        int b_cnt = 0;
        int c_cnt = 0;

        for(int i=0; i<input.length(); i++) {
            if(input.charAt(i)=='A')
                a_cnt++;

            else if(input.charAt(i)=='B')
                b_cnt++;

            else
                c_cnt++;
        }
        dp = new int[a_cnt+1][b_cnt+1][c_cnt+1][3][3];

        dfs(a_cnt, b_cnt, c_cnt, "", 0, 0);

        if(!flag)
            System.out.println(-1);
    }

    public static void dfs(int a, int b, int c, String s, int pre2, int pre) {
        if(flag) return;

        if(a==0 && b==0 && c==0) {
            System.out.println(s);
            flag = true;
            return;
        }

        if(dp[a][b][c][pre2][pre]==1) return;

        dp[a][b][c][pre2][pre] = 1;

        if(a>0)
            dfs(a-1, b, c, s+'A', pre, 0);

        if(b>0 && pre!=1)
            dfs(a, b-1, c, s+'B', pre, 1);

        if(c>0 && pre!=2 && pre2!=2)
            dfs(a, b, c-1,s+'C', pre, 2);
    }
}
