package day3;

import java.util.*;
import java.io.*;
public class B16953 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int cnt = 1;

        while (A < B) {
            if (B % 10 == 1) {
                B /= 10;
                cnt++;
            } else if (B % 2 == 0) {
                B /= 2;
                cnt++;
            } else {
                cnt = -1;
                break;
            }
        }

        if (A != B) {
            cnt = -1;
        }
        System.out.println(cnt);
    }
}
