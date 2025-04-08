class Solution {
    public void helper(int ind,int[] candidates, int target,List<List<Integer>> ans, List<Integer> arr){
        if(ind == candidates.length){
            if(target == 0){
                ans.add(new ArrayList<>(arr));
            }
            return;
        }

        if(candidates[ind]<=target){
            arr.add(candidates[ind]);
            helper(ind+1, candidates, target-candidates[ind], ans, arr);
            arr.remove(arr.size()-1);
        }
        while(ind<candidates.length-1 && candidates[ind] == candidates[ind+1]){ ind++; }
        if(ind<candidates.length){
            helper(ind+1, candidates, target, ans, arr);
        }
        
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans = new ArrayList<>();
        helper(0, candidates, target, ans, new ArrayList<>());
        return ans;
    }
}