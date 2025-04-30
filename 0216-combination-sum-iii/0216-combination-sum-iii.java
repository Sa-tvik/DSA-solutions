class Solution {
    public void helper(int ind, int k, int target,List<List<Integer>> ans, List<Integer> arr){
        if(ind == 10 || arr.size() > k){
            if(target == 0 && arr.size() == k){ 
                ans.add(new ArrayList<>(arr));
            }
            return;
        }
        if(ind<=target){
            arr.add(ind);
            helper(ind + 1,k, target-ind, ans, arr);
            arr.remove(arr.size()-1);
        }
        if(ind<10){
            helper(ind+1,k, target, ans, arr);
        }
        
    }
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        helper(1,k,n,ans, new ArrayList<>());
        return ans;
    }
}