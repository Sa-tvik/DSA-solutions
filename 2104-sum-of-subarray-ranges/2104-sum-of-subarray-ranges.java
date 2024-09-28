class Solution {
    public static long subArrayMin(int[] nums){
        int length = nums.length;
        int[] left = new int[length];
        int[] right = new int[length];
        
        Arrays.fill(left, -1);
        Arrays.fill(right, length);
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < length; ++i) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                left[i] = stack.peek();
            }
            stack.push(i);
        } 
        stack.clear();
        for (int i = length - 1; i >= 0; --i) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }  
        int mod = (int) 1e9 + 7;
        long answer = 0;  
        for (int i = 0; i < length; ++i) {
            answer += (long) (i - left[i]) * (right[i] - i) % mod * nums[i] % mod;
            answer %= mod;
        }
      
        return answer;
    }
    public static long subArrayMax(int[] nums){
        int N = nums.length;
        int[] pge = new int[N];
        int[] nge = new int[N];
        Stack<Integer> st = new Stack<>();
        st = new Stack<>();
        for(int i=N-1;i>=0;i--){
            while(!st.isEmpty() && nums[st.peek()]<=nums[i])
                st.pop();
            nge[i] = st.isEmpty()?N:st.peek();
            st.push(i);
        }
        st = new Stack<>();
        for(int i=0;i<N;i++){
            while(!st.isEmpty() && nums[st.peek()]<nums[i])
                st.pop();
            pge[i] = st.isEmpty()?-1:st.peek();
            st.push(i);
        }
        long sumOfSubarrayMaximums = 0;
        for(int i=0;i<N;i++){
            long cnteleleft = i-pge[i];
            long cnteleright = nge[i]-i;
            sumOfSubarrayMaximums+=cnteleleft*cnteleright*nums[i];
        }
        return sumOfSubarrayMaximums;
    }
    public long subArrayRanges(int[] nums) {
        long max = subArrayMax(nums);
        long min = subArrayMin(nums);
        return max-min;
    }
}