class Solution {
    private int[] nse(int[] arr) {
        int n = arr.length;
        int[] nseDist = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                int idx = stack.pop();
                nseDist[idx] = i - idx;
            }
            stack.push(i);
        }
        
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            nseDist[idx] = n - idx;
        }
        
        return nseDist;
    }

    private int[] psee(int[] arr) {
        int n = arr.length;
        int[] pseeDist = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            pseeDist[i] = stack.isEmpty() ? i + 1 : i - stack.peek();
            stack.push(i);
        }
        
        return pseeDist;
    }
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int[] nseDist = nse(arr);
        int[] pseeDist = psee(arr);
        
        long result = 0;
        long mod = 1_000_000_007;
        
        for (int i = 0; i < n; i++) {
            long contribution = (long) arr[i] * nseDist[i] * pseeDist[i];
            result = (result + contribution) % mod;
        }
        
        return (int) result;
    }
}