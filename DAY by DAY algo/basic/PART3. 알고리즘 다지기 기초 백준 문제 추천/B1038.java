import java.util.*;
import java.io.*;

public class B1038 {
    static ArrayList<Long> list;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        list = new ArrayList<>();
        if (N < 10) {
            System.out.println(N);
        }
        else if (N > 1022) {
            System.out.println(-1);
        }
        else {
            for (int i = 0; i < 10; i++) {
                bp(i, 1);
            }
            Collections.sort(list);
            System.out.println(list.get(N));
        }
    }
    public static void bp (long number, int depth) {
        if (depth > 10) {
            return;
        }
        list.add(number);
        for (int i = 0; i < 10; i++) {
            if (number % 10 > i) {
                bp(number * 10 + i, depth + 1);
            }
        }
    }
}
