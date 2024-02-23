import java.util.*;

public class B14719 {
    public static Scanner sc = new Scanner(System.in);
    public static int[] arr_height;
    public static int H, W, result = 0;
    public static void main(String[] args) {
        H = sc.nextInt();
        W = sc.nextInt();
        arr_height = new int[W];
        
        for (int i = 0; i < W; i++) {
            arr_height[i] = sc.nextInt();
        }
        for (int i = 0; i < W - 1; i++) {
            int cur   = arr_height[i];
            int left  = cur;
            int right = cur;
            
            for (int k = i - 1; k >= 0; k--) {
                if (arr_height[k] > cur) {
                    left = Math.max(arr_height[k], left);
                }
            }
            for (int k = i + 1; k < W; k++) {
                if (arr_height[k] > cur) {
                    right = Math.max(arr_height[k], right);
                }
            }
            if (Math.min(left, right) > cur) {
                result += (Math.min(left, right) - arr_height[i]);
            }
        }
        System.out.println(result);
    }
}
