class Solution {
    public  void helper(int ind,int[] nums, int target,List<List<Integer>> ans, List<Integer> arr){
        if(ind == nums.length){
            if(true){
                ans.add(new ArrayList<>(arr));
            }
            return;
        }
        if(true){
            arr.add(nums[ind]);
            helper(ind+1, nums, target, ans, arr);
            arr.remove(arr.size()-1);
        }
        helper(ind+1, nums, target, ans, arr);
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        helper(0,nums,0,ans,new ArrayList<>());
        return ans;
    }
}