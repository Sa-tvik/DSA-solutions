class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Deque<Integer> st = new ArrayDeque<>();
        int area = 0;
        if( n == 1){return heights[0]; }
        for(int i = 0;i<n;i++){
            while(!st.isEmpty() &&  heights[i]<heights[st.peek()]){
                int h = st.pop();
                int pse = (st.isEmpty())?-1:st.peek();
                area = Math.max(area, heights[h]*(i-pse-1));
            }
            st.push(i);
        }
        while(!st.isEmpty()){
            int h = st.pop();
            int pse = (st.isEmpty())?-1:st.peek();
            area = Math.max(area, heights[h]*(n-pse-1));
        }
        return area;
    }
    public int maximalRectangle(char[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int max = 0;
        int[][] heights = new int[n][m];
        for(int j = 0;j<m;j++){
            int sum = 0;
            for(int i = 0;i<n;i++){
                if(matrix[i][j] == '1'){
                    sum+=1;
                }else{
                    sum = 0;
                }
                heights[i][j] = sum;
            }
        }
        for(int i = 0;i<n;i++){
            max = Math.max(max, largestRectangleArea(heights[i]));
        }
        return max;
    }
}