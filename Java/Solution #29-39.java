// 29. Java Map
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh)
    {
        Scanner in = new Scanner(System.in);
        HashMap h = new HashMap();
        int n=in.nextInt();
        in.nextLine();
        for(int i=0;i<n;i++)
        {
            String name=in.nextLine();
            int phone=in.nextInt();
            in.nextLine();
            h.put(name,phone);
        }
        while(in.hasNext())
        {
            String s=in.nextLine();
            if(h.get(s) != null){
                System.out.println(s+"="+h.get(s));
            }else {
                System.out.println("Not found");
            }
        }
    }
}

// 30. Java Hashset
HashSet h = new HashSet();
for (int i = 0 ; i < t ; i++) {
	h.add(pair_left[i] + " " + pair_right[i]);
	System.out.println(h.size());
}

// 31. Java Generics
class Printer<T>
{  
    public void printArray(T[] arr) {
       for (Object obj : arr) {
           System.out.println(obj);  
       }
    } 
}

// 32. Java Sort
import java.util.*;

class Student{
    private int id;
    private String fname;
    private double cgpa;
    public Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }
    public int getId() {
        return id;
    }
    public String getFname() {
        return fname;
    }
    public double getCgpa() {
        return cgpa;
    }
}

//Complete the code
public class Solution
{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        
        List<Student> studentList = new ArrayList<Student>();
        while(testCases>0){
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();
            
            Student st = new Student(id, fname, cgpa);
            studentList.add(st);
            
            testCases--;
        }

        Collections.sort(studentList, new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                if (s1.getCgpa() == s2.getCgpa()) {
                    if (s1.getFname().compareTo(s2.getFname()) == 0) {
                        return s1.getId() - s2.getId();
                    } else {
                        return s1.getFname().compareTo(s2.getFname());
                    }
                } else if (s1.getCgpa()>s2.getCgpa()) { return -1; }
                else return 1; 
            }
        });
      
          for(Student st: studentList){
            System.out.println(st.getFname());
        }
    }
}

// 33. Java BitSet
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        String op;
        int x,y;

        BitSet b1 = new BitSet(n);
        BitSet b2 = new BitSet(n);
        BitSet[] bitset = new BitSet[3];
      
        bitset[1] = b1;
        bitset[2] = b2;

        for(int i = 0 ; i<m ; i ++) {
            op = scan.next();
            x = scan.nextInt();
            y = scan.nextInt();

            switch (op) {
                case "AND":
                bitset[x].and(bitset[y]);
                break;
                case "OR":
                bitset[x].or(bitset[y]);
                break;
                case "XOR":
                bitset[x].xor(bitset[y]);
                break;
                case "FLIP":
                bitset[x].flip(y);
                break;
                case "SET":
                bitset[x].set(y);
            }
            System.out.printf("%d %d%n", b1.cardinality(), b2.cardinality());
        }
        scan.close();
    }
}

// 34. Java Inheritance I
class Bird extends Animal
{
    void fly(){
        System.out.println("I am flying");
    }

    void sing(){
        System.out.println("I am singing");
    }
}
// 35. Java Inheritance II
class Arithmetic {
    int add(int a, int b) {
        return (a+b);
    }
}

class Adder extends Arithmetic{
    
}

// 36. Java Abstract Class
class MyBook extends Book {
    void setTitle(String s) {
        this.title = s;
    }
}

// 37. Java Interface
class MyCalculator implements AdvancedArithmetic {
    int result = 0;
    public int divisor_sum(int n) {
        for(int i = 1 ; i <= n ; i++) {
            if(n%i == 0) {
                this.result += i;
            }
        }
        return this.result;
    }
}

// 38. Java Method Overriding
@Override
void getNumberOfTeamMembers(){
	System.out.println( "Each team has 11 players in " + getName() );
}

// 39. Java Method Overriding 2 (Super Keyword)
String temp=super.define_me();