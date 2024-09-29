class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        
        // Edge case: If we need to remove all digits, return "0"
        if (n == k) return "0";

        Stack<Character> st = new Stack<>();

        // Traverse each character of num
        for (int i = 0; i < n; i++) {
            char digit = num.charAt(i);
            
            // Pop elements from the stack if the current digit is smaller
            // and we still need to remove digits (k > 0)
            while (!st.isEmpty() && k > 0 && st.peek() > digit) {
                st.pop();
                k--;
            }
            // Push the current digit onto the stack
            st.push(digit);
        }

        // If we still need to remove digits (k > 0), pop remaining digits from the stack
        while (k > 0) {
            st.pop();
            k--;
        }

        // Build the result string from the stack
        StringBuilder sb = new StringBuilder();
        while (!st.isEmpty()) {
            sb.append(st.pop());
        }
        sb.reverse();

        // Remove leading zeros from the final result
        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }

        // Return the result as a string
        return sb.toString();
   }
}