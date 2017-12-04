import java.util.Stack;
import java.util.ArrayList;
import java.util.Collections;

public class solve {

	static ArrayList<String> permutates = new ArrayList<String>();

	public static void main(String[] args) {
		// https://stackoverflow.com/questions/1235179/simple-way-to-repeat-a-string-in-java
		String brackets = String.join("", 
			Collections.nCopies(10000, "()")); 
				System.out.println("Start permutations" + brackets.length());

		// 10^4 pairs of brackets
		permutation("", brackets);
		System.out.println("Done permutations" + permutates.size());


		String checkBalancedExpr1 = checkBalanced("()()()()()()(");
		System.out.println("a*(b+c)-(d*e) : "+checkBalancedExpr1);
		String checkBalancedExpr2=checkBalanced("(a*(b-c)*{d+e}");
		System.out.println("(a*(b-c)*{d+e} : "+checkBalancedExpr2);
	}

	// https://stackoverflow.com/questions/4240080/generating-all-permutations-of-a-given-string
	private static void permutation(String prefix, String str) {
		int n = str.length();
		if (n == 0)
			permutates.add(prefix);
		else {
			for (int i = 0; i < n; i++)
				permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
		}
	}

	public static String checkBalanced(String expr) {
		if (expr.isEmpty())
			return "Balanced";
	 
		Stack<Character> stack = new Stack<Character>();
		for (int i = 0; i < expr.length(); i++) {
			char current = expr.charAt(i);
			if (current == '{' || current == '(' || current == '[' || current == '1') {
				stack.push(current);
			}

			if (current == '}' || current == ')' || current == ']' || current == '0') {
				if (stack.isEmpty())
					return "Not Balanced";
				char last = stack.peek();
				if (current == '}' && last == '{' 
					|| current == ')' && last == '(' 
					|| current == ']' && last == '['
					|| current == '0' && last == '1')
					stack.pop();
				else 
					return "Not Balanced";
			}
		}
	return stack.isEmpty() ? "Balanced" : "Not Balanced";
	}
}