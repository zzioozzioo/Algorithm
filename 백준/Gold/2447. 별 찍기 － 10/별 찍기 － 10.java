import java.io.*;
import java.util.Arrays;

public class Main {

    static char[][] starArray;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        starArray = new char[N][N];

        checkStar(0, 0, N, false);

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                sb.append(starArray[i][j]);
            }
            sb.append("\n");
        }
        br.close();
        System.out.println(sb);
    }

    static void checkStar(int x, int y, int N, boolean blank) {

        if (blank) {
            for (int i = x; i < x + N; i++) {
                for (int j = y; j < y + N; j++) {
                    starArray[i][j] = ' ';
                }
            }
            return;
        }

        if(N <= 1){
            starArray[x][y] = '*';
            return;
        }

        int blockSize = N/3;
        int startCount = 0;

        for(int i = x; i < x + N; i+=blockSize){
            for(int j = y; j < y + N;j+=blockSize){
                startCount++;
                if(startCount == 5){
                    checkStar(i, j, blockSize, true);
                }else{
                    checkStar(i, j, blockSize, false);
                }
            }
        }
    }
}