import java.util.*;
import java.io.*;
public class Boj11689 {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        long result = n;

        for(long i=2; i<=Math.sqrt(n); i++){
            if(n%i==0){
                result = result -(result/i);
                while(n%i==0){
                    n /=i;
                }
            }
        }
        if(n>1){
            result = result - (result/n);
        }
        System.out.print(result);
    }
}
