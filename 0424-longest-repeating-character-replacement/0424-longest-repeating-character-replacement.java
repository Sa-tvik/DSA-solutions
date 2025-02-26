class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, r = 0,maxf = 0, maxLen = 0;
        int[] hash = new int[26];
        while(r<s.length()){
            hash[s.charAt(r) - 'A']++;
            maxf = Math.max(maxf, hash[s.charAt(r) - 'A']);
            if(r-l+1 - maxf>k){
                hash[s.charAt(l)-'A']--;
                l++;
            }
            if(r-l+1-maxf<=k){
                maxLen = Math.max(maxLen, r-l+1);
            }
            r++;
        }
        return maxLen;
    }
}