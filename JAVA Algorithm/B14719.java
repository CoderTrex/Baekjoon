import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B14719 {
    public static Scanner sc = new Scanner(System.in);
    public static int H, W;
    public static int[] arr_height;
    public static int result = 0;

    public static void main(String[] args) {
        H = sc.nextInt();
        W = sc.nextInt();
        arr_height = new int[W];
        
        for (int i = 0; i < W; i++) {
            arr_height[i] = sc.nextInt();
        }

        
    }
}
