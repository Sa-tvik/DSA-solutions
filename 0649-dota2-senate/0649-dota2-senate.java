class Solution {
    public String predictPartyVictory(String senate) {
        int r = 0, d = 0;
        boolean bool = false;
        if(senate.charAt(0) == 'R'){ bool = true; }
        for(int i = 0; i<senate.length();i++){
            if(senate.charAt(i) == 'R'){
                r++;
            }else{ d++; }
        }
        if(r == d){ return (bool) ? "Radiant" : "Dire"; }

        if(r>d){
            if(bool){
                return "Radiant";
            }else if(!bool && r-d == 1){
                return "Dire";
            }else{ return "Radiant"; }
        }else{
            if(!bool){
                return "Dire";
            }else if(bool && d-r == 1){
                return "Dire";
            }else{ return "Radiant"; }
        }
    }
}