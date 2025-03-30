class Solution {
    public static double helper(double x, long n){
        if(n == 0 || x == 1){ return 1; }
        if(n%2 == 1){
            double ans = helper(x,n-1);
            return ans*x;
        }
        x = x*x;
        double ans = helper(x, n/2);
        return ans;
    }
    public double myPow(double x, int n) {
        if(x == 0) { return 0; }
        long exponent = n;
        if (n < 0) {
            x = 1.0/x;
            exponent = -exponent;
        }
        return helper(x,exponent);
    }
}