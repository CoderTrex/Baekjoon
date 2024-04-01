package day12;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11722 {

    public  static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] array = new int[n];
        int[] d = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < n ; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        int max = 1;
        d[n - 1] = 1;
        for(int i = n - 2; i >= 0;  i--) {
            if (array[i] > array[i + 1]) {
                d[i] = max;
                max++;
            } else {
                d[i] = 1;
            }
        }
    }
}
