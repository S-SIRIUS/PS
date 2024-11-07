import java.util.*;
public class Sum {
    public static void main(String [] args){
        String num;
        int n;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        num = scanner.next();
        char [] charry = num.toCharArray();
        int summ=0;
        for(char c: charry){
            summ+=Integer.parseInt(String.valueOf(c));
        }
        System.out.println(summ);
    }
}