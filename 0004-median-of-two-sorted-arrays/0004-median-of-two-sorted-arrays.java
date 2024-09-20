class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int n = n1 + n2;
        
        int ind1 = (n - 1) / 2;  // First middle index (for even, it's the smaller of two middle elements)
        int ind2 = n / 2;        // Second middle index (for even, it's the larger one)
        int cnt = 0;             // To track the number of elements processed
        int ind1el = -1, ind2el = -1; // To store the two median elements
        
        int i = 0, j = 0;  // Pointers for nums1 and nums2
        
        while (i < n1 && j < n2) {
            int val;
            if (nums1[i] < nums2[j]) {
                val = nums1[i];
                i++;
            } else {
                val = nums2[j];
                j++;
            }
            
            if (cnt == ind1) ind1el = val; 
            if (cnt == ind2) ind2el = val; 
            cnt++;
        }


        while (i < n1) {
            if (cnt == ind1) ind1el = nums1[i];
            if (cnt == ind2) ind2el = nums1[i];
            i++;
            cnt++;
        }

        while (j < n2) {
            if (cnt == ind1) ind1el = nums2[j];
            if (cnt == ind2) ind2el = nums2[j];
            j++;
            cnt++;
        }

    
        if (n % 2 == 1) {
            return (double) ind2el;
        }
        

        return (double) (ind1el + ind2el) / 2.0;
    }
}
