// 52. Java BigDecimal
for(int i = 0;i<n;i++){
	BigDecimal max = new BigDecimal(s[i]);
	int idx = i;
	for(int j = i+1;j<n;j++)
	{
		BigDecimal curr = new BigDecimal(s[j]);
		if(curr.compareTo(max) == 1){
			max=curr;
			idx=j;
		}
	}
	String temp = s[i];
	s[i] = s[idx];
	s[idx] = temp;
}

// 53. Java 1D Array (Part 2)
import java.util.*;

public class Solution {

    public static boolean canWin(int leap, int[] game, int i) {
        if(i>=game.length)
            return true;

        if(game[i]==0)
        {
            game[i]=1;
            if(canWin(leap,game,i+leap))
                return true;
            if(canWin(leap,game,i+1))
                return true;
            if(i!=0 && canWin(leap,game,i-1))
                return true;
        }
        return false;
    }

    private static boolean isSolvable(int leap, int[] game, int i) {
        // Base Cases
        if (i >= game.length) {
            return true;
        } else if (i < 0 || game[i] == 1) {
            return false;
        }
                
        game[i] = 1; // marks as visited

        // Recursive Cases
        return isSolvable(leap, game, i + leap) || 
            isSolvable(leap, game, i + 1) || 
            isSolvable(leap, game, i - 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game, 0)) ? "YES" : "NO" );
        }
        scan.close();
    }
}

// 54. Java Stack
import java.util.*;
class Solution{
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		Stack<String> stack = new Stack<>();

		while (sc.hasNext()) {
			String input=sc.next();
            String[] array_word;
            array_word = input.split("");
            
            for(int i = 0; i < array_word.length ; i++) {
                if(array_word[i].equals("{") || array_word[i].equals("[") || array_word[i].equals("(")) {
                stack.push(array_word[i]);
            } else if(array_word[i].equals("}")){
                if(!stack.empty()) {
                        if(!stack.peek().equals("{")) {
                            break;
                        }else {
                            stack.pop();
                        }
                    } else {
                        stack.push("!");
                    }
            } else if(array_word[i].equals("]")){
                if(!stack.empty()) {
                        if(!stack.peek().equals("[")) {
                            break;
                        }else {
                            stack.pop();
                        }
                    } else {
                        stack.push("!");
                    }
            } else if(array_word[i].equals(")")){
                    if(!stack.empty()) {
                        if(!stack.peek().equals("(")) {
                            break;
                        }else {
                            stack.pop();
                        }
                    } else {
                        stack.push("!");
                    }
                }  
            }
            
            if(stack.isEmpty()) {
                System.out.println("true");
            } else {
                System.out.println("false");
                stack.clear();
            }
		}
	}
}

// 55. Can You Access?
Inner inner = new Inner();
Inner.Private p = inner.new Private();
o = p;
System.out.println(num + " is " + p.powerof2(num));

// 56. Prime Checker
class Prime {
    void checkPrime(int ... n) {
        for(int i=0;i<n.length;i++)
        {
            boolean flag=false;
            for(int j=2;j<=Math.sqrt(n[i]);j++)
            {
                if(n[i]%j==0)
                {
                    flag=true;
                    break;
                }
            }
            if((!flag||n[i]==2)&&n[i] != 1)
            {
                System.out.print(n[i]+" ");
            }
        }
        System.out.println();
    }    
}

// 57. Java Visitor Pattern
class SumInLeavesVisitor extends TreeVis {
    private int result = 0;
    public int getResult() {
        return result;
    }

    public void visitNode(TreeNode node) {
    }

    public void visitLeaf(TreeLeaf leaf) {
          result += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private long result = 1;
    private final int M = 1000000007;

    public int getResult() {
        return (int) result;
    }

    public void visitNode(TreeNode node) {
        if (node.getColor() == Color.RED) {
            result = (result * node.getValue()) % M;
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor() == Color.RED) {
            result = (result * leaf.getValue()) % M;
        }
    }
}

class FancyVisitor extends TreeVis {
    private int result = 0;
    public int getResult() {
          if(result < 0) {
            result = -result;      
        }
        return result;
    }

    public void visitNode(TreeNode node) {
        if(node.getDepth()%2 == 0 || node.getDepth() == 0) {
            this.result += node.getValue();
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
        if(leaf.getColor() == Color.GREEN) {
            this.result -= leaf.getValue();
        }
    }
}

public class Solution {  
    public static Tree solve() {
        int N;
        int[] values;
        Color[] colors;
        Map<Integer, Set<Integer>> numbers;
        
        try (Scanner s = new Scanner(System.in)) {
            N = s.nextInt();

            values = new int[N];
            for (int i=0; i<N; i++) {
                values[i] = s.nextInt();
            }

            colors = new Color[N];
            for (int i=0; i<N; i++) {
                colors[i] = (0==s.nextInt())? Color.RED : Color.GREEN;
            }

            numbers = new HashMap<>();
            for (int i=0, u, v; i<N-1; i++) {
                u = s.nextInt()-1;
                v = s.nextInt()-1;
                
                addEdge(u,v, numbers);
                addEdge(v,u, numbers);
            }
        }
        
        if (N==1) { // one node tree
            return new TreeLeaf(values[0], colors[0], 0);
        }
        
        TreeNode root = new TreeNode(values[0], colors[0], 0);
        
        class Frontier {
            public TreeNode tn;
            public int id;
            public Frontier(TreeNode n, int id) {
                tn = n;
                this.id = id;
            }
        }
        Deque<Frontier> frs = new ArrayDeque<>();
        frs.offer(new Frontier(root,0));
        
        Frontier f;
        int depth;
        Tree t;
        Set<Integer> number;
        Set<Integer> added = new HashSet<>();
        added.add(0);
        while (!frs.isEmpty()) {            
            f = frs.poll();
            number = numbers.get(f.id);
            depth = 1 + f.tn.getDepth();
            for (int numID: number) {
                if (!added.contains(numID)) {
                    if (isLeaf(numbers.get(numID), added)) {
                        t = new TreeLeaf(values[numID], colors[numID], depth);
                    } else {
                        t = new TreeNode(values[numID], colors[numID], depth);
                        frs.offer(new Frontier((TreeNode)t, numID));
                    }
                    f.tn.addChild(t);
                    added.add(numID);
                }
            }
        }

        return root;
    }
    
    static void addEdge(int u, int v, Map<Integer, Set<Integer>> numbers) {
        Set<Integer> cld;
        cld = numbers.get(u);
        if (cld==null) {
            cld = new HashSet<>();
            numbers.put(u, cld);
        }
        cld.add(v);
    }
    
    static boolean isLeaf(Set<Integer> num, Set<Integer> treeParents) {
        int nCld = num.size();
        for (int n: num) {
            if (treeParents.contains(n)) {
                nCld--;
            }
        }
        return nCld==0;
    }
	
// 58. Java Annotations
import java.lang.annotation.*;
import java.lang.reflect.*;
import java.util.*;

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface FamilyBudget {
	String userRole() default "GUEST";
	int budget();
}

class FamilyMember {
	@FamilyBudget(userRole = "SENIOR", budget = 100)
	public void seniorMember(int budget, int moneySpend) {
		System.out.println("Senior Member");
		System.out.println("Spend: " + moneySpend);
		System.out.println("Budget Left: " + (budget - moneySpend));
	}

	@FamilyBudget(userRole = "JUNIOR", budget = 50)
	public void juniorUser(int budget, int moneySpend) {
		System.out.println("Junior Member");
		System.out.println("Spend: " + moneySpend);
		System.out.println("Budget Left: " + (budget - moneySpend));
	}
}

public class Solution {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0) {
			String role = in.next();
			int spend = in.nextInt();
			try {
				Class annotatedClass = FamilyMember.class;
				Method[] methods = annotatedClass.getMethods();
				for (Method method : methods) {
					if (method.isAnnotationPresent(FamilyBudget.class)) {
						FamilyBudget family = method
								.getAnnotation(FamilyBudget.class);
						String userRole = family.userRole();
						int budgetLimit = family.budget();
						if (userRole.equals(role)) {
							if(spend <= budgetLimit){
								method.invoke(FamilyMember.class.newInstance(),
										budgetLimit, spend);
							}else{
								System.out.println("Budget Limit Over");
							}
						}
					}
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
			testCases--;
		}
	}
}

// 59. Java Lambda Expressions
 public static PerformOperation isOdd(){
    return (int a) -> a % 2 != 0;
 }  
 
 public static PerformOperation isPrime(){
    return (int a) -> java.math.BigInteger.valueOf(a).isProbablePrime(1);
 }
 
 public static PerformOperation isPalindrome(){
    return (int a) ->  Integer.toString(a).equals(new StringBuilder(Integer.toString(a)).reverse().toString());
 }
}

// 60. Java MD5
import java.io.*;
import java.util.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        String input = scan.nextLine();
        String result = md5(input);

        System.out.println(result);
    }
    
    public static String md5(String msg){
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] byteValue = md.digest(msg.getBytes());
    
            return convertByteArrayToHexString(byteValue);
        }catch(NoSuchAlgorithmException e){
                return "";
            }
    }
    
    private static String convertByteArrayToHexString(byte[] arrayBytes) {

        StringBuffer stringBuffer = new StringBuffer();

        for (int i = 0; i < arrayBytes.length; i++) {
            stringBuffer.append(Integer.toString((arrayBytes[i] & 0xff) + 0x100, 16).substring(1));
        }
        return stringBuffer.toString();
    }
}   

// 61. Java Comparator
class Checker implements Comparator<Player> {
    @Override
    public int compare (Player a, Player b){
        return (a.score>b.score?-1:(a.score==b.score)?a.name.compareTo(b.name):1);
    }
}

// 62. Java Dequeue
    import java.util.*;
    public class test {
        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            Deque<Integer> deque = new ArrayDeque<>();
            Set<Integer> set = new HashSet<>();
            
            int n = in.nextInt();
            int m = in.nextInt();
            int unique = Integer.MIN_VALUE;

            for (int i = 0; i < n; i++) {
                int num = in.nextInt();
                deque.add(num);
                set.add(num);
                
                if(deque.size() == m) {
                    if(set.size() > unique) unique = set.size();
                    int first = deque.remove();
                    if (!deque.contains(first)) set.remove(first);
                }                
            }
            
            System.out.println(unique);
        }
    }

// 63. Java Priority Queue
import java.util.PriorityQueue;
import java.util.Comparator;

class Student {
    int id;
    String name;
    double cgpa;
    
    Student(int id, String name, double cgpa){
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }
    
    int getID() {return this.id;}
    String getName() {return this.name;}
    double getCGPA() {return this.cgpa;}
}

class Priorities {
    List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> pq = new PriorityQueue(
        Comparator.comparing(Student::getCGPA).reversed()
        .thenComparing(Student::getName)
        .thenComparing(Student::getID));
        List<Student> students = new ArrayList<Student>();
        
        for (String input: events) {
            String[] s = new String[4];
            s = input.split(" ");
               
            if(s[0].equals("ENTER")){
                int id = Integer.parseInt(s[3]);
                double cgpa = Double.parseDouble(s[2]);
                pq.add(new Student(id,s[1],cgpa));
            } else if (s[0].equals("SERVED")) {
                Student first = pq.poll();
            }
        }
        
        Student first = pq.poll();
        if (first == null) {
            return students;
        } else {
            while (first != null) {
                students.add(first);
                first = pq.poll();
            }
            return students;
        }
    }
}

// 64. Java SHA-256
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.nio.charset.StandardCharsets; 
import java.security.*;
   
public class Solution {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
        messageDigest.update(s.getBytes());
        byte[] hash = messageDigest.digest();

        for (byte b : hash) {
            System.out.printf("%02x", b);
        }
    }
}
