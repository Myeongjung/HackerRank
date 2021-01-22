// 15. Java Substring
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();

        System.out.println(S.substring(start,end));
    }
}

// 16. Java Substring Comparisons
public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        smallest = s.substring(0,k);
        largest = s.substring(0,k);
        for(int i = 1; i < s.length()-k+1 ; i++){
            if(s.substring(i,k+i).compareTo(smallest) < 0){
                smallest = s.substring(i,k+i);
            } else if (s.substring(i,k+i).compareTo(largest) > 0) {
                largest = s.substring(i,k+i);
            }
        }
        
        return smallest + "\n" + largest;
}

// 17. Java String Reverse
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        System.out.println(A.equals(new StringBuilder(A).reverse().toString())?"Yes":"No");
    }
}

// 18. Java Anagrams
static boolean isAnagram(String a, String b) {
	a = a.toLowerCase();
	b = b.toLowerCase();

	if(a.length() != b.length()) {
		return false;
	}

	int count[] = new int[26];
	
	for (int i = 0; i < a.length(); i++) {
		int index;
		index = a.charAt(i) - 97;
		count[index]++;
		
		index = b.charAt(i) - 97;
		count[index]--;
	}
	for (int i = 0; i < 26; i++) {
		if (count[i] != 0) {
			return false;
		}
	}
	return true;
}

// 19. Java String Tokens
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();

        if(s.length()>0) {
            String[] parts = s.split("[ !,?._'@]+");
            System.out.println(parts.length);

            for(int i = 0; i<parts.length ; i++){
                System.out.println(parts[i]);
            }
        }else {
            System.out.println(0);
        }
        scan.close();
    }
}

// 20. Pattern Syntax Checker
import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
    
            try {
                Pattern.compile(pattern);
                System.out.println("Valid");
            }catch(PatternSyntaxException e){
                System.out.println("Invalid");
            }
            testCases--;
		}
	}
}

// 21. Valid Username Regular Expression
class UsernameValidator {
    public static final String regularExpression = "^[a-zA-Z]\\w{7,29}";
}

// 22. Java Primality Test
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
        String n = scanner.nextLine();
        scanner.close();

        BigInteger b = new BigInteger(n);

        System.out.println(b.isProbablePrime(1)?"prime":"not prime");
    }
}

// 23. Java BigInteger
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger a = new BigInteger(scan.next());
        BigInteger b = new BigInteger(scan.next());
        System.out.println(a.add(b));
        System.out.println(a.multiply(b));
    }
}

// 24. Java 1D Array
int [] a = new int [n];
for (int i = 0; i < n ; i++) {
	a[i] = scan.nextInt();
}
		
// 25. Java 2D Array
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
        int[][] a = new int[6][6];
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                a[i][j] = arrItem;

                if(i > 1 && j > 1) {
                    int sum = 
                        a[i][j]
                        + a[i][j-1]
                        + a[i][j-2]
                        + a[i-1][j-1]
                        + a[i-2][j]
                        + a[i-2][j-1]
                        + a[i-2][j-2];
                    if(sum > max){max = sum;}
                }
            }
        }
        System.out.println(max);
        scanner.close();
    }
}

// 26. Java Subarray
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int [] a = new int[n];
        int count = 0;

        for(int i = 0; i < n ; i++) {
            a[i] = scan.nextInt();
        }

        for(int i = 0; i < n ; i++) {
            int sum = 0;
            for(int j = i; j<n ; j++) {
                sum = sum + a[j];
                if(sum <0) {count++;}
            }
        }

        System.out.println(count);
    }
}

// 27. Java Arraylist
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList <int[]> a = new ArrayList();
        for (int i = 0; i < n ; i++) {
            int an = scan.nextInt();
            int [] arr = new int[an];
            for (int j = 0; j < an ; j++) {
                arr[j] = scan.nextInt();
            }
            a.add(arr);
        }
        n = scan.nextInt();
        for (int i = 0; i < n ; i++) {
            int index = scan.nextInt();
            int value = scan.nextInt();
            System.out.println(a.get(index-1).length >= value ?a.get(index-1)[value-1]:"ERROR!");
        }
    }
}

// 28. Java List
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList <Integer> li = new ArrayList<>();

        for(int i = 0; i< n ; i++) {
            int value = scan.nextInt();
            li.add(value);
        }
        n = scan.nextInt();
        for(int i = 0; i< n ; i++) {
            String q = scan.next();
            int index = scan.nextInt();
            if (q.equals("Insert")) {
                int value = scan.nextInt();
                li.add(index, value);
            }else {
                li.remove(index);
            }
        }
        scan.close();

        for (Integer num : li) {
            System.out.print(num + " ");
        }
       
    }
}