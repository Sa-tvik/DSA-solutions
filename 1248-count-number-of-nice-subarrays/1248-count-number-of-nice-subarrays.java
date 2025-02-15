class Solution {
    public int solve( int[] nums,int goal){
        if(goal<0)return 0;
        int sum = 0;
        int n = 0;
        int start = 0;
        for(int end = 0;end<nums.length;end++){
            sum += (nums[end]%2==0)?0:1;
            while(sum>goal){
                sum -= (nums[start]%2==0)?0:1;
                start++;
            }        
            n += end - start + 1;
        }
        return n;
    }
    public int numberOfSubarrays(int[] nums, int k) {
        return solve(nums,k) - solve(nums,k-1);
    }
}