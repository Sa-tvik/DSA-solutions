class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Character> queue = new LinkedList<>();
        char[] arr = senate.toCharArray();
        
        for(int i=0;i<arr.length;i++){
            queue.add(arr[i]);
        }

        while(queue.size()>0){
            Character c = queue.poll();
            boolean isRemoved = false;
            if(c == 'R'){
                isRemoved = queue.remove('D');
            }
            else{
               isRemoved = queue.remove('R');
            }
            queue.add(c); 
            if(!isRemoved){ 
                break;
            }
        }

        Character winner = queue.poll();
        if(winner == 'R'){
            return "Radiant";
        }
        else{
            return "Dire";
        }
    }
}