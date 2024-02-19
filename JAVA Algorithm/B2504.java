import java.util.*;

public class B2504 {

    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        String sentence = sc.nextLine();
        int A_flag = 0, B_flag  = 0;
        boolean okay = true;  
        

        for (int i = 0; i < sentence.length(); i++) {
            if (A_flag < 0 || B_flag < 0) {
                okay = false;
                break;
            }
            
            if (sentence.charAt(i) == '(') {
                A_flag++;
            }
            else if (sentence.charAt(i) == ')') {
                A_flag--;
            }
            else if (sentence.charAt(i) == '[') {
                B_flag++;
            }
            else if (sentence.charAt(i) == ']') {
                B_flag--;
            }
        }
        if (!okay || A_flag != 0 || B_flag != 0){
            System.out.println(0);
        }
    }
}