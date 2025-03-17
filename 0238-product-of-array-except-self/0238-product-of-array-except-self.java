class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        ans[0] = nums[0];
        for(int i = 1;i<n;i++){
            ans[i] = nums[i]*ans[i-1];
        }

        ans[n-1] = ans[n-2];
        int temp = nums[n-1];
        for(int i = n-2;i>0;i--){
            ans[i] = ans[i-1]*temp;
            temp = temp*nums[i];
        }
        ans[0] = temp;
        return ans;
    }
}