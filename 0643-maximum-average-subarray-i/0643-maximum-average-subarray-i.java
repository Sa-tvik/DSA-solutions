class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int i = 0;
        int j = k;
        double sum = 0;
        double max = 0;
        for (int r = 0; r < k; r++) {
            sum = sum + nums[r];
        }
        max = sum;
        while (j != nums.length) {
            sum += nums[j] - nums[i];
            i++;
            j++;
            if (max < sum) {
                max = sum ;
            }
        }
        return max/k;
    }
}