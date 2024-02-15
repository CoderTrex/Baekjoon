
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class B10818{
    
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int count = sc.nextInt();
            ArrayList<Integer> list = new ArrayList<>(count);
            
            for (int i = 0; i < count; i++) {
                list.add(sc.nextInt());
            }
            sc.close();
            Collections.sort(list);
            System.out.println(list.get(0) + " " + list.get(list.size() - 1));
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}