class Solution {

    // Function to calculate the sum of subarray minimums
    public static long subArrayMin(int[] nums) {
        int length = nums.length;
        int[] left = new int[length];
        int[] right = new int[length];
        
        Arrays.fill(left, -1);
        Arrays.fill(right, length);
        Deque<Integer> stack = new ArrayDeque<>();

        // Finding previous smaller element for each index
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

        // Finding next smaller element for each index
        for (int i = length - 1; i >= 0; --i) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }

        // Calculating the sum of subarray minimums
        long sumOfSubarrayMinimums = 0;
        for (int i = 0; i < length; ++i) {
            long countLeft = i - left[i];  // Number of subarrays starting from the left
            long countRight = right[i] - i;  // Number of subarrays ending on the right
            sumOfSubarrayMinimums += countLeft * countRight * nums[i];
        }

        return sumOfSubarrayMinimums;
    }

    // Function to calculate the sum of subarray maximums
    public static long subArrayMax(int[] nums) {
        int length = nums.length;
        int[] left = new int[length];
        int[] right = new int[length];
        
        Arrays.fill(left, -1);
        Arrays.fill(right, length);
        Deque<Integer> stack = new ArrayDeque<>();

        // Finding previous greater element for each index
        for (int i = 0; i < length; ++i) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                left[i] = stack.peek();
            }
            stack.push(i);
        }

        stack.clear();

        // Finding next greater element for each index
        for (int i = length - 1; i >= 0; --i) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }

        // Calculating the sum of subarray maximums
        long sumOfSubarrayMaximums = 0;
        for (int i = 0; i < length; ++i) {
            long countLeft = i - left[i];  // Number of subarrays starting from the left
            long countRight = right[i] - i;  // Number of subarrays ending on the right
            sumOfSubarrayMaximums += countLeft * countRight * nums[i];
        }

        return sumOfSubarrayMaximums;
    }

    // Function to calculate the sum of subarray ranges
    public long subArrayRanges(int[] nums) {
        long max = subArrayMax(nums);  // Sum of subarray maximums
        long min = subArrayMin(nums);  // Sum of subarray minimums
        return max - min;  // Difference between max and min sums
    }
}