import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int[] a = new int[27];
        for(int i = 0; i < str.length(); i++){
            int index = str.charAt(i) - 'A';
            a[index] ++;
        }

        int solo = 0;
        for (int i = 0; i<a.length; i++){
            if ( a[i] % 2 != 0) {
                solo++;
            }
        }

        String ans = "";
        StringBuilder sb = new StringBuilder();

        if(solo>1){
            ans += "I'm Sorry Hansoo";
        }else {
            for(int i = 0; i < a.length ; i++){
                for (int k = 0; k< a[i]/2 ; k++){
                    sb.append((char)(i+65));
                }
            }

            ans += sb.toString();
            String ops = sb.reverse().toString();

            sb = new StringBuilder();
            for(int i = 0; i< a.length; i++){
                if ( a[i] % 2 == 1){
                    sb.append((char)(i+65));
                }
            }

            ans += sb.toString()+ops;
        }
        System.out.println(ans);
    }
}
