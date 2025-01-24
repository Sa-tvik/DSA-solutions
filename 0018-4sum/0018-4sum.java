class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
       List<List<Integer>> ans = new ArrayList<>();
        int n = nums.length;
        Arrays.sort(nums);
        for(int l = 0;l<n;l++){ 
            if (l > 0 && nums[l] == nums[l - 1]){ continue; }
           for (int i = l + 1; i < n; i++) {
                if (i > l + 1 && nums[i] == nums[i - 1]) continue;
                int j = i + 1;
                int k = n - 1;
                while (j < k) {
                    long sum = nums[i];
                    sum += nums[j];
                    sum += nums[k];
                    sum += nums[l];
                    if (sum < target) {
                        j++;
                    } else if (sum > target) {
                        k--;
                    } else {
                        List<Integer> temp = new ArrayList<>();
                        temp.add(nums[l]);
                        temp.add(nums[i]);
                        temp.add(nums[j]);
                        temp.add(nums[k]);
                        ans.add(temp);
                        j++;
                        k--;
                        while (j < k && nums[j] == nums[j - 1]) j++;
                        while (j < k && nums[k] == nums[k + 1]) k--;
                    }
                }
                
            }
        }
        return ans;
    }
}