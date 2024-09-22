class Solution { 
    public int findKthPositive(int[] arr, int k) {
        int n = arr.length; 
        int low = 0, high = n-1;
        int mNo = 0;
        if (arr[0] > k) {
            return k;
        }
        if(arr[n-1] == n){ return arr[n-1]+k; }
        while (low <= high) {
            int mid = (low + high) / 2;
            int nOfM = arr[mid] - (mid + 1);
            
            if (nOfM < k) {
                low = mid + 1;  
            } else {
                high = mid - 1; 
            }
        }
         return k + high + 1;
    }
}