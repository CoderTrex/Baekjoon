package day2;

import  java.util.*;
import  java.io.*;

public class B1541 {
    public static void main(String[] args) throws  IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String[] arr = st.nextToken().split("-");
        String plus = arr[0];
        String[] minus = new String[arr.length - 1];

        int sum  = paserInt(plus);
        for (int i = 1; i < arr.length; i++) {
           sum -= paserInt(arr[i]);
        }
        System.out.println(sum);
    }

    public static int paserInt(String s) {
        int sum = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '+') {
                sum += Integer.parseInt(s.substring(0, i));
                s = s.substring(i + 1);
                i = 0;
            }
            if (i == s.length() - 1) {
                sum += Integer.parseInt(s);
            }
        }
        return sum;
    }
}
