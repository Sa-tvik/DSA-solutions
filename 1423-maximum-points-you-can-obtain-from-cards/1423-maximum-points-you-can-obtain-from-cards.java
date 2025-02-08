class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int sum = 0, maxp= 0;
        if(k == 1){ return (cardPoints[0]>cardPoints[n-1] ? cardPoints[0] : cardPoints[n-1]); }
        
        if(k == n){ 
            int total = 0;
            for(int i = 0;i<n;i++){
                total += cardPoints[i];
            }
            return total;
         }

        for(int i = n-k;i<n;i++){
            sum += cardPoints[i];
            maxp = Math.max(maxp, sum);
        }
        int i = n-k, j = 0;
        while(j<k){
            sum -= cardPoints[i];
            sum += cardPoints[j];
            i++;
            j++;
            maxp = Math.max(maxp, sum);
        }
        return maxp;
    }
}