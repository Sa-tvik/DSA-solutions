class Solution {
    public int jump(int[] nums) {
        int max =0;
        int jump = 0;
        int mr= 0;
        int n = nums.length;
        if(n == 1 && nums[0] == 0){ 
            return 0;  
        }else if(n==1 && nums[0]>0){ return 0; }

        for(int i =0;i <n;i++){
            max = Math.max(max,i+ nums[i]);
            if(i == mr){ 
                mr = max; 
                jump++; 
            }
            if(mr >= n-1){
                return jump;
            }
        }  
        return -1;
    }
}