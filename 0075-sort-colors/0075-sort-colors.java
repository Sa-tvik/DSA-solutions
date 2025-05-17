class Solution {
    public void sortColors(int[] nums) {
        
        int r = 0;
        int w = 0;
        int b = nums.length-1;
        while(w<=b){
            if(nums[w] == 0){
                nums[w] = nums[r]; 
                nums[r]= 0;
                r++;
                w++;
            }else if(nums[w] == 1){
                w++;
            }else if(nums[w] == 2){
                nums[w] = nums[b];
                nums[b] = 2;
                b--;
            }
        }
    }
}