class Solution {
    public int myAtoi(String s) {
        int sign = 1, i = 0, ans = 0;
        int max = 2147483647, min = -2147483648;
        
        while(i < s.length() && s.charAt(i) == ' ') i++;

        if(i < s.length() && s.charAt(i) == '-') { sign = -1; i++; }

        if(i < s.length() && s.charAt(i) == '+') {
            if(i < s.length() && i != 0 && s.charAt(i - 1) == '-') return 0;
            sign = 1;
            i++;
        }
        
        while(i < s.length() && Character.isDigit(s.charAt(i))) {
            if(ans > ((max - (s.charAt(i) - '0')) / 10)) {
                if(sign == 1) return max;
                else return min;
            }
            ans = ans * 10 + s.charAt(i) - '0';
            i++;
        }
    
        return sign * ans;
    }
}