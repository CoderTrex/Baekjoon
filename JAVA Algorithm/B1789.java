import java.util.*;
import java.io.*;

public class B1789 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        long S = Long.parseLong(st.nextToken());
        int i = 0;
        while (S >= 0) {
            i++;
            S -= i;
        }
        System.out.println(i - 1);
    }
}
