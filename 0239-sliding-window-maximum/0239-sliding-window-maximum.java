class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if (n == 0 || k == 0) {
            return new int[0]; 
        }
        if (k == 1) {
            return nums; 
        }
        int[] ans = new int[n-k+1];
        Deque<Integer> dq = new ArrayDeque<Integer>();
        for(int i = 0;i<n;i++){
            if(!dq.isEmpty() && dq.peekFirst()<i-k+1){
                dq.pollFirst();
            }
            while(!dq.isEmpty() && nums[dq.peekLast()]<nums[i]){
                dq.pollLast();
            }
            dq.offerLast(i);
            if (i >= k - 1) {
                ans[i - k + 1] = nums[dq.peekFirst()]; 
            }
        }
        return ans;
    }
}