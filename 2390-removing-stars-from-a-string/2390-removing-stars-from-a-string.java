class Solution {
    public String removeStars(String s) {
        Stack<Character> st = new Stack<>();
        String sb = new String();
        for(int i = 0;i<s.length();i++){
            if(s.charAt(i) == '*'){
                if(!st.isEmpty()){
                    st.pop();
                }
            }else{
                st.push(s.charAt(i));
            }
        }
        
        while(!st.isEmpty()){
            sb = st.pop() + sb;     
        }
        return sb;
    }
}