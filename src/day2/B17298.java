package day2;


import java.util.*;
import java.io.*;
public class B17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        Stack<Integer> stack = new Stack<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        switch (M) {
            case 1:
                for (int i = 0; i < N; i++) {
                    while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
                        arr[stack.pop()] = arr[i];
                    }
                    stack.push(i);
                }

                while (!stack.isEmpty()) {
                    arr[stack.pop()] = -1;
                }

                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < N; i++) {
                    sb.append(arr[i] + " ");
                }
                System.out.println(sb.toString());
                break;
            case 2:
                int target =  arr[N - 1];
                int push = -1;
                stack.push(-1);
//        System.out.println("start/ push: " + push + ", target: " + target);

                for (int i = N - 2; i >= 0; i--) {
//            System.out.println("i: " + i + " arr[i]: " + arr[i] +  " push: " + push + ", target: " + target);
                    if (i == 0) {
                        if (arr[i] <= target) {
                            stack.push(target);
                        }
                        else
                            stack.push(-1);
                        break;
                    }



                    if (arr[i] < target) {
                        push = target;
                    }
                    else if (arr[i] >= target) {
                        push = -1;
                    }

                    // 앞 수보다 작다.
//            System.out.println("i: " + i + " arr[i]: " + arr[i] +  " push: " + push + ", target: " + target);
                    if (arr[i] <= arr[i - 1]) {
                        if (arr[i - 1] > target)
                            target = arr[i - 1];
                    }
                    else {
                        target = arr[i];
                    }
//            System.out.println("i: " + i + " arr[i]: " + arr[i] +  " push: " + push + ", target: " + target);
                    stack.push(push);
                }

                StringBuilder sb1 = new StringBuilder();
                for (int i = 0; i < N; i++) {
                    sb1.append(stack.pop() + " ");
                }
                System.out.println(sb1.toString());


        }


    }
}
