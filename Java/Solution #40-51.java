// 40. Java Instanceof keyword
import java.util.*;


class Student{}
class Rockstar{}
class Hacker{}

public class InstanceOFTutorial{
	
   static String count(ArrayList mylist){
      int a = 0,b = 0,c = 0;
      for(int i = 0; i < mylist.size(); i++){
         Object element=mylist.get(i);
         if(element instanceof Student)
            a++;
         if(element instanceof Rockstar)
            b++;
         if(element instanceof Hacker)
            c++;
      }
      String ret = Integer.toString(a)+" "+ Integer.toString(b)+" "+ Integer.toString(c);
      return ret;
   }

   public static void main(String []args){
      ArrayList mylist = new ArrayList();
      Scanner sc = new Scanner(System.in);
      int t = sc.nextInt();
      for(int i=0; i<t; i++){
         String s=sc.next();
         if(s.equals("Student"))mylist.add(new Student());
         if(s.equals("Rockstar"))mylist.add(new Rockstar());
         if(s.equals("Hacker"))mylist.add(new Hacker());
      }
      System.out.println(count(mylist));
   }
}

// 41. Java Iterator
Object element = it.next();
if(element instanceof String)

// 42. Java Exception Handling (Try-catch)
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try{
            int a = scan.nextInt();
            int b = scan.nextInt();
            System.out.println(a/b);
        }catch (InputMismatchException e){
            System.out.println("java.util.InputMismatchException");
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
}

// 43. Java Exception Handling
class MyCalculator {
    long power(int n, int p) throws Exception {
        if(n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        }else if(n<0 || p<0) {
            throw new Exception("n or p should not be negative.");
        }
        return (long)Math.pow(n,p);
    }
}

// 44. Java Varargs - Simple Addition
class Add {
    void add (int... ints) {
        int result = 0;
        String str = "";
        for (int i : ints) {
            str += String.valueOf(i)+"+";
            result += i;
        }
        System.out.println(str.substring(0,str.length()-1)+"="+result);
    }
}

// 45. Java Reflection - Attributes
public class Solution {
        public static void main(String[] args){
            Class student = Student.class;
            Method[] methods = student.getDeclaredMethods();

            ArrayList<String> methodList = new ArrayList<>();
            for(Method m : methods){
                methodList.add(m.getName());
            }
            Collections.sort(methodList);
            for(String name: methodList){
                System.out.println(name);
            }
        }
}
	
// 46. Java Factory Pattern
if (order.equals("cake")) {
    return new Cake();
}
else if (order.equals("pizza")) {
    return new Pizza();
}
else {
    return null;
}

// 47. Java Singleton Pattern
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

class Singleton {
    private Singleton() {}
    public String str;
    private static Singleton instance = new Singleton();
    public static Singleton getSingleInstance() { return instance; }
}

// 48. Covariant Return Types
class Flower {
    public String whatsYourName() {
        return "I have many names and types";
    }
}

class Jasmine extends Flower {
    @Override 
    public String whatsYourName() {
        return "Jasmine";
    }    
}

class Lily extends Flower {
    @Override 
    public String whatsYourName() {
        return "Lily";
    }    
}

class Region {
    public Flower yourNationalFlower() {
        return new Flower();
    }
}

class WestBengal extends Region {
    @Override 
    public Jasmine yourNationalFlower() {
        return new Jasmine();
    }
}

class AndhraPradesh extends Region {
    @Override 
    public Lily yourNationalFlower() {
        return new Lily();
    }
}

// 49. Java Regex
class MyRegex{
    String zeroTo255 = "(\\d{1,2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])";
    public String pattern = zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255;
}

// 50. Java Regex 2 - Duplicate Words
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DuplicateWords {

    public static void main(String[] args) {

        String regex = "\\b(\\w+)(\\s+\\1\\b)*";
        Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);

        Scanner in = new Scanner(System.in);
        int numSentences = Integer.parseInt(in.nextLine());
        
        while (numSentences-- > 0) {
            String input = in.nextLine();
            
            Matcher m = p.matcher(input);
            
            // Check for subsequences of input that match the compiled pattern
            while (m.find()) {
                input = input.replaceAll(m.group(),m.group(1));
            }
            
            // Prints the modified sentence.
            System.out.println(input);
        }
        
        in.close();
    }
}

// 51. Tag Content Extractor
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int testCases = Integer.parseInt(scan.nextLine());
        
        while (testCases-- > 0) {
            String line = scan.nextLine();
            
            boolean matchFound = false;
            Pattern r = Pattern.compile("<(.+)>([^<]+)</\\1>");
            Matcher m = r.matcher(line);

            while (m.find()) {
                System.out.println(m.group(2));
                matchFound = true;
            }
            if ( ! matchFound) {
                System.out.println("None");
            }
        }
    }
}
