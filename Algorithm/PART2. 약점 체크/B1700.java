// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.ArrayList;
// import java.util.List;
// import java.util.StringTokenizer;

// public class BOJ1700 {
//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         int n = Integer.parseInt(st.nextToken());
//         int k = Integer.parseInt(st.nextToken());
//         st = new StringTokenizer(br.readLine());
//         List<Integer> orders = new ArrayList<>();
//         List<Integer> multitap = new ArrayList<>();
//         int answer = 0;
//         for(int i = 0; i<k; i++){
//             orders.add(Integer.parseInt(st.nextToken()));
//         }
//         while(!orders.isEmpty()){
//             int order = orders.remove(0);
//             // 멀티탭에서 이미 사용중인 경우
//             if(multitap.contains(order)) continue;
//             // 멀티탭에 자리가 있는 경우
//             if(multitap.size() < n){
//                 multitap.add(order);
//             } else {
//             // 멀티탭에 자리가 없는 경우
//                 boolean flag = false;
//                 int idx = -1;
//                 int maxIdx = -1;
//                 answer++;
//                 for(int i = 0; i<multitap.size(); i++){
//                     if(!orders.contains(multitap.get(i))){
//                         // 다시 사용하지 않을 전자기기인 경우
//                         flag = true;
//                         multitap.remove(i);
//                         multitap.add(order);
//                         break;
//                     } else {
//                         if(orders.indexOf(multitap.get(i))> idx){
//                         // 다시 사용할 전자기기의 우선순위를 계산
//                             idx = orders.indexOf(multitap.get(i));
//                             maxIdx = i;
//                         }
//                     }
//                 }
//                 if(!flag){
//                     // 모든 전자기기가 다시 사용할 전자기기인 경우
//                     // 계산한 우선순위를 이용해서 해결
//                     multitap.remove(maxIdx);
//                     multitap.add(order);
//                 }
//             }
//         }
//         System.out.println(answer);
//     }
// }

import java.util.*;

public class B1700 {
    public static int N, K;
    public static int min = Integer.MAX_VALUE;

    public static void main (String[] arg) {
        Scanner sc = new Scanner(System.in);
        N= sc.nextInt();
        K = sc.nextInt();
        int[] arr = new int[K];
        boolean[] visited = new boolean[K];


        for (int i = 0; i < K; i++) {
            arr[i] = sc.nextInt();
            visited[i] = false;
        }
        sc.close();
        dfs(arr, visited, 0, 0);
        System.out.println(min);
    }

    public static void dfs (int[] arr, boolean[] visited, int num, int count) {
        if (num == K) {
            min = Math.min(min, count);
            return;
        }
        
        if (num < N) {
            visited[arr[num]] = true;
            dfs(arr, visited, num + 1, count);
        }
        else {
            for (int i = 0; i < K; i++) {
                if (visited[i] == true) {

                    visited[i] = false;
                    visited[arr[num]] = true;
                    
                    dfs(arr, visited, num + 1, count + 1);
                    
                    visited[i] = true;
                    visited[arr[num]] = false;
                }
            }
        }
    }
}

