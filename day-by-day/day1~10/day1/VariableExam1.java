package day1;

public class VariableExam1 {// 다양한 변수를 선언하고 아래처럼 출력해주세요.
    class Main1 {
        public static void main(String[] args) {

            // 정수 : int, 실수(소수) : double, 문장 : String
            int i = 100;
            double d = 3.14;
            String s = "안녕하세요";
            System.out.println(i); // 출력 : 100

            System.out.println(d); // 출력 : 3.14

            System.out.println(s); // 출력 : 안녕하세요

            i = 200;
            d = 10.5;
            s = "반갑습니다.";
            System.out.println(i); // 출력 : 200

            System.out.println(d); // 출력 : 10.5

            System.out.println(s); // 출력 : 반갑습니다.


        }
    }

    // 문제 : a와 b가 가지고 있는 값을 서로 뒤바꿔주세요.

    class Main2 {
        public static void main(String[] args) {

            int a = 5;
            int b = 10;

            System.out.println("a : " + a);
            System.out.println("b : " + b);

            // 여기서 부터
            int temp = a;
            a = b;
            b = temp;
            // 여기까지 수정 가능

            System.out.println("a : " + a);
            // 출력 : a : 10
            System.out.println("b : " + b);
            // 출력 :  b : 5
        }
    }




    // 문제 : 실행되는 출력문에는 참 그렇지 않으면 거짓 이라고 적어주세요.

    class Main3 {
        public static void main(String[] args) {

            if ( true ) {
                System.out.println("참");
            }

            if ( false ) {
                System.out.println("거짓");
            }

            int a = 10;
            // `==` => 같다.
            if ( a == 10 ) {
                System.out.println("참");
            }

            // `!=` => 같지 않다.
            if ( a != 10 ) {
                System.out.println("거짓");
            }

            if ( a > 10 ) {
                System.out.println("거짓");
            }

            if ( a >= 10 ) {
                System.out.println("참");
            }

            int b = 10;

            if ( a == b ) {
                System.out.println("참");
            }

            //boolean c => c 에는 오직 true/false 만 담을 수 있다.

            boolean c = a != b; // false;

            if ( c ) {
                System.out.println("거짓");
            }

            if ( c == false ) {
                System.out.println("거짓");
            }

            // `!` => 반전
            if ( !c ) {
                System.out.println("참");
            }

            // `!` => 반전
            if ( !(!c) ) {
                System.out.println("거짓");
            }

            boolean d = true;

            if ( c != d ) {
                System.out.println("거짓");
            }
        }
    }
}
