import java.util.*;
import java.io.*;

public class B3085 {
    public static int N;
    public static int max_col, max_row;
    public static char[][] board;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        max_col = 1; 
        max_row = 1; 
        board = new char[N][N];
        
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = s.charAt(j);
            }
        }

        for (int q = 0;  q < N; q++) {
            for (int p = 0; p < N - 1; p++) {
                char temp = board[q][p];
                board[q][p] = board[q][p + 1];
                board[q][p + 1] = temp;
                cal_max();
                temp = board[q][p];
                board[q][p] = board[q][p + 1];
                board[q][p + 1] = temp;

                temp = board[p][q];
                board[p][q] = board[p + 1][q];
                board[p + 1][q] = temp;
                cal_max();                
                temp = board[p][q];
                board[p][q] = board[p + 1][q];
                board[p + 1][q] = temp;
            }
        }
        System.out.println(Math.max(max_col, max_row));
    }
    
    public static void cal_max() {
        for (int i = 0; i < N; i++) {
            char row = board[i][0]; // 가로
            char col = board[0][i]; // 세로
            int colCnt = 1, rowCnt = 1;
            for (int j = 1; j < N; j++) {
                if (row == board[i][j]) {
                    colCnt++;
                } else {
                    max_col = Math.max(max_col, colCnt);
                    row = board[i][j];
                    colCnt = 1;
                }
                
                if (col == board[j][i]) {
                    rowCnt++;
                } else {
                    max_row = Math.max(max_row, rowCnt);
                    col = board[j][i];
                    rowCnt = 1;
                }
            }
            max_col = Math.max(max_col, colCnt);
            max_row = Math.max(max_row, rowCnt);
        }
    }
}