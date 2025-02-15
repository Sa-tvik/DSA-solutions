class Solution {
    
    public int solve( int[] nums,int goal){
        if(goal<0)return 0;
        int sum = 0;
        int n = 0;
        int start = 0;
        for(int end = 0;end<nums.length;end++){
            sum += nums[end];
            while(sum>goal){
                sum -= nums[start];
                start++;
            }        
            n += end - start + 1;
        }
        return n;
    }
    public int numSubarraysWithSum(int[] nums, int goal) {
        return solve(nums,goal) - solve(nums,goal-1);
    }
}