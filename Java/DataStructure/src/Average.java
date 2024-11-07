import java.util.*;
public class Average {
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        int n;
        n = scanner.nextInt();
        int max=0;
        int [] scores = new int[n];
        for(int i=0; i<n; i++){
            int score= scanner.nextInt();
            scores[i] = score;
            if (score > max){
                max = score;
            }
        }
        double  sum=0;
        for(int i=0; i<n; i++){
            sum += (double)scores[i]/max*100;
        }
        System.out.println(sum/n);

    }
}
