

import java.util.Scanner;

public class B2406 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    
        int Max_Passenger = 0;
        int Current_Passenger = 0;
        int riding, quiting;

        for (int i = 0; i < 10; i++) {
            riding = sc.nextInt();
            quiting = sc.nextInt();
            
            Current_Passenger += (riding - quiting);
            
            if (Current_Passenger > 10000) {
                Current_Passenger = 10000;
            }
            if (Current_Passenger < 0) {
                Current_Passenger = 0;
            }
        
            if (Current_Passenger > Max_Passenger) {
                Max_Passenger = Current_Passenger;
            }
        }
        System.out.println(Max_Passenger);
    }
}
