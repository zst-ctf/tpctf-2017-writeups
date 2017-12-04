class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def is_left_bracket(current):
    return current == '1' or current == '{' or current == '(' or current == '[' 

def is_right_bracket(current):
    return current == '0' or current == '}' or current == ')' or current == ']'

def is_pair_bracket(current, last):
    return (current == '0' and last == '1'
                or current == '}' and last == '{' 
                or current == ')' and last == '(' 
                or current == ']' and last == '[')

def check_balanced(str):
    if not str:
        return True

    if str.count('0') != str.count('1'):
        return False

    stack = Stack()
    for current in str:
        #current = str[i]
        if (is_left_bracket(current)):
            stack.push(current)

        if (is_right_bracket(current)):
            if stack.isEmpty():
                return False

            last = stack.peek();
            if (is_pair_bracket(current, last)):
                stack.pop();
            else:
                return False

    return stack.isEmpty()

def get_possibilities(pairs):
    # expressed in binary where 1=( and 0=)
    balanced_count = 0
    mynumb = 2**(pairs*2)
    while mynumb > 0:
        binary = bin(mynumb)[2:] # remove 0b prefix
        if check_balanced(binary):
            balanced_count += 1
        mynumb -=1
    return balanced_count

for x in range(100):
    print(f"{x} -> {get_possibilities(x)}")


    
'''


()()()()
(()()())
((())())
(()(()))
(())(())
((()()))
(((())))


{}<>[]() / {}<>[()]
{<>}[]() / {<>}[()]
{<>[]}() / {<[]>}()
{<>[]()} / {<[]>()} / {<[]()>}

n = 4
p = 3


3 possible 
'''

'''
public static String checkBalanced(String expr) {
    if (expr.isEmpty())
        return "Balanced";
 
    Stack<Character> stack = new Stack<Character>();
    for (int i = 0; i < expr.length(); i++) {
        char current = expr.charAt(i);
        if (current == '{' || current == '(' || current == '[' || current == '1') {
            stack.push(current);
        }

        
    }
return stack.isEmpty() ? "Balanced" : "Not Balanced";
}
'''