// Test: Braces
class Parser{
    static String isBalanced(String s) 
    {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else if (stack.empty()) {
                return "false";
            } else {
                char top = stack.pop();
                if ((top == '(' && ch != ')') || (top == '[' && ch != ']')
                        || (top == '{' && ch != '}')) {
                    return "false";
                }
            }
        }
        if (!stack.empty()) {
            return "false";
        }
        return "true";
    }
    
}

// Test: How Will You Compare
class Comparator {
    public boolean compare(int a, int b) {
        return a == b;
    }

    public boolean compare(String a, String b) {
        return a.equals(b);
    }

    public boolean compare(int[] a, int[] b) {
        return Arrays.equals(a, b);
    }
}