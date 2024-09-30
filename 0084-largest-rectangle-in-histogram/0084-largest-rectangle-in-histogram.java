class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> st = new Stack<>();
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
}