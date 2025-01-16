class Solution {
    public static void dfs(int node,  boolean[] vis, ArrayList<ArrayList<Integer>> graph){
        vis[node] = true;
         for(Integer it: graph.get(node)){
             if(!vis[it]){
                 dfs(it, vis, graph);
             }
         }
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j] == 1 && i != j) {
                    graph.get(i).add(j);
                }
            }
        }

        boolean[] vis = new boolean[n];
        int count = 0;
        for(int i = 0;i<n;i++){
            if(!vis[i]){
                dfs(i, vis, graph);
                count++;
            }
        }
        
        return count;
    }
    
}