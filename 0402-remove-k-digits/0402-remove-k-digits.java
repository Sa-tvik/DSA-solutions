class Solution {
    public String removeKdigits(String num, int k) {
        if (num.length() == k) {
            return "0";
        }
        
        StringBuilder str = new StringBuilder(); 
        for (char c : num.toCharArray()) {
            while (str.length() > 0 && k > 0 && str.charAt(str.length() - 1) > c) {
                str.deleteCharAt(str.length() - 1);  
                k--;  
            }
            str.append(c);  
        }
        while (k > 0) {
            str.deleteCharAt(str.length() - 1);
            k--;
        }
        while (str.length() > 0 && str.charAt(0) == '0') {
            str.deleteCharAt(0);
        }
        return str.length() == 0 ? "0" : str.toString();
    }
}