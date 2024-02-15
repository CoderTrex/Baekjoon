

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Vector;

public class B3460 {
    public static void recr(int num , Vector<Integer> v) {
        if (num > 0) {
            v.add(num % 2);
            recr(num / 2, v);
        }
    }

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Vector<Integer> v = new Vector<Integer>();
        int count, num; 

        try {
            count = Integer.parseInt(br.readLine());
            
            for (int i = 0; i < count; i++) {
                num = Integer.parseInt(br.readLine());
                recr(num, v);
                for (int j = 0; j < v.size(); j++) {
                    if (v.get(j) == 1) {
                        System.out.print(j);
                        if (j != v.size() - 1) {
                            System.out.print(" ");
                        } else {
                            System.out.println();
                        }
                    }
                }
                v.clear();
            }

        } catch (NumberFormatException | IOException e) {
            System.out.println("Invalid input or error reading input. Please enter a valid integer.");
        }
    }
}
