class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if(n == 1 || n == 0){ return 0;  }
        int j = 1;
        int profit = 0;
        int min = Integer.MAX_VALUE;
        for(int i = 0;i<n && j<n;i++){
            if(prices[i]<min){
                min = prices[i];
            }else if(prices[i]-min>profit){ 
                profit = prices[i]-min;
            }
        }
        return profit;
    }
}