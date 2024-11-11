import java.util.*;
import java.io.*;
public class Boj21568 {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int gcd = makeGcd(a,b);

        if(c%gcd!=0){
            System.out.print(-1);
        }
        else{
            int mok = c/gcd;
            long[] ret = Euclid(a,b);
            System.out.println(ret[0]*mok + " " + ret[1]*mok);
        }
    }

    public static long [] Euclid(long a, long b){
        long[] ret = new long[2];
        if(b==0){
            ret[0]=1; ret[1]=0;
            return ret;
        }
        long q = a/b;
        long[] v = Euclid(b, a%b);
        ret[0] = v[1];
        ret[1] = v[0] - v[1]*q;
        return ret;
    }
    public static int makeGcd(int a, int b){
        if (b==0){
            return a;
        }
        else{
            return makeGcd(b, a%b);
        }
    }
}
