// 1. Welcome to Java!
public class Solution {

    public static void main(String[] args) {
        System.out.println("Hello, World.");
        System.out.println("Hello, Java.");
    }
}


// 2. Java Stdin and Stdout I
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}

// 3. Java Stdin and Stdout II
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}

// 4. Java If-Else
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();

        
        if (N%2 != 0) {
            System.out.println("Weird");
        }else if (N > 20) {
            System.out.println("Not Weird");
        }else if (2<=N && N<=5) {
            System.out.println("Not Weird");
        }else if (6<=N && N<=20) {
            System.out.println("Weird");
        }
    }
}	

// 5. Java Output Formatting
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                int count = s1.length();
                for(int j=count;j<15;j++){
                    s1 += " ";
                }
                System.out.println(s1+String.format("%03d", x));
            }
            System.out.println("================================");

    }
}

// 6. Java Loops I
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        for(int i = 0; i< 10 ; i++) {
            System.out.println(String.format("%d x %d = %d",N,i+1,N*(i+1)));
        }
        scanner.close();
    }
}

// 7. Java Loops II
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        int temp =0;
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            for(int j=0; j<n; j++) {
                temp = a+ Recursion(b,j);
                System.out.print(temp + " ");
            }   
            System.out.print("\n");
        }
        in.close();
    }
    static int Recursion(int b, int j) {
        int sum = 0;
        int k = j;
        if(k == 0) {
            sum = b*(int)Math.pow(2,k);
            return sum;
        } else {
            sum = b*(int)Math.pow(2,k);
            k = k-1;
            sum = sum + Recursion(b,k);
            return sum;
        }    
    }
}

// 8. Java Datatypes
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {
            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)System.out.println("* byte");
                if(x>=-(Math.pow(2, 16)/2) && x<=((Math.pow(2, 16)/2)-1))System.out.println("* short");
                if(x>=-(Math.pow(2, 32)/2) && x<=((Math.pow(2, 32)/2)-1))System.out.println("* int");
                if(x>=-(Math.pow(2, 64)/2) && x<=((Math.pow(2, 64)/2)-1))System.out.println("* long");
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}

// 9. Java End-of-file
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i = 1;

        try{
            while(true) {
                String myString = scanner.nextLine();
                System.out.println(i+ " " + myString);
                i++;
            }
        } catch(NoSuchElementException e) {
            scanner.close();
        }
    }
}

// 10. Java Static Initializer Block
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
        public static Scanner scanner = new Scanner(System.in);  
        public static int B = scanner.nextInt();
        public static int H = scanner.nextInt();
        public static boolean flag = false;

        static{ 
            try{
                if(B <= 0 || H<=0) {
                    throw new Exception();
                }else {
                    flag = true;
                }
            }catch (Exception e) {
                System.out.println("java.lang.Exception: Breadth and height must be positive");
            }
        }

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class

// 11. Java Int to String
//String s=???; Complete this line below
	String s = String.valueOf(n);
	
// 12. Java Date and Time
class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        String [] arr = {"SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"};
        try {
            String date = String.valueOf(year) +"-"+ String.format("%02d", month) + "-"+String.format("%02d", day);
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd") ;
            Date nDate = dateFormat.parse(date) ;
            Calendar cal = Calendar.getInstance() ;
            cal.setTime(nDate);
        
            int dayNum = cal.get(Calendar.DAY_OF_WEEK) ;

            return arr[dayNum-1];
        }catch (Exception e) {return new String("");}
    }

}

// 13. Java Currency Formatter
import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        NumberFormat nf = NumberFormat.getCurrencyInstance( Locale.US ); 
        nf.setMaximumFractionDigits(2); 
        String us = nf.format(payment);
        
        nf = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        String india = nf.format(payment);

        nf = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = nf.format(payment);

        nf = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = nf.format(payment);

        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}

// 14. Java Strings Introduction
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        
        
        System.out.println(A.length()+B.length());

        if (A.compareTo(B) > 0){
            System.out.println("Yes");
        }else {
            System.out.println("No");
        }
        String temp = A.substring(0,1).toUpperCase() + A.substring(1) +" " +B.substring(0,1).toUpperCase() + B.substring(1);
        System.out.println(temp);        
    }
}