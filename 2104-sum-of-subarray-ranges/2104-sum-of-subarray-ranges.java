class Solution {

    public static long subArrayMin(int[] nums) {
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

        long sumOfSubarrayMinimums = 0;
        for (int i = 0; i < length; ++i) {
            long countLeft = i - left[i];
            long countRight = right[i] - i;
            sumOfSubarrayMinimums += countLeft * countRight * nums[i];
        }

        return sumOfSubarrayMinimums;
    }

    public static long subArrayMax(int[] nums) {
        int length = nums.length;
        int[] left = new int[length];
        int[] right = new int[length];

        Arrays.fill(left, -1);
        Arrays.fill(right, length);
        Deque<Integer> stack = new ArrayDeque<>();

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

        for (int i = length - 1; i >= 0; --i) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }

        long sumOfSubarrayMaximums = 0;
        for (int i = 0; i < length; ++i) {
            long countLeft = i - left[i];
            long countRight = right[i] - i;
            sumOfSubarrayMaximums += countLeft * countRight * nums[i];
        }

        return sumOfSubarrayMaximums;
    }

    public long subArrayRanges(int[] nums) {
        long max = subArrayMax(nums);
        long min = subArrayMin(nums);
        return max - min;
    }
}