class Solution {
    static boolean helper(int[] piles, int h, int k){
        int hoursNeeded = 0;
        for (int pile : piles) {
            hoursNeeded += Math.ceil((double) pile / k);
 
            if (hoursNeeded > h) {
                return false; 
            }
        }
        return true;      
    }
    public int minEatingSpeed(int[] piles, int h) { 
        int max = 0;
        for(int i = 0;i<piles.length;i++){
            max = Math.max(max,piles[i]);
        }
        int low = 1;
        int high = max;
        int min = max;

        while(low<=high){
            int mid =   low + (high-low)/2;
            if(!helper(piles, h, mid)){
                low = mid+1;
            }else {
                min = mid;
                high = mid-1;
            }
        }
        return min;
    }
}